from flask import Blueprint, render_template, request
from www.models import tic_mbr

bp = Blueprint('user_modify', __name__, url_prefix='/')

@bp.route('/userModify', methods=["GET", "POST"])
def modify():
    if request.method == "GET":
        userId = request.args.get('userid')
    
    userData = tic_mbr.query.filter_by(tic_mbr_usrid=userId).first()

    return render_template(
        'user_modify.html', userData=userData
    )
