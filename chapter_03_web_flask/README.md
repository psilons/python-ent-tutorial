# Flask Web Application Container

[Flask](https://pypi.org/project/Flask/) is a lightweight web app container. 
It delegates HTTP requests through [Werkzeug](https://palletsprojects.com/p/werkzeug/)
to our code and use [Jinja2](https://pypi.org/project/Jinja2/) as response template.

We can run Flask for development and wrap it in a [WSGI](https://wsgi.readthedocs.io/en/latest/) 
server, such as
[gunicorn](https://gunicorn.org/)
or [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) 
for production(to handle multithreading).

Tornado is simple, but need more knowledge for multi-threading.
Django has relatively higher learning curve. 
Other web servers can be found [here](https://steelkiwi.com/blog/top-10-python-web-frameworks-to-learn/),
and [here](https://scoutapm.com/blog/the-most-popular-python-web-frameworks-in-2020),
such as CherryPy and FastAPI.

Document: 
- https://flask.palletsprojects.com/en/1.1.x/

Tutorials:
- https://hackersandslackers.com/your-first-flask-application/
- https://www.tutorialspoint.com/flask/index.htm
- https://www.javatpoint.com/flask-tutorial
- https://flask.palletsprojects.com/en/1.1.x/tutorial/
- https://exploreflask.com/en/latest/views.html

Books:
- Flask Web Development, 2E

## HTTP Basics

[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) is part of the core 
internet foundation as the ommunication protocol. 

Here are the common aspects that we have on a daily bases:
- request methods, such as GET, POST
- request parameters and encoding
- request headers

Here are some tutorials:
- https://developer.mozilla.org/en-US/docs/Web/HTTP
- https://www.tutorialspoint.com/http/index.htm
- https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html

## HTML

[HTML](https://html.spec.whatwg.org/) is the document format in the WWW world, 
[wiki](https://en.wikipedia.org/wiki/HTML). It's GUI description language.

Here are some tutorials:
- https://www.w3schools.com/html/
- https://developer.mozilla.org/en-US/docs/Web/HTML

Most modern web sites are using [javascript](https://en.wikipedia.org/wiki/JavaScript)
to generate HTML DOM tree. Popular javascript frameworks include
[Vue.js](https://vuejs.org/), [React.js](https://reactjs.org/), and 
[Angular.js](https://angularjs.org/). Others are mentioned 
[here](https://www.lambdatest.com/blog/best-javascript-framework-2020/)

[CSS](https://en.wikipedia.org/wiki/CSS) is used for decoration styles.

Javascript and CSS are separate topics.

## Flask Application Setup
We need to map url resources to one of the following:
- static files: css, javascript, images, etc.
- dynamic templates.
- Python code for request handling and dynamic content generating.

![web_structure](docs/web_structure.png)

It's not a good idea to leave the Python code in the url accessible
folder. Generally, we put static files on a web server, such as Nginx,
and put templates and Python code on the Flask server behind the
web server. To avoid confusion, we call Nginx web server and Flask
web app server, or simply app server.

When we start the Flask server in dev, we have to start from the
web root folder in order to serve static content.

Here is the setup in the Python code(src/flask_test_app/web_main.py):

```
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', root_path='.', static_folder="static")

@app.route('/')  
def root():
    return "Hello, world"
    
# start web app
if __name__ == '__main__':
    app.run(debug=True)
```

We specify the root folder and others in the app object.

The default port is 5000, we may change that with
```port=8888``` in the ```app.run()```

## URL routing
URLs are the interface for user to submit requests. They are routed by Flask
to our handler logic via annotation @app.route() like the above.

src/flask_test_app/web_main.py lists several ways to deal with requests:
- Using template with dynamic data (/hello)
- Using template with dynamic structure (/pokemon/<<int:num>>)
- GET/POST methods ()
- HTML form (/length)
- parameters in url (/pokemon/<<int:num>>)

src/flask_test_app/web_handlers.py shows
- streaming data
- file upload

Generally, we put handler logic in separate files for better code
structure. In the file src/flask_test_app/web_handlers.py, 

```
from flask import Response, stream_with_context, Blueprint

stream_urls = Blueprint('url', __name__, static_folder="static", template_folder='templates')

```

Then we can include all handler method with @app.route in this file
to the web_main.py:

```
import flask_test_app.web_handlers as web_handlers
app.register_blueprint(web_handlers.stream_urls)
```

HTTP redirect is discussed 
[here](https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask),
[here](https://stackoverflow.com/questions/54690994/how-to-send-post-request-using-flask-redirect),
[here](https://stackoverflow.com/questions/15473626/make-a-post-request-while-redirecting-in-flask/15480983#15480983),
and [here](https://softwareengineering.stackexchange.com/questions/99894/why-doesnt-http-have-post-redirect).
However, these discussions suggest that we should redirect POST, though
technically we can do so by set code to 307 in the redirect method.

Basically, we can redirect requests like this:

```
flask.redirect(flask.url_for('operation', new_param=value, **request.args))
```

Redirect does not carry request parameters, so we have to do it manually.
This is because the redirect request is a new request. Clients can see the
url change because the redirect response reaches clients.

[Difference](http://www.differencebetween.net/technology/difference-between-forward-and-redirect/)

Redirect is useful in several cases, e.g., when a user hits a page where login
is required we can redirect the user to the login page.

Redirect tells browser to initiate a new request to the new url.

In Java, there is also a url forward but seems Flask does not have it.
See [here](https://www.baeldung.com/servlet-redirect-forward),
[here](http://www.differencebetween.net/technology/difference-between-forward-and-redirect/),
[flask-http-forwarding](https://github.com/casetext/flask-http-forwarding),
and [Flask-Forward](https://pythonhosted.org/Flask-Forward/).

Flask has a message flashing
- https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
- https://cs.wellesley.edu/~cs304/lectures/flask/activities-3.html

## Error handling:  
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling
https://pythonprogramming.net/flask-error-handling-basics/
https://code-maven.com/python-flask-catch-exception
@app.errorhandler(Exception)
https://stackoverflow.com/questions/60324360/what-is-best-practice-for-flask-error-handling

## HTTP Sessions and Cookies

https://www.javatpoint.com/flask-session
https://www.valentinog.com/blog/cookies/
session/authentication
https://blog.paradoxis.nl/defeating-flasks-session-management-65706ba9d3ce

client side session makes server stateless but not safe.
app['SECRET_KEY] encrypts data in cookie, but cookies
can be stolen.

server side session
flask-session - abandoned?
https://pythonhosted.org/Flask-KVSession/
https://hackersandslackers.com/managing-user-session-variables-with-flask-sessions-and-redis/
use a distributed cache to make server stateless.
https://gist.github.com/wushaobo/52be20bc801243dddf52a8be4c13179a

https://stackoverflow.com/questions/43304363/simple-server-side-flask-session-variable/47459571
shopping cart

ttps://testdriven.io/courses/learn-flask/sessions/

https://testdriven.io/courses/learn-flask/sessions/

## WSGI Integration

## Testing
https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_client

## HTML to PDF
https://pythonpedia.com/en/knowledge-base/28165704/convert-html-to-pdf-using-python-flask









