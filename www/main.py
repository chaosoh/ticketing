from flask import Flask, render_template #, redirect,url_for
from flask import request
import pymysql.cursors

app = Flask(__name__)

# MySQL configurations 
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='choh3722',
                       db='ticketing',
                       charset='utf8mb4')

#cursor = conn.cursor()

@app.route('/nmodify.html')
def index():
    userId = "hong"

    cursor1 = conn.cursor()
    query = "SELECT * FROM tic_mbr where tic_mbr_usrid='"+userId+"'"
    cursor1.execute(query)
    userData = cursor1.fetchone()

    cursor1.close()
    #conn.close()

    userTel = userData[2]
    result1= userTel[0:3]
    result2= userTel[3:7]
    result3= userTel[7:11]

    userTel = result1+"-"+result2+"-"+result3

    return render_template(
        'nmodify.html',
        userData=userData,
        userTel=userTel
    )

@app.route('/nmodify_result.html',  methods=['POST'])
def success():
    form_data = request.form
    userid = form_data['user_id']
    userName = form_data['name']
    userTel = form_data['tel']
    gender = form_data['gender']
    birthday = form_data['birthday']
    email = form_data['email']
    address = form_data['address']
    h_point = form_data['user_hpoint']
    n_point = form_data['user_npoint']
    grade = form_data['user_grade']
    
    if gender=='m':
        user_gender = '남자'
    if gender=='f':
        user_gender = '여자'

    cursor2 = conn.cursor()

    query = "update tic_mbr set tic_mbr_tel='"+userTel+"', tic_mbr_gender='"+gender+"'"
    query = query+", tic_mbr_bthday='"+birthday+"'"+", tic_mbr_email='"+email+"'"
    query = query+", tic_mbr_addr='"+address+"'"+" where tic_mbr_usrid='"+userid+"'"

    cursor2.execute(query)
    conn.commit()    
    cursor2.close()
    #conn.close()

    userData = [userid, userName, userTel, birthday, email, address, user_gender, h_point, n_point, grade]

    return render_template(
        'nmodify_result.html',
        userData=userData
    )

@app.route('/nrefund.html')
def cancel():
    buy_id = "4"
    cursor3 = conn.cursor()
    query = "SELECT * FROM ticketing.tic_buy inner join ticketing.tic_con on "
    query = query+"ticketing.tic_buy.tic_con_cid=ticketing.tic_con.tic_con_cid where tic_buy_bid='"+buy_id+"'";
    cursor3.execute(query)
    buyData = cursor3.fetchone()

    bMethod = ""
    if buyData[2] == "1":
        bMethod = "휴대폰"
    elif buyData[2] == "2":
        bMethod = "카드"
    elif buyData[2] == "2":
        bMethod = "계좌이체"

    query = "select * from ticketing.tic_bst where ticketing.tic_bst.tic_buy_bid='"+buy_id+"'";
    cursor3.execute(query)
    seatData = cursor3.fetchone()

    cursor3.close()

    price = 0
    if seatData[1] == "S":
        price = seatData[2]*20000
    elif seatData[1] == "A":
        price = seatData[2]*15000
    elif seatData[1] == "B":
        price = seatData[2]*10000    

    return render_template(
        'nrefund.html',
        buyData=buyData, seatData=seatData, price=price, bMethod=bMethod
    )

#cursor.close()
#conn.close()

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="127.0.0.1", port="80", debug=True)
