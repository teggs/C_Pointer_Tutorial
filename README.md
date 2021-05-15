# C_Pointer_Tutorial

<p>Flask_project is the root directory<br>
  APP fold has to under the Flask_project folder, and templates has to under App folder.</p>
  
    a full readme.md, describing the design and development of the application, and giving instructions on how to launch from local host.
  <h3> Start the Falsk app</h3>
  Start the flask app, with the code "export FLASK_APP = app.py" in the terminal command line.<br>
  First of all, create a virtual environment and install all the required open source with the requirement.txt. <br>
  The default port for the Flask is 5000. If the port used by the another app, please check with the command "lsof -i 5000", the close the listener with the command
  "kill -9 $PortID".<br>
  Or, another method is set the port and the host for the flask app.<br>
  
   <h3>Using selenium to test the app /h3>
   <p>In the app fold, use python IDE to open the test2.py, the set the host and the local variable before run the test, the default host is "127.0.0.1" and the default port is 5000.<br>
   In addition, the selenium testing code is write for chrome webdriverm, please put the webdriver in to the root directory, and ensure the version of the webdriver is matching your chrome web application</p>
  
  <h3> Reigseter and login to the  C pointer tutorial flask app</h3>
  <p> In the login page, input a username, a email address, a password and a confirmed password. The flask wtf form validator will check the input format, please input the valid information, or the register request will be rejected.
  After successful register, then input the user name and the password to login to the app. If you forget the password or the username, please register again.
  
  <h3>The study platform</h3>
  
  
  
  
  
  
  
  

