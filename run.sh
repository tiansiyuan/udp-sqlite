#!/bin/sh

log='tmp/log.txt'
date > $log
./sqlite.py >> $log
date >> $log
