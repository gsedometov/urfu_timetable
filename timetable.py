from typing import Iterable

from period import PeriodWithTime


class Timetable:
    def __init__(self, days=14, periods_per_day=6):
        self._days = days
        self._periods = [[None for _ in range(periods_per_day)] for _ in range(days)]

    def __setitem__(self, key, value):
        self._periods[key[0]][key[1]] = value

    def __getitem__(self, item):
        return self._periods[item[0]][item[1]]

    def __str__(self):
        return ', '.join(str(day) for day in self._periods)

    def load_periods(self, periods: Iterable[PeriodWithTime]):
        for time, period in periods:
            if not self[time]:
                self[time] = period
            else:
                self[time[0]+self._days//2, time[1]] = period


    @classmethod
    def from_days(cls, days):
        n_days = len(days)
        n_pairs = max(days, key=len)
        tt = cls(n_days, n_pairs)
        for i, day in enumerate(days):
            for j, period in enumerate(day):
                tt[i, j] = period
        return tt


    @classmethod
    def from_periods(cls, periods):
        pass