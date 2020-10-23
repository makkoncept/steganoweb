import os

from flask import Flask
from dotenv import load_dotenv, find_dotenv

from config import Config


load_dotenv(find_dotenv())

app = Flask(__name__)
app.config.from_object(Config)


from app import routes
