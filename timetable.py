from typing import Iterable

from period import PeriodWithTime


class Timetable:
    def __init__(self, days=14, periods_per_day=6):
        self._days = days
        self._periods = [[None for _ in range(periods_per_day)] for _ in range(days)]

    def __setitem__(self, key, value):
        if key[1] <= 0:
            raise IndexError('Пары нумеруются с 1')
        self._periods[key[0]][key[1]-1] = value

    def __getitem__(self, item):
        if item[1] <= 0:
            raise IndexError('Пары нумеруются с 1')
        return self._periods[item[0]][item[1]-1]

    def __str__(self):
        return ', '.join(str(day) for day in self._periods)

    def load_periods(self, periods: Iterable[PeriodWithTime]):
        for time, period in periods:
            if not self[time]:
                self[time] = period
            else:
                self[time[0]+self._days//2, time[1]] = period