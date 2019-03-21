# -*- coding: utf-8 -*-
import sqlite3

def create_table(cursor):
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    # '''执行语句'''
    sql = '''create table weibo (
            id int,
            text text,
            created_at text,
            author text)'''

    cursor.execute(sql)

    # '''使用游标关闭数据库的链接'''
    cursor.close()

# 插入微博
def insert_weibo(author, created_at, id, text):
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    sql = ''' insert into weibo
                  (author, created_at, id, text)
                  values
                  (:wb_author, :wb_created_at, :wb_id, :wb_text)'''
    # 把数据保存到name username和 id_num中
    cursor.execute(sql, {'wb_author': author, 'wb_created_at': created_at, 'wb_id': id, 'wb_text': text})
    conn.commit()
    print 'inserted'
    # '''使用游标关闭数据库的链接'''
    cursor.close()

def select_weibo():
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    sql = ''' select author, created_at, id, text from weibo'''
    # 执行语句
    results = cursor.execute(sql)

    # 遍历打印输出
    all_weibo = results.fetchall()
    for weibo in all_weibo:
        print(weibo)
    # '''使用游标关闭数据库的链接'''
    cursor.close()

# 插入评论
def insert_comment(author, created_at, id, text):
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    sql = ''' insert into comment
                  (author, created_at, id, text)
                  values
                  (:wb_author, :wb_created_at, :wb_id, :wb_text)'''
    # 把数据保存到name username和 id_num中
    cursor.execute(sql, {'wb_author': author, 'wb_created_at': created_at, 'wb_id': id, 'wb_text': text})
    conn.commit()
    print 'inserted'
    # '''使用游标关闭数据库的链接'''
    cursor.close()