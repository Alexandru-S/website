from flask import render_template, Blueprint, request, flash, redirect, url_for

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/admin', methods=['GET', 'POST'])   # pragma: no cover
def admin():
    if request.method == 'GET':
        print("get meyhod here")
        return "works on get method"
