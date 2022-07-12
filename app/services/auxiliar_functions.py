from datetime import datetime

from werkzeug.exceptions import BadRequest


def date_maker():
    return datetime.now()
