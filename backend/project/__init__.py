from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from project.index.views import index_blueprint
from project.admin.views import admin_blueprint
from project.entity.views import entity_blueprint
from project.api.views import api_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)