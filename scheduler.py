import datetime

def read_schedule(path):
    """ Read schedule file(path) """
    List =  open(path, 'r', encoding='utf-8').readlines()
    print("[i] read_schedule from {}".format(path))
    print('\n'.join(List))
    return List


def add_schedule(path, time):
    """ Add schedule """
    if check_value(time, path):
        with open(path, 'a') as f:
            f.write(time + '\n')
        return True
    else:
        return False

def check_value(val, path):
    """ Check user input value """
    if len(val) > 5:
        print("[Err] check_value: len error")
        return False
    
    temp = val.split(':')
    if not(temp[0].isdecimal() and temp[1].isdecimal()):
        print("[Err] check_value: format error")
        return False

    current_list = '\n'.join(read_schedule(path))
    if val in current_list:
        print("[Err] check_value: duplicate error")
        return False

    return True


def check_schedule(path):
    """ Check schedule from the file(path) """
    now = datetime.datetime.now()
    print("[i] now: {}".format(now))
    file = read_schedule(path)
    for i in range(11):# check rug (check_every_ten_min)
        time = (now - datetime.timedelta(minutes=i)).strftime('%H:%M')
        if time[0] == '0':# remove first 0(ex. 08:00 -> 8:00)
            time = time.replace(time[0], '', 1)

        for schedule in file:
            schedule = schedule.replace('\n','')
            print("[i] compare {} and {}".format(time, schedule))
            if schedule == time:
                print("[+] schedule matched !")
                return True

    return False
    

