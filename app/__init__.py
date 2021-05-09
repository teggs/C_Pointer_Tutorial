from flask import Flask, render_template, flash,request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config.from_object(Config)

from app.routes import *
