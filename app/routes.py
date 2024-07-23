from flask import render_template, redirect, flash
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

@app.route("/login", )
def login():
   form = LoginForm()

   if form.validate_on_submit():  
      flash('Login requested for user {}, remember_me{}'.format(form.username.data, form.remember_me.data))     
      return redirect('/index')      
   return render_template("login.html",title="Sign In", form= form)