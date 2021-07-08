"""Main App"""

from flask import Flask
from flask_cors import CORS
from app.controller import api

app = Flask(__name__)
CORS(app)

api.init_app(app)

