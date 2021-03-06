## -*- coding: utf-8 -*-
## project/app/__init__.py

from flask import Flask, render_template, url_for, g, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_htmlmin import HTMLMIN
from flask_bcrypt import Bcrypt
from flask_sijax import Sijax
import os

# Set unicode encoding
import sys
if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf8')

# Setup Flask and read config from ConfigClass defined above
app = Flask(__name__)
app.config.from_object('config')

# Initialize Flask extensions
# Flask-SQLAlchemy
db = SQLAlchemy(app)

# Flask-mail
mail = Mail(app)

# HTML min
#HTMLMIN(app)

## Import models
from app.admin.models import *
from app.masterData.models import *
from app.task.models import *
from app.strategy.models import *
from app.project.models import *
from app.organization.models import *
from app.performance.models import *

# Flask-sijax
Sijax(app)

# Flask-bcrypt
bcrypt = Bcrypt(app)

## import blueprints
from app.admin.views import adminBP
from app.auth.views import authBP
from app.settings.views import settingsBP
from app.user.views import userBP
from app.masterData.views import mdBP

## Register blueprints
app.register_blueprint(adminBP, url_prefix='/admin')
app.register_blueprint(authBP, url_prefix='/auth')
app.register_blueprint(settingsBP, url_prefix='/settings')
app.register_blueprint(userBP, url_prefix='/user')
app.register_blueprint(mdBP, url_prefix='/masterData')


# indexView
@app.route('/')
def indexView():
    kwargs = {'title':'Index',
              'contentTitle': '',}
    return render_template('index.html', **kwargs)
