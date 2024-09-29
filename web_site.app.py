
import os
import re
import sqlite3
from datetime import datetime
from operator import index

from flask import Flask
from flask import flash
from flask import render_template
from flask import request
from flask import session

template_dir = os.path.abspath("./templates")
app = Flask(__name__, template_folder=template_dir)
DATABASE = 'database.db'
app.secret_key = os.urandom(12)


@app.route('/')
@app.route('/index.html')
def home():
    """defines home page"""
    now = datetime.now()  # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    if not session.get('logged_in'):
        return render_template('login.html',
                               session=session.get("logged_in"))
    else:
        return render_template('index.html', date_time=date_time)


@app.route('/page2.html')
def page2():
    """defines second page"""
    now = datetime.now()  # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    if not session.get('logged_in'):
        return render_template('login.html',
                               session=session.get("logged_in"))
    else:
        return render_template('page2.html', date_time=date_time)


@app.route('/page3.html')
def page3():
    """"defines third page"""
    now = datetime.now()  # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    if not session.get('logged_in'):
        return render_template('login.html',
                               session=session.get("logged_in"))
    else:
        return render_template('page3.html', date_time=date_time)


@app.route('/register')
def register():
    """requests user to register"""
    if not session.get('logged_in'):
        return render_template('register.html',
                               session=session.get("logged_in"))
    else:
        return logout()


@app.route('/register', methods=['POST'])
def register_user():
    """Use our password check function to validate password
        If password returned by our function is dictionary not boolean
        then it has errors, in that case"""
    if not isinstance(password_check(request.form['password']), bool):
        # Get the error dictionary
        error_dict = password_check(request.form['password'])
        # Flash appropriate message for each error
        if error_dict['length_error']:
            flash("Length of the password must be 12", category='error')
        if error_dict["digit_error"]:
            flash("Password should contain at least one number", category='error')
        if error_dict['uppercase_error']:
            flash("Password should contain at least one uppercase letter", category='error')
        if error_dict['lowercase_error']:
            flash("Password should contain at least one lowercase letter", category='error')
        if error_dict['symbol_error']:
            flash("Password should contain at least one special character", category='error')
        return register()
    elif register_user(request.form['username'], request.form['password']):
        return index('index.html')
    else:
        flash('email exists!')
        return index('index.html')


@app.route('/login', methods=['POST'])
def login_user():
    """if request.form['password'] == 'password' and request.form['username'] == 'admin':"""
    if check_user(request.form['username'], request.form['password']):
        session['logged_in'] = True
        session['email'] = request.form['username']
    else:
        flash('wrong email/password!')
    return index('index.html')


@app.route("/change_password")
def change_password():
    """allows user to change password"""
    if not session.get('logged_in'):
        return index('index.html')
    else:
        return render_template('change_password.html')


@app.route("/change_password", methods=['POST'])
def change_pword():
    """allows user to change password"""
    print(session.get("email"))
    if not isinstance(password_check(request.form['password']), bool):
        # Get the error dictionary
        error_dict = password_check(request.form['password'])
        # Flash appropriate message for each error
        if error_dict['length_error']:
            flash("Length of the password must be 12", category='error')
        if error_dict["digit_error"]:
            flash("Password should contain at least one number", category='error')
        if error_dict['uppercase_error']:
            flash("Password should contain at least one uppercase letter", category='error')
        if error_dict['lowercase_error']:
            flash("Password should contain at least one lowercase letter", category='error')
        if error_dict['symbol_error']:
            flash("Password should contain at least one special character", category='error')
        return change_pword()
    elif update_password(session.get("email"), request.form['password']):
        return index('index.html')
    else:
        flash('An error occurred')
        return index('index.html')


@app.route("/logout")
def logout():
    """allows user to logout"""
    session['logged_in'] = False
    return index('index.html')


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect("database.db")
        print(sqlite3.version)
        return conn
    except sqlite3.Error as e:
        print(e)


def register_user(email, password):
    script = "insert into userdata values(?,?)"
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute(script, [email, password])
        conn.commit()
        print("Added")
        return True
    except:
        print('Email exists')
        return False


def check_user(email, password):
    """allows user to check email and password"""
    script = "select * from userdata where email=? and password = ?"
    conn = create_connection()
    c = conn.cursor()
    conn.row_factory = sqlite3.Row
    c.execute(script, [email, password])
    print("Checking")
    if c.fetchone():
        print("Exists")
        return True
    else:
        return False


def update_password(email, password):
    """allows user to register email and password"""
    script = "insert into userdata values(?,?)"
    conn = create_connection()
    c = conn.cursor()
    c.execute(script, [password, email])
    conn.commit()
    print("Added")
    return True


def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 12

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ @!#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

    # overall result
    password_ok = not (length_error or digit_error or uppercase_error
                       or lowercase_error or symbol_error)
    # If password is in right form return true
    if password_ok:
        return True
    # else return a dictionary telling what kind of error the password has
    else:
        return {
            'password_ok': password_ok,
            'length_error': length_error,
            'digit_error': digit_error,
            'uppercase_error': uppercase_error,
            'lowercase_error': lowercase_error,
            'symbol_error': symbol_error,
        }


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5000, passthrough_errors=False)
