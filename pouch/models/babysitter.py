from mongokit import Document
from pouch import connection
from datetime import datetime

@connection.register
class Babysitter(Document):
        __collection__= 'babysitters'
        __database__= 'pouch'
        structure = {
                'first_name' : unicode,
                'last_name' : unicode,
                'creation' : datetime,
                'rate' : float,
                'phone_number' : int,
                'uuid' : unicode,
                'photo' : {
                        'path' : unicode,
                        'file' : unicode,
                        'width' : int,
                        'height' : int
                }
        }
        required_fields = ['first_name', 'last_name']
        default_values = {'creation' : datetime.utcnow()}
        use_dot_notation = True

connection.register([Babysitter])
