class Config(object):
        SECRET_KEY = '{SECRET_KEY}'
        SITE_NAME = 'Pouch'
        SYS_ADMINS = ['joao@pouch.com']

# Dont forget that you have to set env variables, eg. DEV
class ProductionConfig(Config):
        DEBUG = True
        TESTING = True
        #change this when it is eventully deployed
        MONGODB_DATABASE = 'pouch'
        MONGODB_HOST = 'localhost'
        MONGODB_PORT = 27017
        APP_SECRET_KEY = '\xa9^\xf3\x0e\xa2\xd4X\xe7\x1f\xbfj\x95\t\x82(\xf4\xebF\xee){\x9f\xb8\xfe'
        UPLOAD_LOCATION = "/Users/joaobatalha/Sites/images"

class StagingConfig(Config):
        DEBUG = True
        TESTING = True
        MONGODB_DATABASE = 'pouch'
        MONGODB_HOST = 'localhost'
        MONGODB_PORT = 27017
        APP_SECRET_KEY = '\xa9^\xf3\x0e\xa2\xd4X\xe7\x1f\xbfj\x95\t\x82(\xf4\xebF\xee){\x9f\xb8\xfe'
        UPLOAD_LOCATION = "/Users/joaobatalha/Sites/images"

class DevelopmentConfig(Config):
        DEBUG = True
        TESTING = True
        MONGODB_DATABASE = 'pouch'
        MONGODB_HOST = 'localhost'
        MONGODB_PORT = 27017
        APP_SECRET_KEY = '\xa9^\xf3\x0e\xa2\xd4X\xe7\x1f\xbfj\x95\t\x82(\xf4\xebF\xee){\x9f\xb8\xfe'
        UPLOAD_LOCATION = "/Users/joaobatalha/Sites/images"