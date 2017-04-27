from collections import namedtuple
import datetime
from itertools import groupby
from operator import itemgetter
from typing import Iterable, Tuple


Period = namedtuple('Period', ['discipline', 'room', 'teacher'])
PeriodWithTime = Tuple[Tuple[int, int], Period]

period_mapping = {
    (8, 30): 0,
    (10, 15): 1,
    (12, 0): 2,
    (14, 15): 3,
    (16, 0): 4,
    (17, 40): 5
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
    return place, Period(discipline, room, teacher)


def extract_periods(schedule: str):
    periods = []
    it = iter(schedule.splitlines()[7:])
    while True:
        try:
            periods.append(read_period(it))
        except StopIteration:
            return periods


def split_to_days(periods: Iterable[PeriodWithTime]):
    sorted_ = sorted(periods, key=itemgetter(0, 0))
    days = groupby(sorted_, key=itemgetter(0, 0))
    return [list(d) for k, d in days]
