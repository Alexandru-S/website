from flask import render_template, Blueprint, request

contact_blueprint = Blueprint('contact', __name__, template_folder='templates')


@contact_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    """ Returns the HTML for contacts page.
    Args:
      none: takes no args for now.

    Returns:
      contact.html file if request is GET
    """
    if request.method == 'GET':
        return render_template('contact.html')
