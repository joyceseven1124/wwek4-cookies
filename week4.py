# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:05:49 2022

@author: 劉佳怡
"""

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import make_response


app = Flask(__name__,static_folder="static" ,static_url_path = "/static")


@app.route("/")
def form():
    state = request.cookies.get('state')
    if state == "logged in":
        return redirect("/member")
    else:
        resp = make_response(render_template("home.html"))
        resp.set_cookie(key='state', value='not logged in')
        return resp

   
@app.route("/signin",methods=["POST"])
def signin():
    input_account = request.form["account"]
    input_password = request.form["password"]
    if input_account == 'test' and input_password == 'test':
        resp = make_response(redirect("/member"))
        resp.set_cookie(key='state', value='logged in')
        return resp
    elif input_account == '' or input_password == '':
        return redirect("/error?message=empty")
    else:
        return redirect("/error")


@app.route("/square/<number>")
def square(number):
    total = int(number)*int(number)
    return render_template("calculate.html", result = total )
    
@app.route("/member")
def success():
    state = request.cookies.get('state')
    if state == "logged in" :
        return render_template("success.html")
    else:
        return redirect("/")
   
    
@app.route("/error")
def fail():
    message = request.args.get("message",None)
    if message == "empty":  
        return render_template("fail.html",message="請輸入帳號、密碼")
    else:
        return render_template("fail.html",message="帳號、或密碼輸入錯誤")
    
@app.route("/signout")
def signout():
    resp = make_response(redirect("/"))
    resp.set_cookie(key='state', value='not logged in')
    return resp

app.run(port=3000)