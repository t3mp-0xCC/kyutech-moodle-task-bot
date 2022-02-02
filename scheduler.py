# -*- coding:utf-8 -*-
import datetime
from db import read_table

TABLE = 'schedule'


def read_schedule(path):
    """ Read schedule from database """
    schedule = read_table(TABLE)# list of tuple
    return schedule


def add_schedule(path, time):
    """ Add schedule """
    if check_value(path, time) and check_duplicate(path, time):
        with open(path, 'a') as f:
            f.write(time + '\n')
        return True
    else:
        return False


def remove_schedule(path, time):
    """ Remove schedule """
    if check_value(path, time) and not(check_duplicate(path, time)):
        file = open(path,'r')
        lst = []
        for line  in file:
            if time in line:
                line = line.replace(time, '')
            lst.append(line)
        file.close()
        file = open(path, 'w')
        for line in lst:
            file.write(line)
        file.close()

        return True
    else:
        return False


def check_value(path, val):
    """ Check user input value """
    if len(val) > 5:
        print("[Err] check_value: len error")
        return False

    if not(':' in val):
        print("[Err] check_value: format error(not ':' in val)")
        return False

    temp = val.split(':')
    if not(temp[0].isdecimal() and temp[1].isdecimal()):
        print("[Err] check_value: format error(val is not decimal)")
        return False

    if int(temp[0]) > 24 or (int(temp[1]) > 59 or len(temp[1]) < 2):
        print("[Err] check_value: format error(invalid decimal)")
        return False

    return True


def check_duplicate(path, val):
    current_list = '\n'.join(read_schedule(path))
    if val in current_list:
        return False

    return True


def check_schedule(path):
    """ Compare  """
    now = datetime.datetime.now()
    print("[i] now: {}".format(now))
    schedule = read_schedule(path)
    for i in range(10):# check rug (check_every_ten_min)
        cmp_time = (now - datetime.timedelta(minutes=i)).strftime('%H:%M')
        if cmp_time[0] == '0':# remove first 0(ex. 08:00 -> 8:00)
            cmp_time = cmp_time.replace(cmp_time[0], '', 1)
        
        for schedule in times:
            print("[i] compare {} and {}".format(time, schedule))
            if schedule == time:
                print("[+] schedule matched !")
                return True

    return False
