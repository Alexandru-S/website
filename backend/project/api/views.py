from flask import render_template, Blueprint, request, flash, redirect, url_for

api_blueprint = Blueprint('api', __name__, template_folder='templates')


@api_blueprint.route('/api', methods=['GET', 'POST'])   # pragma: no cover
def api():
    if request.method == 'GET':
        print("get meyhod here")
        return "works on get method"

