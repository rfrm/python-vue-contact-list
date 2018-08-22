import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import click

app = Flask(__name__)
from . import config
app.logger.info('>>> {}'.format(config.flask_config))

db = SQLAlchemy(app)

from app.api import api_rest, api_bp
from app.client import client_bp

app.register_blueprint(api_bp)
app.register_blueprint(client_bp)
