from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm, PropertyForm

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

@app.route("/login", methods=["GET", "POST"])
def login():
      form = LoginForm()
      if form.validate_on_submit():
         flash('Login requested for user {}, remember_me={}'.format(
               form.username.data, form.remember_me.data))
         return redirect(url_for('index'))
      return render_template('login.html', title='Sign In', form=form)

@app.route("/property", methods=['GET', 'POST'])
def property():
   form = PropertyForm()
   if form.validate_on_submit():
       if form.type.data == 'house':
           return redirect(url_for('house'))
       flash('Add property')
       return redirect('/index')
   return render_template('property.html', form = form)

@app.route('/house', methods=["POST", "GET"])
def house():
    return render_template('house')