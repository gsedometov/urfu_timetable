import datetime

import requests


def get_group_id(group):
    resp = requests.get('http://urfu.ru/api/schedule/groups/suggest/', {'query': group})
    return resp.json()['suggestions'][0]['data']


def get_group_schedule(group_id, date=None):
    if date is None:
        date = datetime.date.today().strftime('%Y%m%d')
    resp = requests.get('http://urfu.ru/api/schedule/groups/calendar/{0}/{1}/'.format(group_id, date))
    return resp.content.decode()