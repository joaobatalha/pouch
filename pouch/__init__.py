import os

FLASK_APP_DIR = os.path.dirname(os.path.abspath(__file__))

from flask import Flask
app = Flask(__name__)
app.debug = True

#Config
if os.getenv('DEV') == 'True':
        app.config.from_object('pouch.config.DevelopmentConfig')
        app.logger.info('Config: Development')
elif os.getenv('STAGING') == 'True':
        app.config.from_object('pouch.config.StagingConfig')
        app.logger.info('Config: Staging')
else:
        app.config.from_object('pouch.config.ProductionConfig')
        app.logger.info('Config: Production')

#Logging
import logging
logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
        datefmt='%Y%m%d-%H:%M%p',
)

#from flaskext.assets import Environment
#assets = Environment(app)
#assets_output_dir = os.path.join(FLASK_APP_DIR, 'static', 'gen')
#if not os.path.exists(assets_output_dir):
#        os.mkdir(assets_output_dir)

#Database Connection
from mongokit import Connection, Document
connection = Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])

from pouch.controllers.frontend import frontend
from pouch.controllers.child import child
from pouch.controllers.babysitter import babysitter
from pouch.controllers.event import event
app.register_blueprint(frontend)
app.register_blueprint(child)
app.register_blueprint(babysitter)
app.register_blueprint(event)

