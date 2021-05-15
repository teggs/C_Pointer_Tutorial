from selenium import webdriver
import random
import time



driver = webdriver.Chrome()

host = "127.0.0.1"
port = 5000
flask_url = "http://"+str(host)+":"+str(port)+"/login?next=%2F"

random_alpha = ['a','b','c','d','e','f','g','h','i','j']
alpha_list = []
for i in range(10):
    alpha_list.append(random.choice(random_alpha))
gpw = "".join(alpha_list)

user_user = str(gpw)+str(gpw)
email_email = str(gpw)+"@"+str(gpw)+".com"

password_password = '00000123'
confirmed_password = '00000123'

#go to register manager page
driver.get(flask_url)

#click sign
click_signup = driver.find_element_by_id('signup')
click_signup.click()
time.sleep(0.5)

def user_name():
    #user_name
    user_name = driver.find_element_by_id('username')
    user_name.send_keys(user_user)
    time.sleep(0.5)
user_name()

#mail
email = driver.find_element_by_id('email')
email.send_keys(email_email)
time.sleep(0.5)

def password():
    #password
    password = driver.find_element_by_id('password')
    password.send_keys(password_password)
    time.sleep(0.5)
password()

#confirmed
confirm = driver.find_element_by_id('confirm')
confirm.send_keys(confirmed_password)
time.sleep(0.5)

def submit():
    #submit
    submit = driver.find_element_by_id('submit')
    submit.click()
    time.sleep(0.5)
submit()

user_name()
password()
submit()

# submit
submit = driver.find_element_by_id('learning')
submit.click()
time.sleep(1.5)

# submit
submit = driver.find_element_by_id('back')
submit.click()
time.sleep(1)

# submit
submit = driver.find_element_by_id('assessing')
submit.click()
time.sleep(1.5)

#assessing pqge
choice_list = ['A','B','C','D']
def choose_answer(answer):
    choose_answer = driver.find_element_by_id(str(answer))
    choose_answer.click()
    time.sleep(0.3)
    next = driver.find_element_by_id('next')
    next.click()
    time.sleep(0.5)

for i in range(10):
    answer = random.choices(choice_list)[0]
    print(answer)
    choose_answer(answer)

#get the assessment
submit = driver.find_element_by_id('submit')
submit.click()
time.sleep(1.5)

#driver.close()
















