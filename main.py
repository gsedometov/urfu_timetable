#!/usr/bin/env python3
from group import get_group_id, get_group_schedule
from period import extract_periods, split_to_days, Period
from timetable import Timetable


def main():
    group_id = get_group_id('Фт-340007')
    schedule = get_group_schedule(group_id)
    periods = extract_periods(schedule)
    tt = Timetable()
    tt.load_periods(periods)
    print(split_to_days([((1, 1), Period(1, 2, 3))]))


if __name__ == '__main__':
    main()
