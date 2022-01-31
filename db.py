import sqlite3

DB = 'main.db'

def db_init():
    print("[+] databse init")
    with sqlite3.connect(DB) as db:
        cur = db.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS schedule(time STRING)')
        cur.execute('SELECT COUNT(*) from schedule')
        result = cur.fetchall()
        print(result)
        if result[0][0] == 0:
            print("[i] database is empty !")
            cur.execute('INSERT INTO schedule(time) values("8:00")')
            db.commit()

        cur.close()
