from flask import Flask

import os

app = Flask(__name__)


from project.index.views import index_blueprint
from project.admin.views import admin_blueprint
#from project.entity.views import entity_blueprint
from project.api.views import api_blueprint

app.register_blueprint(index_blueprint)
app.register_blueprint(admin_blueprint)
#app.register_blueprint(entity_blueprint)
app.register_blueprint(api_blueprint)