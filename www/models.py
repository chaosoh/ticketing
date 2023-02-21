from www import db

class tic_mbr(db.Model):
    tic_mbr_usrid = db.Column(db.String(20), primary_key=True)
    tic_mbr_name = db.Column(db.String(10), nullable=False)
    tic_mbr_tel = db.Column(db.String(11), nullable=True)
    tic_mbr_gender = db.Column(db.String(1), nullable=True)
    tic_mbr_bthday = db.Column(db.Date(), nullable=True)
    tic_mbr_email = db.Column(db.String(30), nullable=True)
    tic_mbr_addr = db.Column(db.String(100), nullable=True)
    tic_mbr_hpoint = db.Column(db.Integer, nullable=True)
    tic_mbr_npoint = db.Column(db.Integer, nullable=True)
    tic_mbr_grade = db.Column(db.Integer, nullable=True)
    tic_mbr_passwd = db.Column(db.String(64), nullable=False)

class tic_buy(db.Model):
    tic_buy_bid = db.Column(db.Integer, primary_key=True)
    tic_mbr_usrid = db.Column(db.String(20), nullable=False)
    tic_buy_mthd = db.Column(db.String(1), nullable=True)
    tic_buy_bdate = db.Column(db.Date(), nullable=True)
    tic_con_cid = db.Column(db.Integer, nullable=True)
    tic_non_tel = db.Column(db.String(11), nullable=True)

class tic_bst(db.Model):
    tic_bst_uid = db.Column(db.Integer, primary_key=True)
    tic_bst_seat = db.Column(db.String(2), nullable=True)
    tic_bst_num = db.Column(db.Integer, nullable=True)
    tic_buy_bid = db.Column(db.String(3), nullable=False)
    