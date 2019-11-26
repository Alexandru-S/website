from flask import render_template, Blueprint, request, flash, redirect, url_for

contact_blueprint = Blueprint('contact', __name__, template_folder='templates')


@contact_blueprint.route('/contact', methods=['GET', 'POST'])   # pragma: no cover
def contact():
    if request.method == 'GET':
        return render_template('contact.html')