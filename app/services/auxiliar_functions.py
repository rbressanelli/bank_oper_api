from datetime import date, datetime


def date_maker():
    return date.today()


def only_date(data):
    temp = datetime.strftime(data, "%Y-%m-%d")
    return datetime.strptime(temp, "%Y-%m-%d").date()
