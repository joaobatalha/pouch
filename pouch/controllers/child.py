import datetime
import uuid
from PIL import Image
from flask import Blueprint, request, render_template
import json, pdb, os
from pouch import connection
from pouch import app
from pouch.models import child
from datetime import datetime

child = Blueprint('child', __name__)

@child.route('/register_child', methods=['POST'])
def register_child():
    json_request = json.loads(request.form['json_payload'])
    first_name = json_request['first_name']
    user_id = unicode(uuid.uuid4().hex[:11])
    last_name = json_request['last_name']
    gender = json_request['gender']
    emergency_contacts = json_request['emergency_contacts']
    age = json_request['age']
    # concerns = json_request['concerns']
    allergies = json_request['allergies']
    photo_path = app.config['UPLOAD_LOCATION']
    child = connection.Child()
    child['first_name'] = unicode(first_name)
    child['last_name'] = unicode(last_name)
    child['gender'] = unicode(gender)
    child['age'] = int(age)
    child['emergency_contacts'] = emergency_contacts
    # child['concerns'] = concerns
    child['allergies'] = allergies
    child['uuid'] = user_id
    try:
        if request.files:
            pdb.set_trace()
            photo = request.files['photo']
            filename = photo.filename
            photo_full_path = photo_path + '/' + filename
            photo.save(os.path.join(app.config['UPLOAD_LOCATION'], filename))
            img = Image.open(photo_full_path)
            width, height = img.size
            child['photo'] = {
                'path' : unicode('192.168.1.31/~joaobatalha/images/'),
                'file' : unicode(filename),
                'width' : width,
                'height' : height
            }

    except:
        pass
    child.save()
    return json.dumps(user_id)