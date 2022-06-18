from flask import Blueprint

soc = Blueprint('soc', __name__)

from . import events