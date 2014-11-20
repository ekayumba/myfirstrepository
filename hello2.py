#! /usr/bin/env python
# --*-- coding: utf-8 --*--


from flask import Flask, request, make_response, redirect
app = Flask(__name__)


@app.route('/')
def give_browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/response')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response  


@app.route ('/kigali')
def func():
    response = make_response('<h1>I am in capital of Rwanda!</h1>')
    return response 

@app.route('/user/<name>')
def user(name):
    response = make_response('<h1>Hello, %s!</h1>' % name)
    return response
   

@app.route ('/facebook')
def goto_facebook():
    return redirect('http://www.facebook.com')


if __name__ == '__main__':
    app.run(debug=True)
