from flask import Blueprint, render_template, request
from www.models import tic_buy

bp = Blueprint('refund', __name__, url_prefix='/')

@bp.route('/refund')
def refund():
    if request.method == "GET":
        buyId = request.args.get('buyid')
        
    buyId = "4"
    buyData = tic_buy.query.filter_by(tic_buy_bid=buyId).first()
    
    bMethod = ""
    if buyData.tic_buy_mthd == "1":
        bMethod = "휴대폰"
    elif buyData.tic_buy_mthd == "2":
        bMethod = "카드"        
    elif buyData.tic_buy_mthd == "2":
        bMethod = "계좌이체"
        
    return render_template(
        'nrefund.html',
        buyData=buyData, bMethod=bMethod
        #buyData=buyData, seatData=seatData, price=price, bMethod=bMethod
    )
