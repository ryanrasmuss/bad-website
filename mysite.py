#!/bin/python3

from flask import Flask, url_for, render_template, request, redirect, flash, send_from_directory
#from flask_login import LoginManager
from werkzeug.utils import secure_filename
from datetime import datetime
import subprocess as subp
import os

from Database import Insert_New_User as INU
from Database import Username_Exists
from Database import Verify_Login
from Policies import GOOD
from Logging import *

UPLOAD_FOLDER = '/mysite/files/'
ALLOWED_EXT = set(['txt', 'pdf', 'png', 'iso', 'jpg', 'jpeg', 'gif', 'exe', 'c'])

app = Flask(__name__)
app.secret_key = 'n0tprod'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#login_manager = LoginManager()

#@login_manager.user_loader
#def load_user(user_id):
#    return User.get(user_id)

# Download files landing page

@app.route('/download/<filename>', methods=('GET', 'POST'))
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# General Files page (after successful login)

@app.route('/files', methods=('GET', 'POST'))
def files():

    nofiles = False

    try:
        files = subp.check_output(["ls -p files/ | grep -v /"], shell=True).decode("ascii")
    except subp.CalledProcessError as e:
        nofiles = True
        
    if nofiles:
        files = list()
    else:
        # files := \nl separated string
        # convert into list
        files = list(filter(None,files.split('\n')))
    
    print (files)
    return render_template('files.html', files=files)

# Dedicated Upload Page

@app.route('/upload', methods=('GET', 'POST'))
def upload():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file content')
            return redirect(request.url)

        ffile = request.files['file']

        if ffile.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if ffile:
            filename = secure_filename(ffile.filename)
            ffile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('download', filename=filename))
            flash('File has been uploaded successfully')
            return redirect(url_for('upload'))
    return render_template('upload.html')

# XXX: This page would require login, so would files, upload, download
@app.route('/landing', methods=['GET', 'POST'])
def landing():
    return render_template('landing.html')

# LANDING PAGE '/' 'index.html'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# LOGIN PAGE '/' 'login.html' redirects: index.html, register, self, files


def logout():

    session.pop('username', None)
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        print ("clicked submit")
        username = request.form["username"]
        password = request.form["password"]

        if Username_Exists(username) is True:
            if Verify_Login(username, password):
                print ("Logged in!")
                flash('Welcome')
                # XXX: store session
                # login_user(username)
                # XXX: redirect to files landing page if successful
                # XXX: create session
                # session['username'] = username
                return redirect(url_for('landing'))
            else:
                print ("Incorrect creds! gtfo")
                flash("Creds are incorrect, sorry please leave.")
                # Return to login page
                return redirect(url_for('login'))
            #print ("Username does exit, BUT FETCHING PW IS NOT IMPLEMENTED YET")
        else:
            print ("Username does not exist")
            flash("Creds are incorrect, sorry please leave.")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        print ("clicked submit")
        username = request.form['username'].encode('utf-8')
        password = request.form['password'].encode('utf-8')
        print (username, "of type", type(username))
        print (password, "of type", type(password))

        INU_ret = INU(username, password)
        if INU_ret is not GOOD:
            print (INU_ret, "is not good")
            logit("incorrect register attempt")
            return render_template('register.html')

        # XXX: need to return an alert and clear forms

        print ("Inserted new username and password successfully")
        logit("successfully registered new user")
        flash('Registration successful')
        return redirect(url_for('login'))
        #return render_template('index.html')

    return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = 'slyther1n'
    #login_manager.init_app(app)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', port=5000, debug=True)
