import datetime

def read_schedule(path):
    """ Read schedule file(path) """
    file = open(path, 'r')
    schedule = file.readline()
    print("[+] {}".format(path))
    print(schedule)
    file.close()
    return schedule

def check_schedule(path):
    """ Check schedule from the file(path) """
    date_now = datetime.datetime.now()
    print(date_now)
    date_now_hour = date_now.hour
    print(date_now_hour)
    file = open(path, 'r')

