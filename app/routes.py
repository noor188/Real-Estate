from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm, PropertyForm, HouseForm, ApartmentForm, PropertyListing

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
      if form.type.data == 'apartment':
           return redirect(url_for('apartment'))

      flash('Add property')
      return redirect(url_for('index'))
   return render_template('property.html', form = form)

@app.route("/house", methods=['GET', 'POST'])
def house():
   form = HouseForm()
   if form.validate_on_submit():
       flash('Add House')
       return redirect(url_for('index'))
   return render_template('house.html', form= form)

@app.route("/apartment", methods=['GET', 'POST'])
def apartment():
   form = ApartmentForm()
   if form.validate_on_submit():
       flash('Add Apartment')
       return redirect(url_for('index'))
   return render_template('apartment.html', form=form)

@app.route('/propertylisting', methods=['POST', 'GET'])
def property_listing():
   form = PropertyListing()
   if form.validate_on_submit():
        flash("updated status")
   return render_template('property_listing.html', form= form)
        
       
   