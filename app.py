from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///countydata.db'
db = SQLAlchemy(app)
from flask import request, jsonify
    
from controllers import *    



