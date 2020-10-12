import os

from flask import Flask
from dotenv import load_dotenv, find_dotenv

from config import Config


load_dotenv(find_dotenv())

app = Flask(__name__)
app.config.from_object(Config)

DEFAULT_FILE_PATH = os.path.join(app.root_path, "static/images", "default.png")

from app import routes
