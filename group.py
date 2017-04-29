import datetime

import requests


def get_group_id(group):
    resp = requests.get('http://urfu.ru/api/schedule/groups/suggest/', {'query': group})
    return resp.json()['suggestions'][0]['data']


def get_group_schedule(group_id, date: datetime.date = None):
    if date is None:
        today = datetime.date.today()
        monday = today - datetime.timedelta(today.weekday())
        date = monday.strftime('%Y%m%d')
    else:
        date = date.strftime
    resp = requests.get('http://urfu.ru/api/schedule/groups/calendar/{0}/{1}/'.format(group_id, date))
    return resp.content.decode()
