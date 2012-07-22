import datetime

from flask import Blueprint, request, render_template
from pouch import app

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
        if app.debug:
                app.logger.debug('rendering index')
        return render_template(
                'index.html',
                config=app.config,
                now=datetime.datetime.now,
                )
