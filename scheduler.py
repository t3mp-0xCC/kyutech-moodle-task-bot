import datetime

def read_schedule(path):
    """ Read schedule file(path) """
    List =  open(path, 'r', encoding='utf-8').readlines()
    print("[+] {}".format(path))
    print(List)
    return List


def check_schedule(path):
    """ Check schedule from the file(path) """
    date_now = datetime.datetime.now()
    print(date_now)
    date_now_hour = date_now.hour
    print(date_now_hour)
    file = open(path, 'r')

