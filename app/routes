from flask import render_template,flash
from app import app

from forms import signupForm
from forms import loginForm
from modelss import User

@app.route('/')
def index():
    return render_template('welcome_page.html', title ="C-pointer tutorial")

@app.route('/signup',methods = ['GET','POST'])

def signup():

    sf = signupForm()
    if sf.validate_on_submit():
        username = sf.username.data
        email = sf.email.data
        password = sf.password.data
        user = User(username = username, email = email, password = password)
        print(username,email,password)
        #db.session.add(user)
        #db.session.commit()
        flash('Congrats, registeration success', category = 'success')
    return render_template('signup.html', form = sf)


    #error = None
    #if request.method == 'POST':
    #    if request.form['username'] != 'tomsmoker' or request.form['password'] != 'hunter2':
    #        error = "Pls check the password"
    #    else:
    #        return redirect(url_for('signup'))
    #return render_template('signup.html', error = error)

@app.route('/login',methods = ['GET','POST'])
def login():
    lf = loginForm()
    if lf.validate_on_submit():
        username = lf.username.data
        password = lf.password.data
        print(username, password)
        pass
    return render_template('login.html', form = lf)
    #error = None
    #if request.method == 'POST':
    #    if request.form['username'] != 'tomsmoker' or request.form['password'] != 'hunter2':
    #        error = "Username or Password may wrong?"
    #    else:
    #        return redirect(url_for('login'))
    #return render_template('login.html', error = error)
