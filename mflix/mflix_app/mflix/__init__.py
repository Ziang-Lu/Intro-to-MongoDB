from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mflix-app-mongodb'
# Override the configuration values from the configuration file, which is
# pointed by "MFLIX_SETTINGS" environment variable
app.config.from_envvar('MFLIX_SETTINGS', silent=True)

# Initialize the LoginManager object with the newly create application
login_manager = LoginManager(app)

from .auth import *
from .mflix import *
