#!/usr/bin/env python3
'''
Get data from UDP and save into SQLite DB.
Later query according to user provided condition, data/time.
And present the data as graph via web.

Producer: getData
Consumer: writeDB
'''

import multiprocessing
import sqlite3
import datetime
import random
import os

def getData():
    '''Get data from network via UDP.
    Or use random numbers for testing.'''
    pass

def createDB(n):
    '''Create DB, naming as date'''
    filename = 'tmp/test%d.db' % n
    if os.path.exists(filename):
        os.remove(filename)

    conn = sqlite3.connect(filename)
    print("Opened database %d successfully" % n)
    c = conn.cursor()
    c.execute('''CREATE TABLE realtime (
        id integer not null primary key,
        ch integer not null,
        sn integer not null,
        v  integer not null
    )''')

    conn.commit()
    conn.close()

def writeDB(n):
    '''write into DB n'''
    filename = 'tmp/test%d.db' % n
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    sql = 'INSERT into realtime VALUES (NULL, ?, ?, ?)'
    sn = 0
    for i in range(60*60): # *24
        start = datetime.datetime.now()
        dataSet = []
        for j in range(20*8): # 20 = 1000 / 50
            for ch in range(1,9): # 8 channels
                data = (ch, sn, random.randint(0, 2**16-1))
                dateSet = dataSet.append(data)

            sn += 1

        c.executemany(sql, dataSet)
        conn.commit()
        end = datetime.datetime.now()
        print('channel %d == %d*2000 ----> %d microseconds' % (ch, i, (end-start).microseconds))


def saveCSV():
    pass


def query():
    '''get data from DB.'''
    pass

def drawPic():
    pass


def main(n):
    for i in range(n):
        createDB(i)
        writeDB(i)

    # pool = multiprocessing.Pool(processes = 8)
    # for i in range(n):
    #     pool.apply_async(writeDB, args=(i,))

    # pool.close()
    # pool.join()

if __name__ == '__main__':
    main(1)
