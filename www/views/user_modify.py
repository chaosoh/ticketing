from flask import Blueprint, render_template

bp = Blueprint('user_modify', __name__, url_prefix='/')

@bp.route('/userModify')
def index():
    return render_template(
        'user_modify.html'
    )
