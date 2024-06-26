from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    '''View function for the inde web page'''
    user = {'username': 'Noor'}
    return render_template("index.html", title= "Microblog", user= user)
