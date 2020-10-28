# RAPIfi-FlaskWebApp

_This is the landing page of a fictional Wifi company, RAPIfi. It uses Flask and Bootstrap Web app and has a dockerfile to run it_


## How to use 

* In the main directory run the following commands: 

```bash
 $ docker build -t rapifi-test .
 $ docker run --name rapifi-test -d -p 80:5000 rapifi-test
 ```

* You can see the app by entering to "localhost" through a web browser.

* You can stop the container by running:

```bash
$ docker stop rapifi-test 
```

## What will I find here?

🍄 When you open the app you'll see the main page with a Contact Form at the end ('/') <br>
🍄 The contact form submits to a csv file for test purposes <br>
🍄 By completing the form you'll be redirected to the same page with a success message ('/form') <br>

🍄 If you want to see the entered values, scroll to the end page and you'll find a link to the "employee login page" <br>
🍄 Complete the form:<br>
```
Username: admin
Password: admin
```
🍄 You'll be redirected to '/datos' 


### Testing

* Create Virtual Env:

```bash
$ pip install virtualenv
$ virtualenv flask
```
* Navigate to "flask" folder and activate

> $ source bin/activate 

* Install Flask

> $ python -m pip install flask

* Check if it was installed

> $ python -m pip list

* Run the application 

```bash
$ cd ..
$ cd app
$ python app.py
```
* Stop the environment

> $ deactivate
