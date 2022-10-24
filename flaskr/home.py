from flask import (
    Blueprint, render_template, request
)
from werkzeug.exceptions import abort
import pandas as pd

from flaskr.db import get_db

bp = Blueprint('home', __name__, url_prefix='/home')


# Routes the contact page
@bp.route('/', methods=["GET", "POST"])
def contact():
    return render_template('home/contact.html')


# Routes the about page
@bp.route('/about')
def about():
    return render_template('home/about.html')
