from flask import render_template,flash,redirect,url_for,request
from app import app,db
from flask_login import login_user, login_required, current_user,logout_user
from app.forms import signupForm
from app.forms import loginForm
from app.modelss import User
import numpy as np

#@socketio.on('connect', namespace='/')
@app.route('/')
@login_required
def index():
    return render_template('base.html', title ="C-pointer tutorial")

@app.route('/signup',methods = ['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return render_template('studyP.html')
    sf = signupForm()
    if sf.validate_on_submit():
        username = sf.username.data
        email = sf.email.data
        password = sf.password.data
        user = User(username = username, email = email, password = password, save_the_answer="-1", question_index="-1", flag = 1)
        db.session.add(user)
        db.session.commit()
        flash('Congrats, registeration success', category = 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form = sf)

#@socketio.on('connect', namespace='/login')
@app.route('/login',methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return render_template('studyP.html')
    lf = loginForm()
    if lf.validate_on_submit():
        username = lf.username.data
        password = lf.password.data
        remember = lf.remember.data
        #check if password is matched
        user = User.query.filter_by(username = username).first()
        if user and user.password == password:
            #user exist and password matched
            login_user(user,remember = remember)
            flash('Login success', category='info')
            #print(user_name)
            return render_template('studyP.html')

        flash("User not exists or password not match", category = 'danger')
    return render_template('login.html', form = lf)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')

ground_truth = {'1':1,'2':0,'3':2,'4':1,'5':0,
                '6':3,'7':2,'8':1,'9':1,'10':3,
                '11':3,'12':1,'13':3,'14':1,'15':1,
                '16':1,'17':3,'18':1,'19':2,'20':1,
                '21':2,'22':3,'23':1,'24':2,'25':1,
                '26':1,'27':2,'28':2,'29':3,'30':3}

@app.route('/login/assessing',methods=["GET", "POST"])
def assess():
    if request.method == 'POST':
        user_answer = request.form['user_answer']

        # To front_end 2: question_index
        q_index = request.form['q_index'] #question index

        correct_answer = {}
        q_index_list = q_index.split(",")
        for i in range(len(q_index_list)):
            correct_answer[i] = correct_answer.get(i,ground_truth[q_index_list[i]]) #the answer for the question
        assert len(correct_answer) == 10

        answered_correctness = []
        user_answer_list = user_answer.split(",")

        for i in range(len(user_answer_list)):
            ans = int(user_answer_list[i])
            if ans == correct_answer[i]:
                answered_correctness.append(1) #if correct, record as 1
            elif ans == -1: # if not answer, then continues
                continue
            elif ans != correct_answer[i]:
                answered_correctness.append(0) #if incorrect, record as 0

        # To front_end 1: easy-medium-hard correctness
        emh_list = []
        emh_list.append(sum(answered_correctness[0:5]))
        emh_list.append(sum(answered_correctness[5:8]))
        emh_list.append(sum(answered_correctness[8:10]))

        #save the result for the next time
        username = current_user.username  #check the user
        user = User.query.filter_by(username=username).first()  # update the user information
        #To db 1: user_answer
        user.save_the_answer = user_answer
        #To db 2: question_index:q_index
        user.question_index = q_index
        # To db 4: correctness_count
        user.emh = str(emh_list)

        #user.flag = 1
        if request.form.get('action') == "submit":
            # To db 3: flag: submit{1} not submit{0}
            user.flag = 1
            db.session.commit()
            print("submit_success")

            all_users = User.query.all()

            total_easy_mark = []  # get the total mark for the user
            total_middle_mark = []
            total_hard_mark = []
            for i in range(len(all_users)):
                try:
                    marks_list = all_users[i].emh[1:-1].split(",")

                    total_easy_mark.append(int(marks_list[0]))

                    total_middle_mark.append(int(marks_list[1]))

                    total_hard_mark.append(int(marks_list[2]))

                except TypeError:
                    continue
            avg_easy_mark = round(sum(total_easy_mark) / len(all_users), 2)
            avg_medium_mark = round(sum(total_middle_mark) / len(all_users), 2)
            avg_hard_mark = round(sum(total_hard_mark) / len(all_users), 2)
            accuracy_rate = sum(answered_correctness) * 10

            adj1 = np.where(accuracy_rate >= 80, 'good', np.where(accuracy_rate >= 60, 'fair',
                                                                  np.where(accuracy_rate >= 40, 'not good',
                                                                           'poor')))

            e = int(all_users[i].emh[1:-1].split(",")[0])
            m = int(all_users[i].emh[1:-1].split(",")[1])
            h = int(all_users[i].emh[1:-1].split(",")[2])
            adj2 = np.where(e>= 4,'good', np.where(e == 3, 'fair',np.where(e == 2, 'not good','poor')))

            adj3 = np.where(m == 3, 'good', np.where(m == 2, 'fair',np.where(m >= 1, 'not good','poor')))

            adj4 = np.where(h == 2, 'good', np.where(h == 1, 'fair', 'poor'))

            print(str(adj1) + str(adj2) + str(adj3) + str(adj4))

            return render_template('assessment.html', adj1 = adj1, adj2 = adj2, adj3 = adj3, adj4= adj4,
                                   accuracy_rate = accuracy_rate, avg_easy_mark = avg_easy_mark,
                                   avg_hard_mark = avg_hard_mark, avg_medium_mark = avg_medium_mark,
                                   e_right =e, m_right = m, h_right = h)

        elif request.form.get('action') == "return":
            # To db 3: flag: submit{1} not submit{0}
            user.flag = 0
            db.session.commit()
            print("return_success")
            return redirect(url_for('login'))

    else:
        #save the result for the next time
        username = current_user.username  #check the user
        user = User.query.filter_by(username=username).first()  # update the user information
        #To front: user_answer
        user_answer = user.save_the_answer 
        #To front: question_index:q_index
        q_index = user.question_index 
        #To front: flag
        flag = user.flag 

        return render_template('answer_sheet.html',user_answer = user_answer, question_index = q_index, flag = flag)

@app.route('/login/assessment',methods=["GET", "POST"])
def assessment():
    return render_template('assessment.html')

@app.route('/login/learning',methods=["GET", "POST"])
def learning():
    return render_template('teaching_sheet.html')

@app.route('/login/introduction',methods=["GET", "POST"])
def promoting():
    return render_template('promoting_sheet.html')




