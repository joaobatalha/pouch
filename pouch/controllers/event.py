import datetime
import uuid
from PIL import Image
from flask import Blueprint, request, render_template
import json, pdb, os
from pouch import connection
from pouch import app
from pouch.models.event import Event as eventModel
import pouch.controllers.babysitter as bb_controller
from datetime import datetime

event = Blueprint('event', __name__)

@event.route('/register_event', methods=['POST'])
def register_event():
    json_request = json.loads(request.form['json_payload'])
    pdb.set_trace()
    event_uuid = unicode(uuid.uuid4().hex[:5])
    child_uuid = json_request['child_uuid']
    # starting_time = json_request['starting_time']
    # ending_time = json_request['ending_time']
    reminders = json_request['reminders']
    house_rules = json_request['house_rules']
    event = connection.Event()
    event['event_uuid'] = unicode(event_uuid)
    event['child_uuid'] = unicode(child_uuid)
    event['house_rules'] = house_rules
    # event['starting_time'] =
    # event['ending_time'] =
    event['reminders'] = json_request['reminders']
    event.save()
    return json.dumps(event_uuid)

@event.route('/set_babysitter', methods=['POST'])
def set_babysitter():
    json_request = json.loads(request.form['json_payload'])
    event_uuid = json_request['event_uuid']
    babysitter_uuid = json_request['babysitter_uuid']
    e = connection.pouch.events.find_and_modify({'event_uuid' : event_uuid}, {"$set" : {'babysitter_uuid' : babysitter_uuid}})
    ev = connection.Event.find_one({'event_uuid' : event_uuid })
    return ev.to_json()

@event.route('/post_moment', methods=['POST'])
def post_moment():
    json_request = json.loads(request.form['json_payload'])
    event_uuid = json_request['event_uuid']
    moment = json_request['moment']
    if moment['type'] == 'photo':
        try:
            if request.files:
                photo = request.files['photo']
                filename = photo.filename
                photo_path = app.config['UPLOAD_LOCATION']
                photo_full_path = photo_path + '/' + filename
                photo.save(os.path.join(app.config['UPLOAD_LOCATION'], filename))
                img = Image.open(photo_full_path)
                width, height = img.size
                photo = {
                    'path' : unicode('192.168.1.31/~joaobatalha/images/'),
                    'file' : unicode(filename),
                    'width' : width,
                    'height' : height
                }
                moment = {
                    'type' : 'photo',
                    'timestamp' : moment['timestamp'],
                    'photo' : photo
                }
                event = connection.pouch.events.find_and_modify({'event_uuid' : event_uuid}, {"$push" : {'moments' : moment}})
        except:
            pass
    else:
        event = connection.pouch.events.find_and_modify({'event_uuid' : event_uuid}, {"$push" : {'moments' : moment}})
    return 'moment added'

@event.route('/get_moments', methods=['GET'])
def get_moments():
    event_uuid = request.args.get('event_uuid')
    e = connection.Event.find_one({'event_uuid' : event_uuid})
    to_return = e.get('moments')
    return json.dumps(to_return)

@event.route('/get_reminders', methods=['GET'])
def get_reminders():
    event_uuid = request.args.get('event_uuid')
    e = connection.Event.find_one({'event_uuid' : event_uuid})
    to_return = e.get('reminders')
    return json.dumps(to_return)

@event.route('/get_feed', methods=['GET'])
def get_reminders():
    event_uuid = request.args.get('event_uuid')
    e = connection.Event.find_one({'event_uuid' : event_uuid})
    moments = e.get('moments')
    reminders = e.get('reminders')
    to_return = {
        'moments' : moments,
        'reminders' : reminders
    }
    return json.dumps(to_return)

@event.route('/start_babysitting', methods=['GET'])
def start_babysitting():
    event_uuid = request.args.get('event_uuid')
    date = datetime.utcnow()
    e = connection.pouch.events.find_and_modify({'event_uuid' : event_uuid}, {"$set" : {'started_babysitting_ts' : date}})
    return 'started babysitting'

@event.route('/finish_babysitting', methods=['GET'])
def finish_babysitting():
    event_uuid = request.args.get('event_uuid')
    finished = datetime.utcnow()
    e = connection.pouch.events.find_one({'event_uuid' : event_uuid})
    started = e.get('started_babysitting_ts')
    interval = finished - started
    babysitter_uuid = e['babysitter_uuid']
    rate = bb_controller.get_rate(babysitter_uuid)
    hours = round(interval.seconds / 3600.00, 2)
    total = rate * hours
    to_return = {
        'rate' : rate,
        'hours' : hours,
        'total' : total
    }
    print json.dumps(to_return)
    return json.dumps(to_return)




