from flask import Blueprint, render_template

bp = Blueprint('refund', __name__, url_prefix='/')

@bp.route('/refund')
def index():
    return render_template(
        'refund.html'
    )
