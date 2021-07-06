from flask import *

show_bp = Blueprint('show', __name__)


@show_bp.route('/')
def show():
    return "6666"
