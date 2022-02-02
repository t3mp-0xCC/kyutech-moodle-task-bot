import sqlite3

DB = 'main.db'

def db_init():
    print("[+] databse init")
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS schedule(time STRING)')
        cur.execute('SELECT COUNT(*) from schedule')
        result = cur.fetchall()
        if result[0][0] == 0:
            print("[i] database is empty !")
            cur.execute('INSERT INTO schedule(time) values("8:00")')
            cur.execute('INSERT INTO schedule(time) values("12:00")')
            conn.commit()

        cur.close()
    conn.close()


def read_table(table):
    """ Read databse table and return list """
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('SELECT * FROM {}'.format(table))
    data = cur.fetchall()
    print("[+] read table: {}".format(table))
    print(data)
    cur.close()
    conn.close()
    return data
