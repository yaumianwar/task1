#!/usr/bin/python

from flask import Flask, render_template
from db import database
from models import PersonalInformation
from models import BlogList


app = Flask(__name__)
app.config.from_object('config')
database.init_app(app)

@app.route("/")
def homepage():
	personal_information = PersonalInformation.query.filter_by(id=1).first()
	return render_template("index.html",  **locals())

@app.route("/blog")
def listblog():
	listblog = BlogList.query.all()
	return render_template("work.html",  **locals())


if __name__=="__main__":
	app.run(debug=True)