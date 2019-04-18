# -*- coding: UTF-8 -*-

import pymysql

def create_tables():
    # 打开数据库连接
    db = pymysql.connect("172.16.20.56", "slv", "dq@1214", "nba")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql_fans = ''' create table if not exists fans (id int, idstr text, screen_name text, name text, province int, city int, location text, description text, url text, profile_image_url text, profile_url text, domain text, weihao text, gender text, 
    followers_count int, friends_count int, statuses_count int, favourites_count int, created_at text, following text, allow_all_act_msg text, geo_enabled text, verified text, verified_type int, remark text, 
    status_id int, allow_all_comment text, avatar_large text, verified_reason text, follow_me text, online_status int, bi_followers_count int, lang text, star int, mbtype int, mbrank int, block_word int, tags text)
        '''
    sql_weibo = '''create table if not exists weibos(created_at text,  id int, text text, source text, favorited text, truncated text, in_reply_to_status_id text, in_reply_to_user_id text,in_reply_to_screen_name text, mid text, reposts_count int, 
    comments_count int,  user text)'''
    sql_comment = '''create table if not exists comments(created_at text, id int, text text, source text, mid text, user text, cmtUid int, status text)'''
    sql_repost = '''create table if not exists repost(author int, created_at text, id int, text text, source text, favorited text, truncated text, in_reply_to_status_id text,
    in_reply_to_user_id text,in_reply_to_screen_name text, mid text, reposts_count int, comments_count int, user text, retweeted_status text
    )'''
    sql_user = '''Create table if not exists user(id int, screen_name text, name text, province text, city text, location text, description text, url text, 
        profile_image_url text, domain text, gender text, followers_count int, friends_count int, statuses_count int, favourites_count int, created_at text, following text ,
        geo_enabled text, verified text, status text, allow_all_comment text, avatar_large text, verified_reason text, follow_me text, online_status int, bi_followers_count int )
        '''
    cursor.execute(sql_fans)
    cursor.execute(sql_weibo)
    cursor.execute(sql_comment)
    cursor.execute(sql_repost)
    cursor.execute(sql_user)

    # 关闭数据库连接
    db.close()

#插入NBA信息
def insert_nba_info(id, screen_name, name, province, city, location, description , url, profile_image_url, domain, gender, followers_count, friends_count, statuses_count,
favourites_count, created_at, following , geo_enabled, verified, status, allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count):

    # 打开数据库连接
    conn = pymysql.connect("172.16.20.56", "slv", "dq@1214", "nba")
    # '''创建游标'''
    cursor = conn.cursor()
    sql = '''insert into user
                  (id, screen_name, name, province, city, location, description , url, profile_image_url, domain, gender, followers_count, friends_count, statuses_count,
favourites_count, created_at, following , geo_enabled, verified, status, allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count)
                  values
                  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s
                  )'''

    cursor.execute(sql, {'id': id,  'screen_name': screen_name, 'name': name, 'province': province, 'city': city, 'location': location, 'description': description,
                         'url': url, 'profile_image_url': profile_image_url, 'domain': domain,  'gender': gender,
                         'followers_count': followers_count, 'friends_count': friends_count, 'statuses_count': statuses_count, 'favourites_count': favourites_count,
                         'created_at': created_at, 'following': following,  'geo_enabled': geo_enabled, 'verified': verified,
                         'status': status,  'allow_all_comment': allow_all_comment, 'avatar_large': avatar_large,
                         'avatar_large': avatar_large, 'verified_reason': verified_reason, 'follow_me': follow_me, 'online_status': online_status, 'bi_followers_count': bi_followers_count
                        })
    conn.commit()
    print 'inserted'
    # '''使用游标关闭数据库的链接'''
    cursor.close()

