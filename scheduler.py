def read_schedule(path):
    """ Read schedule file(path) """
    file = open(path, 'r')
    schedule = file.readline()
    print("[+] {}".format(path))
    print(schedule)
    file.close()
    return schedule
