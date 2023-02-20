from www import db

class tic_mbr(db.Model):
    tic_mbr_usrid = db.Column(db.String(20), primary_key=True)
    tic_mbr_name = db.Column(db.String(10), nullable=False)
    tic_mbr_tel = db.Column(db.String(10), nullable=False)
    tic_mbr_gender = db.Column(db.String(10), nullable=False)
    tic_mbr_bthday = db.Column(db.String(10), nullable=False)
    tic_mbr_email = db.Column(db.String(30), nullable=True)
    tic_mbr_addr = db.Column(db.String(10), nullable=False)
    tic_mbr_hpoint = db.Column(db.String(10), nullable=False)
    tic_mbr_npoint = db.Column(db.String(10), nullable=False)
    tic_mbr_grade = db.Column(db.String(10), nullable=False)
