from mongokit import Document
from pouch import connection
from datetime import datetime

#Types of reminders:
# sleep
# food
# medicine

# Types of moments:
# text
# photo
# sleep
# toilet
# video


@connection.register
class Event(Document):
        __collection__= 'events'
        __database__= 'pouch'
        use_schemaless = True
        structure = {
                'reminders' : [
                    {
                        'type' : unicode,
                        'timestamp' : unicode,
                        'description' : unicode
                    }
                    ],
                # 'moments' : [
                # {
                #     'type' : unicode,
                #     'time' : datetime,
                #     'description' : unicode
                # }
                # ],

                'started_babysitting_ts' : datetime,
                'starting_ts' : datetime,
                'ending_ts' : datetime,
                'babysitter_uuid' : unicode,
                'child_uuid' : unicode,
                'event_uuid' : unicode,
                'house_rules' : [unicode]
        }
        use_dot_notation = True

connection.register([Event])
