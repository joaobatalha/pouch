from mongokit import Document
from pouch import connection
from datetime import datetime

@connection.register
class Child(Document):
        __collection__= 'children'
        __database__= 'pouch'
        structure = {
                'first_name' : unicode,
                'last_name' : unicode,
                'creation' : datetime,
                'uuid' : unicode,
                'gender' : unicode,
                'emergency_contacts' : [
                    {
                        'name' : unicode,
                        'number' : int
                    }
                ],
                'age' : int,
                'concerns' : [unicode],
                'allergies' : [unicode],
                'photo' : {
                        'url' : unicode,
                        'file' : unicode,
                        'width' : int,
                        'height' : int
                }
        }
        required_fields = ['first_name', 'last_name']
        default_values = {'creation' : datetime.utcnow()}
        use_dot_notation = True

connection.register([Child])
