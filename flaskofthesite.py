from flask import Flask, render_template , request, redirect, url_for, session
from submissionform import trackingsystem
from loginform import Logindetails
import sqlite3
import os
import requests

#Eto automatic na pupunta sa database. para di na need copypaste directory
# Get the folder where THIS script lives
script_dir = os.path.dirname(os.path.abspath(__file__))

# Database folder inside the script folder
base_dir = os.path.join(script_dir, "Database")

# Create the folder (this will always succeed)
os.makedirs(base_dir, exist_ok=True)

db_path = os.path.join(base_dir, "users.db")
app=Flask(__name__)
app.secret_key="sikreto"



#════════════════════════════════════════════════════════════════════════════════════════════════════════#
#[LOGIN/LOGOUT/REGISTER SECTION (BEGINNING)]
#════════════════════════════════════════════════════════════════════════════════════════════════════════#

#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Login Page
@app.route('/logintab', methods = ['POST','GET'])
def logintab():
    Loginform = Logindetails()
    if request.method == "POST":
        #Captcha Line ------------------------------------------------------------x
        captcha = request.form.get('g-recaptcha-response')
        secret_key = "6Lfqpo0sAAAAAJa4rv0NjjL9JwuuXKPuNYiPBVm3"

        verify = requests.post(
                "https://www.google.com/recaptcha/api/siteverify",
                data={
                    "secret": secret_key,
                    "response": captcha}
            )
        result = verify.json()
        if not result.get("success"):
            return render_template('logintab.html', form=Loginform, error="Please verify the CAPTCHA")
        # Captcha line -------------------------------------------------------------END
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Login Details
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Admin login----------------------------------------------------------------------x
        if username == "admin" and password == "admin":
            session['user'] = username
            conn.close()
            return redirect('/dashboardAdmin')

        # Non-admin login ---------------------------------------------------------x
        c.execute("SELECT * FROM userlog WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['user'] = username
            return redirect('/dashboardProf')
        else:
            return render_template('logintab.html', form=Loginform, error="-- Invalid Username or Password --")
    else:
        return render_template('logintab.html', form=Loginform)
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
# Logout Line
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('logintab'))

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
# Registration Details
@app.route('/registrationtab', methods = ['POST','GET']) 
def registrationtab():
    registrationform = trackingsystem()
    if request.method=="POST":
        if(request.form['username'] !="" and request.form["password"] !="" and request.form["email"] !=""):
            username = request.form["username"]
            password = request.form["password"]
            email = request.form["email"]
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT * FROM userlog WHERE username=?", (username,))
            data = c.fetchall()
            if data:
                conn.close()
                return render_template('error.html')
            else:
                if not data:
                    c.execute("INSERT INTO userlog (username,password,email) VALUES (?,?,?)", (username,password,email))
                    conn.commit()
                    conn.close()
                    return redirect(url_for('logintab'))

    elif request.method=="GET":
        registrationform = trackingsystem()
        return render_template('registab.html', form=registrationform)
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#

#════════════════════════════════════════════════════════════════════════════════════════════════════════#
#[LOGIN/LOGOUT/REGISTER SECTION (END)]
#════════════════════════════════════════════════════════════════════════════════════════════════════════#




#════════════════════════════════════════════════════════════════════════════════════════════════════════#
#[ADMINISTRATOR SECTION(BEGINNING)]
#════════════════════════════════════════════════════════════════════════════════════════════════════════#

#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
# Dashboard for Administrators (With Protection)
@app.route('/dashboardAdmin')
def dashboardAdmin():
    if 'user' not in session:
        return redirect('/logintab')
    return render_template('dashboardAdmin.html', name=session['user'])
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
# Faculty List for Administrators
@app.route ('/facultylistAdmin')
def facultylistAdmin():
    db_path = os.path.join(base_dir, 'Facultylist.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row 

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM TEACHERS')

    rows = cursor.fetchall()
    for row in rows:
        print(row["Emp_ID"])

    return render_template('facultylistAdmin.html', rows=rows)
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
# Class Assignment for Adminstrators
@app.route('/classassignmentAdmin')
def assignmentAdmin():
    render_template('classassignmentAdmin.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#[Requirements for Administrators]
@app.route ('/requirementsAdmin')
def requirementsAdmin():
    db_path = os.path.join(base_dir, 'Facultylist.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row 

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM REQUIREMENTS')

    rows = cursor.fetchall()
    for row in rows:
        print(row["Requirement_ID"])

    return render_template('requirementsAdmin.html', rows=rows)
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Submission Monitoring
@app.route('/submissionmonitoringAdmin')
def submissionmonitoringAdmin():
    db_path = os.path.join(base_dir, 'facultylist.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM SUBMISSION')

    rows = cursor.fetchall()
    for row in rows:
        print(row["Submission_ID"])

    return render_template('submissionmonitoringAdmin.html', rows=rows)
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Profile for Administrators
@app.route('/profileAdmin')
def profileAdmin():
    render_template('profileAdmin.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#

#════════════════════════════════════════════════════════════════════════════════════════════════════════#
#[ADMINISTRATOR SECTION(END)]
#════════════════════════════════════════════════════════════════════════════════════════════════════════#





#════════════════════════════════════════════════════════════════════════════════════════════════════════#
#[PROFESSOR/NON-ADMIN SECTION(BEGINNING)]
#════════════════════════════════════════════════════════════════════════════════════════════════════════#

#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Dashboard for Professors
@app.route('/dashboardProf')
def dashboardProf():
    if 'user' not in session:
        return redirect('/logintab')
    return render_template('dashboardProf.html', name=session['user'])
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#My Classes for Professors
@app.route('/myClassesProf')
def myClassesProf():
    return render_template('myClassesProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#\


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Section 1 for Professors
@app.route('/section1Prof')
def section1Prof():
    return render_template('section1Prof.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Subject 1 for Professors
@app.route('/subject1Prof')
def subject1Prof():
    return render_template('subject1Prof.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Gradesheet for Professors
@app.route('/gradeSheetProf')
def gradeSheetProf():
    return render_template('gradeSheetProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Class Record for Professors
@app.route('/classRecordProf')
def classRecordProf():
    return render_template('classRecordProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Exam for Professors
@app.route('/examProf')
def examProf():
    return render_template('examProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Portfolio for Professors
@app.route('/portfolioProf')
def portfolioProf():
    return render_template('portfolioProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Major Exam for Professors
@app.route('/majorExamProf')
def majorExamProf():
    return render_template('majorExamProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Sample Quiz for Professors
@app.route('/sampleQuizProf')
def sampleQuizProf():
    return render_template('sampleQuizProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Finals for Professors
@app.route('/finalsProf')
def finalsProf():
    return render_template('finalsProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Sample Exam for Professors
@app.route('/sampleExamProf')
def sampleExamProf():
    return render_template('sampleExamProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Midterms for Professors
@app.route('/midtermsProf')
def midtermsProf():
    return render_template('midtermsProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
#Core Syllabus for Professors
@app.route('/coreSyllabusProf')
def coreSyllabusProf():
    return render_template('coreSyllabusProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#


#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#
# Profile for Professors
@app.route('/profileProf')
def profileProf():
    render_template('profileProf.html')
#⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺#

#════════════════════════════════════════════════════════════════════════════════════════════════════════#
#[NON-ADMIN/PROFESSOR SECTION (END)]
#════════════════════════════════════════════════════════════════════════════════════════════════════════#

def init_db():
    folder = base_dir
    os.makedirs(folder, exist_ok=True)
    db_path = os.path.join(folder, "users.db")
    print("Database path:", db_path)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS userlog(
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()     

if __name__ =="__main__":
    app.run(debug=True) 