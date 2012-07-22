import datetime
import uuid
from PIL import Image
from flask import Blueprint, request, render_template
import json, pdb, os
from pouch import connection
from pouch import app
from pouch.models import babysitter
from datetime import datetime

babysitter = Blueprint('babysitter', __name__)

@babysitter.route('/register_babysitter', methods=['POST'])
def register_babysitter():
    json_request = json.loads(request.form['json_payload'])
    user_id = unicode(uuid.uuid4().hex[:11])
    first_name = json_request['first_name']
    last_name = json_request['last_name']
    rate = json_request['rate']
    phone_number = json_request['phone_number']
    photo_path = app.config['UPLOAD_LOCATION']
    babysitter = connection.Babysitter()
    babysitter['first_name'] = unicode(first_name)
    babysitter['last_name'] = unicode(last_name)
    babysitter['rate'] = float(rate)
    babysitter['phone_number'] = int(phone_number)
    babysitter['uuid'] = unicode(user_id)
    try:
        if request.files:
            photo = request.files['photo']
            filename = photo.filename
            photo_full_path = photo_path + '/' + filename
            photo.save(os.path.join(app.config['UPLOAD_LOCATION'], filename))
            img = Image.open(photo_full_path)
            width, height = img.size
            babysitter['photo'] = {
                'path' : unicode('192.168.1.31/~joaobatalha/images/'),
                'file' : unicode(filename),
                'width' : width,
                'height' : height
            }

    except:
        pass
    babysitter.save()
    return json.dumps(user_id)

def get_rate(uuid):
    b = connection.pouch.babysitters.find_one({'uuid' : uuid})
    rate = b.get('rate')
    return rate
