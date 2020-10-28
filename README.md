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

- When you open the app you'll see the main page with a Contact Form at the end ('/')
- The contact form submits to a csv file for test purposes 
- By completing the form you'll be redirected to the same page with a success message ('/form')
- If you want to see the entered values, navigate to '/datos'. A table with the loaded data will appear. 
