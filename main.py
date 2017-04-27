#!/usr/bin/env python3
from schedule import *


def main():
    group_id = get_group_id('Фт-340007')
    schedule = get_group_schedule(group_id)
    print(extract_periods(schedule))
    #print(schedule)
    #print(place_of_week('20170427T120000'))


if __name__ == '__main__':
    main()
