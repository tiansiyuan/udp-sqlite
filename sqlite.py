#!/usr/bin/env python3

import multiprocessing
import sqlite3
import datetime
import random
import os

def createDB(n):
    filename = 'tmp/test%d.db' % n
    if os.path.exists(filename):
        os.remove(filename)

    conn = sqlite3.connect(filename)
    print("Opened database %d successfully" % n)
    c = conn.cursor()
    c.execute('''CREATE TABLE realtime (
        id integer not null primary key,
        ch integer not null,
        v  integer not null
    )''')

    conn.commit()
    conn.close()

def writeDB(n):
    '''write into DB n'''
    filename = 'tmp/test%d.db' % n
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    sql = 'INSERT into realtime VALUES (?, ?, ?)'
    index = 0
    for i in range(60*60*24):
        start = datetime.datetime.now()
        for j in range(2000):
            data = (index, n, random.randint(0, 2**63-1)) 
            c.execute(sql, data)
            index += 1

        conn.commit()
        end = datetime.datetime.now()
        print('channel %d == %d*2000 ----> %d microseconds' % (n, i, (end-start).microseconds))


def main(n):
    for i in range(n):
        createDB(i)

    pool = multiprocessing.Pool(processes = 8)
    for i in range(n):
        pool.apply_async(writeDB, args=(i,))

    pool.close()
    pool.join()

if __name__ == '__main__':
    main(8)
