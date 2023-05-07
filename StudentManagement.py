from flask import Flask,redirect, render_template,url_for,request
import sqlite3 as sql
from flask_mail import Mail, Message
import os
import math
import random
import smtplib

app = Flask(__name__)
mail = Mail(app)

@app.route('/')
def Home():
    return render_template("StudentManagement_Home.html")  

@app.route('/AddStudent', methods=['POST','GET'])
def AddStudent():
    if request.method == 'POST':
        Sid = request.form['s']
        Name = request.form['n']
        Age = request.form['a']
        Email = request.form['e']
        PhoneNo = request.form['p']
        Address = request.form['ad']
        Course = request.form['c']
        
        db = sql.connect("std.db")
        data = db.cursor()
            
        Sid = request.form['s']
        # data.execute('create table std(Sid varchar(1000)not null , Name varchar(20) not null, Age int, Email varchar(20)primary key not null, PhoneNo varchar(15), Address varchar(50) not null, Course varchar(20) not null)')
        SID = request.form['s']
        data.execute(f"SELECT count(Sid) FROM std WHERE Sid = {SID}")
        
        a = 10
        b = 10
             
        if len(PhoneNo) < 10 or len(PhoneNo) > 10:
            msg = "Please Enter 10 Digits Phone Number...!!!"
            return render_template("StudentManagement_Add.html", msg = msg)
            
        if data.fetchone()[0] > 0:
            Msg = "Sid Alredy Taken...!!!"
            return render_template("StudentManagement_Add.html", Msg = Msg)

        if a == b :
            EMAIL = request.form['e']
            a=data.execute(f"SELECT count(Email) from std WHERE Email='{Email}'")
            
            if data.fetchone()[0] > 0 :
                MSG = "Email Already Exists...!!!"
                return render_template("StudentManagement_Add.html", MSG = MSG)
            
            else:
                digits = "0123456789"
                global OTP1
                OTP1 = ""
                for i in range(4): 
                    OTP1 += digits[math.floor(random.random()*10)]
                global otp
                otp = OTP1 + " is Your OTP...!!!"        
                msg = otp
                print(OTP1)
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("yssaini0117@gmail.com", "cavander@0")
                emailid = Email
                s.sendmail('&&&&&&&&&&&',emailid,msg)
                 
                

                return render_template("StudentManagement_Addotp.html")
                db.close()   

    return render_template("StudentManagement_Add.html")



@app.route('/Submit', methods=['POST','GET'])
def Submit():
    # AddStudent.otp()
    print(OTP1)
    a = OTP1
    OTP = request.form['o']
    if OTP == a :
        Msg = ""
        print("OTP Matched Successfully...!!!")

        db = sql.connect("std.db")
        data = db.cursor()

        data.execute(f'''insert into std values({Sid},'{Name}',{Age},'{Email}','{PhoneNo}','{Address}','{Course}')''')
        db.commit()
        db.rollback()
        return render_template("StudentManagement_Add1.html")
    else:
        error = "Incorrect OTP...!!!"
        return render_template("StudentManagement_Addotp.html", error = error)

@app.route('/FindStudent', methods=['POST','GET'])
def FindStudent():
    if request.method == 'POST':
        db = sql.connect("std.db")
        db.row_factory = sql.Row
        data = db.cursor()
        
        Sid = request.form['s']
        data.execute(f"SELECT * FROM std WHERE Sid = {Sid}")
        
        rows = data.fetchall()
        print("You Have Successfully Finded...!!!")
        return render_template("StudentManagement_Find.html", rows = rows)

    return render_template("StudentManagement_Find.html")

@app.route('/FindStudent/ByName', methods=['POST','GET'])
def FindStudentByName():
    if request.method == 'POST':
        db = sql.connect("std.db")
        db.row_factory = sql.Row
        data = db.cursor()

        error = None
        NAME = request.form['n']
        data.execute(f"SELECT count(Name) FROM std WHERE Name = '{NAME}'")

        if data .fetchone()[0] > 1:
            error = "invalid password" 
            return render_template("StudentManagement_findname.html", error = error)     
        else:
            Name = request.form['n']
            data.execute(f"SELECT * FROM std WHERE Name = '{Name}'")
        
            rows = data.fetchall()
            print("You Have Successfully Finded...!!!")
            return render_template("StudentManagement_Find.html", rows = rows)

    return render_template("StudentManagement_Find.html")

@app.route('/FindStudent/Byname1', methods=['POST','GET'])
def FindStudentByname1():
    if request.method == 'POST':
        db = sql.connect("std.db")
        db.row_factory = sql.Row
        data = db.cursor()

        Sid = request.form['s']
        data.execute(f"SELECT * FROM std WHERE Sid = {Sid}")

        rows = data.fetchall()
        print("You Have Successfully Finded...!!!")
        return render_template("StudentManagement_findname.html", rows = rows)

    return render_template("StudentManagement_findname.html")

@app.route('/FindStudent/ByEmail', methods=['POST','GET'])
def FindStudentByEmail():
    if request.method == 'POST':
        db = sql.connect("std.db")
        db.row_factory = sql.Row
        data = db.cursor()
        
        Email = request.form['e']
        data.execute(f"SELECT * FROM std WHERE Email = '{Email}'")
        
        rows = data.fetchall()
        print("You Have Successfully Finded...!!!")
        return render_template("StudentManagement_Find.html", rows = rows)

    return render_template("StudentManagement_Find.html")

@app.route('/FindStudent/ByCourse', methods=['POST','GET'])
def FindStudentByCourse():
    if request.method == 'POST':
        db = sql.connect("std.db")
        db.row_factory = sql.Row
        data = db.cursor()
        
        Course = request.form['c']
        data.execute(f"SELECT * FROM std WHERE Course = '{Course}'")
        
        rows = data.fetchall()
        print("You Have Successfully Finded...!!!")
        return render_template("StudentManagement_Find.html", rows = rows)

    return render_template("StudentManagement_Find.html")

@app.route('/RemoveStudent', methods=['POST','GET'])
def RemoveStudent():
    if request.method == 'POST':
        db = sql.connect("std.db")
        data = db.cursor()

        Sid = request.form['s']
        data.execute(f"DELETE FROM std where Sid = {Sid}")
        db.commit()
        print("You Have Successfully Removed...!!!")

    return render_template("StudentManagement_Remove.html")

@app.route('/RemoveStudent/ByName', methods=['POST','GET'])
def RemoveStudentByName():
    if request.method == 'POST':
        db = sql.connect("std.db")
        data = db.cursor()

        Name = request.form['n']
        Name1 = data.execute(f"SELECT * FROM std WHERE Name = '{Name}'")

        rows = data.fetchall()
        error = None

        if Name == Name1 :
            error = "invalid password" 
            return render_template("StudentMangement_Remove1.html", error = error)      
        else:
            data.execute(f"DELETE FROM std where Name = '{Name}'")
            db.commit()
            print("You Have Successfully Removed...!!!")
        
    return render_template("StudentManagement_Remove.html")

@app.route('/Remove1/BySid', methods=['POST','GET'])
def Remove1BySid():
    if request.method == 'POST':
        db = sql.connect("std.db")
        data = db.cursor()
        Sid = request.form['s']
        data.execute(f"DELETE FROM std where Sid = {Sid}")
        db.commit()
        print("You Have Successfully Removed...!!!")

    return render_template("StudentMangement_Remove1.html")
    
@app.route('/ShowStudent', methods=['POST','GET'])
def ShowStudent():
    db = sql.connect("std.db")
    db.row_factory = sql.Row
    
    data = db.cursor()
    data.execute("select * from std")
    
    rows = data.fetchall()
    return render_template("StudentManagement_Data.html", rows = rows)

if __name__ == '__main__':
    app.run(host='localhost',port=80,debug=True)