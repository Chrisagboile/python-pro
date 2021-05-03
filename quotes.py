from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import os
import re


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:P@ssword@localhost/quotes'

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://sjohrchjwnrhul:853d898d66e27ed61b11cf845c722e7fc4b7540468b1593d8057924e577caa42@ec2-34-252-251-16.eu-west-1.compute.amazonaws.com:5432/dadu8ik5h0luju'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#uri = os.getenv("DATABASE_URL")  # or other relevant config var
#if uri.startswith("postgres://"):
#    uri = uri.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy(app)

class favquotes(db.Model):
    __tablename__ = 'favquotes'

    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    fruits = ["apple","grape"," beries","oranges"]
    return render_template('index.html',quote='Kindness needs no translation',fruits=fruits)

@app.route('/about')
def about():
    return render_template('about.html',quote='Kindness needs no translation')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/default')
def default():
    result = favquotes.query.all()
    return render_template('default.html',result=result)

@app.route('/process',methods =['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata =favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('default'))
