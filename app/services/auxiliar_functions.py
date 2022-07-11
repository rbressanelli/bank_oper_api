from werkzeug.exceptions import BadRequest
from datetime import datetime


def date_maker():
    return datetime.now()
