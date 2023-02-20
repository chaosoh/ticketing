from flask import Blueprint, render_template, url_for
#from werkzeug.utils import redirect
from www.models import tic_mbr

bp = Blueprint('userList', __name__, url_prefix='/')

@bp.route('/userList')
def _list():
    member_list = tic_mbr.query.order_by(tic_mbr.tic_mbr_usrid.desc())
    
    return render_template('member_list.html', member_list=member_list)
    #return redirect(url_for('question._list'))
