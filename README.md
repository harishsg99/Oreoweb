# Oreoweb [![Join the chat at https://gitter.im/Oreoweb/community](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Oreoweb/community) ![test](https://forthebadge.com/images/badges/made-with-python.svg)

<p align="center">
    <img src="https://github.com/harishsg99/Oreoweb/blob/master/pic.jfif?raw=true">
</p>

Oreoweb is a Python Web Framework built for Developers to integrate scale AI powered web and API based applications.Oreoweb framework supports web development and API development with inbuilt Database and inbuilt deep learning library

It is a WSGI framework and can be used with any WSGI application server such as Gunicorn.


## Features

- WSGI compatible
- Basic and parameterized routing
- Class based handlers
- Test Client
- Support for templates
- Support for static files
- Custom exception handler
- Middleware
- Deep learning
- NoSQL DB
- AutoML(Coming Soon)

## Quick Start

Install it:

```bash
pip install oreoweb
```

Basic Usage:

```python
# app.py
from oreoweb import oreoweb

app = oreoweb()


@app.route("/")
def home(req, resp):
    resp.text = "Hello, this is a home page."


@app.route("/about")
def about_page(req, resp):
    resp.text = "Hello, this is an about page."


@app.route("/{age:d}")
def tell_age(req, resp, age):
    resp.text = f"Your age is {age}"


@app.route("/{name:l}")
class GreetingHandler:
    def get(self, req, resp, name):
        resp.text = f"Hello, {name}"


@app.route("/show/template")
def handler_with_template(req, resp):
    resp.html = app.template("example.html", context={"title": "Awesome Framework", "body": "welcome to the future!"})


@app.route("/json")
def json_handler(req, resp):
    resp.json = {"this": "is JSON"}


@app.route("/custom")
def custom_response(req, resp):
    resp.body = b'any other body'
    resp.content_type = "text/plain"
```

Start:

```bash
gunicorn app:app
```


