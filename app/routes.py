from flask import render_template
from app import app
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    '''View function for the inde web page'''
    user  = {'username': 'Noor'}
    posts = [{
                'author': {'username': 'Noor'},
                'post'  : 'an apartment for sell'
             },
             {
                'author': {'username': 'Sarah'},
                'post'  : 'a house for sell'                 
             }]
    return render_template("index.html", title= " Welcome Microblog", user= user, posts=posts)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html",title="Sign In", form= form)