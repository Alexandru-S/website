from flask import render_template, Blueprint, request, flash, redirect, url_for

index_blueprint = Blueprint('index', __name__, template_folder='templates')


@index_blueprint.route('/index', methods=['GET', 'POST'])   # pragma: no cover
def index():
    if request.method == 'GET':
        print("get meyhod here")
        return "works on get method"
