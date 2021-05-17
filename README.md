Start the Falsk app
Start the flask app, with the code "export FLASK_APP = app.py" in the terminal command line.
First of all, create a virtual environment and install all the required open source with the requirement.txt.
The default port for the Flask is 5000. If the port used by other apps, please check with the command "lsof -i 5000", then close the listener with the command "kill -9 $PortID".
Or, another method is to set the port and the host for the flask app.

Using selenium to test the app
In the app fold, use python IDE to open the test2.py, set the host and the local variable before running the test, and the default host is "127.0.0.1", the default port is 5000.
In addition, the selenium testing code is written for the chrome web driver. Please put the web driver into the root directory, and ensure the version of the web driver is matching 
your chrome web application

Reigseter and login to the C pointer tutorial flask app （the registration/login page）
In the login page, input a username, an email address, a password and a confirmed password. The flask wtf form validator will check the input format. Please input the valid information, 
or the validator will reject the user registration request. After successful register, then input the user name and the password to login to the app. If you forget the password or the 
username, please register again.

The study platform
After success in login into the app, there are three options. 
The introduction of the C pointer part tells the motivation of the app to establish.(the page promoting the theme and purpose to users)
The teaching part includes several videos because the video tutor has a good knowledge of the C-pointers.(the learning page)
The assessment part helps the user to check the progress of the learning. (the page for assessment)

The design of the assessment
There are 3 main areas in this page. They are used for presenting exercise, choices and hints, respectively.
When this page was initialized, 10 random numbers were generated. Then 10 exercises will be selected from the database based on the random numbers.
Users can make choices and their choices will be recorded. Unless they click the 'submit' button, the 10 execrises will not be refreshed.
When the user finished all the 10 exercise and click 'submit' button, they will be led to the result page.

The assessment result (the page presesnting feedback, aggregate results and usage statsitics)
After finish the testing, the app returns a comment on the user's performance. The bar plot evaluates the user's performance and compares it with the other users' performance. 
The natural language template assists the user to understand the bar plot and the understanding level of the C pointer.