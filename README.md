# C_Pointer_Tutorial

<p>Flask_project is the root directory<br>
  APP fold has to under the Flask_project folder, and templates has to under App folder.</p>
  
    a full readme.md, describing the design and development of the application, and giving instructions on how to launch from local host.
# C_Pointer_Tutorial

<p>Flask_project is the root directory<br>
  APP fold has to under the Flask_project folder, and templates have to under the App folder.</p>
  
    A full readme.md, describing the design and development of the application and giving instructions on how to launch from local host.
  <h3> Start the Falsk app</h3>
  Start the flask app, with the code "export FLASK_APP = app.py" in the terminal command line.<br>
  First of all, create a virtual environment and install all the required open source with the requirement.txt. <br>
  The default port for the Flask is 5000. If the port used by other apps, please check with the command "lsof -i 5000", then close the listener with the command
  "kill -9 $PortID".<br>
  Or, another method is to set the port and the host for the flask app.<br>
  
   <h3>Using selenium to test the app /h3>
   <p>In the app fold, use python IDE to open the test2.py, set the host and the local variable before running the test, and the default host is "127.0.0.1", the default port is 5000.<br>
   In addition, the selenium testing code is written for the chrome web driver. Please put the web driver into the root directory, and ensure the version of the web driver is matching your chrome web application</p>
  
  <h3> Reigseter and login to the  C pointer tutorial flask app</h3>
  <p> In the login page, input a username, an email address, a password and a confirmed password. The flask wtf form validator will check the input format. Please input the valid information, or the validator will reject the user registration request.
  After successful register, then input the user name and the password to login to the app. If you forget the password or the username, please register again.
  
  <h3>The study platform</h3>
  After success in login into the app, there are three options. The introduction of the C pointer part tells the motivation of the app to establish. The teaching part includes several videos because the video tutor has a good knowledge of the C-pointers. And an assessment part helps the user to check the progress of the learning.
  
  <h3>The design of the assessment</h3>
  
  
  <h3> The assessment result</h3>
 After finish the testing, the app returns a comment on the user's performance. The bar plot evaluates the user's performance and compares it with the other users' performance.
 The natural language template assists the user to understand the bar plot and the understanding level of the C pointer.
  
  
  
  
  
  
  
  

