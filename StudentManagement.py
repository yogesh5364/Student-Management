from flask import Flask,redirect, render_template,url_for,request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("StudentManagement_Home.html")

@app.route('/AddStudent', methods=['POST','GET'])
def AddStudent():
    if request.method == 'POST':
        try:
            Sid = request.form['s']
            Name = request.form['n']
            Age = request.form['a']
            Email = request.form['e']
            PhoneNo = request.form['p']
            Address = request.form['ad']
            Course = request.form['c']
         
            db = sql.connect("std.db")
            data = db.cursor()
            #data.execute('create table std(Sid int primary key not null, Name varchar(20) not null, Age int, Email varchar(20), PhoneNo varchar(15), Address varchar(50) not null, Course varchar(20) not null)')
            data.execute(f'''insert into std values({Sid},'{Name}',{Age},'{Email}','{PhoneNo}','{Address}','{Course}')''')
            db.commit()
            print("You Have Successfully Added...!!!")

        except:
            db.rollback()
            print("Error")
    
        finally:
            return render_template("StudentManagement_Add.html")
            db.close()

    return render_template("StudentManagement_Add.html")

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
        
        Name = request.form['n']
        data.execute(f"SELECT * FROM std WHERE Name = '{Name}'")
        
        rows = data.fetchall()
        print("You Have Successfully Finded...!!!")
        return render_template("StudentManagement_Find.html", rows = rows)

    return render_template("StudentManagement_Find.html")

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

@app.route('/RemoveStudent/ByEmail', methods=['POST','GET'])
def RemoveStudentByEmail():
    if request.method == 'POST':
        db = sql.connect("std.db")
        data = db.cursor()

        Email = request.form['e']
        data.execute(f"DELETE FROM std where Email = '{Email}'")
        db.commit()
        print("You Have Successfully Removed...!!!")

    return render_template("StudentManagement_Remove.html")

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