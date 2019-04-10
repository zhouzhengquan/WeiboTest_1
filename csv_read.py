# -*- coding: utf-8 -*-
import csv
import sqlite

def csv_read(path):
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        column = [row[2] for row in reader]
    # print column
    return column

def main():
    tags = '[{"77463":"偶喜欢玩","weight":"518943","flag":"0"},{"684":"运动","weight":"1008693","flag":"1"},{"1235":"幽默","weight":"1065730","flag":"1"},{"314":"摄影","weight":"1378501","flag":"1"},{"1501":"自由","weight":"2439141","flag":"1"},{"464":"美食","weight":"28298284","flag":"1"},{"847":"80后","weight":"3663926","flag":"1"},{"2526":"迪斯尼","weight":"648","flag":"0"},{"829":"旅行","weight":"3294172","flag":"1"},{"285":"音乐","weight":"6714563","flag":"1"}]'
    uids = csv_read('nba_uid.csv')
    for n in uids:
        sqlite.insert_tag(n, tags)
    # sqlite.insert_tag(1212, tags)
    print 'finished'

if __name__ == '__main__':
    main()