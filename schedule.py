from collections import namedtuple
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

Period = namedtuple('Period', ['time', 'discipline', 'room', 'teacher'])

period_mapping = {
    (8, 30): 1,
    (10, 15): 2,
    (12, 0): 3,
    (14, 15): 4,
    (16, 0): 5,
    (17, 40): 6
}


def place_of_week(start_time):
    date = datetime.datetime.strptime(start_time, '%Y%m%dT%H%M%S')
    day = date.weekday()
    n_period = period_mapping[(date.hour, date.minute)]
    return day, n_period


def read_period(it):
    next(it)
    next(it)
    place = place_of_week(next(it).split(':')[-1])
    next(it)
    discipline = next(it).split(':')[-1]
    if discipline == 'Физическая культура':
        room = None
        teacher = None
    else:
        room = next(it).split(':')[-1]
        teacher = next(it).split(':')[-1].strip()
    next(it)
    return Period(place, discipline, room, teacher)


def extract_periods(schedule: str):
    periods = []
    it = iter(schedule.splitlines()[7:])
    while True:
        try:
            periods.append(read_period(it))
        except StopIteration:
            return periods
