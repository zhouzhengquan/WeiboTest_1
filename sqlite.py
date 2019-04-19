# -*- coding: utf-8 -*-
import sqlite3
#建表
def create_tables():
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    sql_fans =''' create table if not exists fans (id int, idstr text, screen_name text, name text, province int, city int, location text, description text, url text, profile_image_url text, profile_url text, domain text, weihao text, gender text, 
followers_count int, friends_count int, statuses_count int, favourites_count int, created_at text, following text, allow_all_act_msg text, geo_enabled text, verified text, verified_type int, remark text, 
status_id int, allow_all_comment text, avatar_large text, verified_reason text, follow_me text, online_status int, bi_followers_count int, lang text, star int, mbtype int, mbrank int, block_word int, tags text)
    '''
    sql_weibo='''create table if not exists weibos(created_at text,  id int, text text, source text, favorited text, truncated text, in_reply_to_status_id text, in_reply_to_user_id text,in_reply_to_screen_name text, mid text, reposts_count int, 
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
    cursor.close()

# 批量插入微博信息
def insert_weibo_batch(wbList):
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    for n in range(0, 100000):
        sql = ''' insert into weibos
                          (created_at, id, text, source, favorited, truncated, in_reply_to_status_id,in_reply_to_user_id, in_reply_to_screen_name,
                           mid, reposts_count, comments_count, user)
                          values
                          (?,?,?,?,?,?,?,?,?,?,?,?,?);'''
        data = []
        for wb in wbList:
            data.append((wb.created_at, wb.id, wb.text, wb.source, wb.favorited, wb.truncated, wb.in_reply_to_status_id,
                         wb.in_reply_to_user_id,
                         wb.in_reply_to_screen_name, wb.mid, wb.reposts_count, wb.comments_count, wb.user))
        sql = sql[:-1] + ';'
        cursor.executemany(sql, data)

    conn.commit()
    # print 'inserted'
    # '''使用游标关闭数据库的链接'''
    cursor.close()

#批量插入微博2
def insert_weibo_batch2(wbList):
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    sql = ''' insert into weibos
                  (created_at, id, text, source, favorited, truncated, in_reply_to_status_id,in_reply_to_user_id, in_reply_to_screen_name,
                   mid, reposts_count, comments_count, user)
                  values
                  (:created_at, :id, :text, :source, :favorited, :truncated, :in_reply_to_status_id, :in_reply_to_user_id, :in_reply_to_screen_name,
                   :mid, :reposts_count, :comments_count, :user)'''
    for n in range(0, 100000):
        for wb in wbList:
            cursor.execute(sql, {'created_at': wb.created_at, 'id': wb.id, 'text': wb.text, 'source': wb.source,
                                 'favorited': wb.favorited,
                                 'truncated': wb.truncated,
                                 'in_reply_to_status_id': wb.in_reply_to_status_id,
                                 'in_reply_to_user_id': wb.in_reply_to_user_id,
                                 'in_reply_to_screen_name': wb.in_reply_to_screen_name,
                                 'mid': wb.mid, 'reposts_count': wb.reposts_count, 'comments_count': wb.comments_count,
                                 'user': wb.user
                                 })

    conn.commit()
    # print 'inserted'
    # '''使用游标关闭数据库的链接'''
    cursor.close()

#插入微博
def insert_weibo(created_at,  id, text, source, favorited, truncated, in_reply_to_status_id,in_reply_to_user_id,
in_reply_to_screen_name, mid, reposts_count, comments_count, user):
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    sql = ''' insert into weibos
                  (created_at, id, text, source, favorited, truncated, in_reply_to_status_id,in_reply_to_user_id, in_reply_to_screen_name,
                   mid, reposts_count, comments_count, user)
                  values
                  (:created_at, :id, :text, :source, :favorited, :truncated, :in_reply_to_status_id, :in_reply_to_user_id, :in_reply_to_screen_name,
                   :mid, :reposts_count, :comments_count, :user)'''

    cursor.execute(sql, {'created_at': created_at, 'id': id, 'text': text, 'source': source,'favorited': favorited, 'truncated': truncated,
                         'in_reply_to_status_id': in_reply_to_status_id, 'in_reply_to_user_id': in_reply_to_user_id, 'in_reply_to_screen_name': in_reply_to_screen_name,
                         'mid': mid, 'reposts_count': reposts_count,'comments_count': comments_count, 'user': user
                         })
    conn.commit()
    # print 'inserted'
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

# 插入评论信息
def insert_comment(created_at, id, text, source, mid, user, cmtUid, status):
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    sql = ''' insert into comments
                  (created_at, id, text, source, mid, user, cmtUid, status)
                  values
                  (:created_at, :id, :text, :source, :mid, :user, :cmtUid, :status)'''

    cursor.execute(sql, {'created_at': created_at, 'id': id, 'text': text, 'source': source,
                         'mid': mid, 'user': user, 'cmtUid': cmtUid, 'status': status})
    conn.commit()
    print 'inserted'
    # '''使用游标关闭数据库的链接'''
    cursor.close()

#插入转发信息
def insert_repost(author, created_at, id, text, source, favorited, truncated, in_reply_to_status_id,
                 in_reply_to_user_id,in_reply_to_screen_name, mid, reposts_count, comments_count, user, retweeted_status):

    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    conn.text_factory = str
    # '''创建游标'''
    cursor = conn.cursor()
    sql = ''' insert into repost
                  (author, created_at, id, text, source, favorited, truncated, in_reply_to_status_id,
                 in_reply_to_user_id,in_reply_to_screen_name, mid, reposts_count, comments_count, user, retweeted_status)
                  values
                  (:author, :created_at, :id, :text, :source, :favorited, :truncated, :in_reply_to_status_id,
                 :in_reply_to_user_id,:in_reply_to_screen_name, :mid, :reposts_count, :comments_count, :user, :retweeted_status)'''

    cursor.execute(sql, {'author': author, 'created_at': created_at, 'id': id, 'text': text, 'source': source, 'favorited': favorited, 'truncated': truncated,
                         'in_reply_to_status_id': in_reply_to_status_id, 'in_reply_to_user_id': in_reply_to_user_id, 'in_reply_to_screen_name': in_reply_to_screen_name,
                         'mid': mid, 'reposts_count': reposts_count,  'comments_count': comments_count, 'user': user, 'retweeted_status': retweeted_status})
    conn.commit()
    print 'inserted'
    # '''使用游标关闭数据库的链接'''
    cursor.close()

# 插入标签
def insert_tag(id, tags):

    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    conn.text_factory = str
    # '''创建游标'''
    cursor = conn.cursor()
    sql = ''' insert into tags
                  (id, tags)
                  values
                  (:id, :tags)'''
    cursor.execute(sql, {'id': id, 'tags': tags})
    conn.commit()
    print 'inserted'
    # '''使用游标关闭数据库的链接'''
    cursor.close()

#批量插入粉丝信息
def insert_fans_batch(fanList):
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    sql = '''insert into fans
                  (id, idstr, screen_name, name, province, city, location, description, url, profile_image_url, profile_url, domain, weihao, gender, followers_count, 
                  friends_count, statuses_count, favourites_count, created_at, following, allow_all_act_msg, geo_enabled, verified, verified_type, remark, status_id, 
                  allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count, lang, star, mbtype, mbrank, block_word, tags)
                  values
                  (:id, :idstr, :screen_name, :name, :province, :city, :location, :description, :url, :profile_image_url, :profile_url, :domain, :weihao, :gender, 
                  :followers_count, :friends_count, :statuses_count, :favourites_count, :created_at, :following, :allow_all_act_msg, :geo_enabled, :verified, 
                  :verified_type, :remark, :status_id, :allow_all_comment, :avatar_large, :verified_reason, :follow_me, :online_status, :bi_followers_count, :lang, 
                  :star, :mbtype, :mbrank, :block_word, :tags)'''
    for n in range(0, 400000):
        for fan in fanList:
            cursor.execute(sql, {'id': fan.id, 'idstr': fan.idstr, 'screen_name': fan.screen_name, 'name': fan.name, 'province': fan.province, 'city': fan.city, 'location': fan.location, 'description': fan.description,
                         'url': fan.url, 'profile_image_url': fan.profile_image_url, 'profile_url': fan.profile_url, 'domain': fan.domain, 'weihao': fan.weihao, 'gender': fan.gender,
                         'followers_count': fan.followers_count, 'friends_count': fan.friends_count, 'statuses_count': fan.statuses_count, 'favourites_count': fan.favourites_count,
                         'created_at': fan.created_at, 'following': fan.following, 'allow_all_act_msg': fan.allow_all_act_msg, 'geo_enabled': fan.geo_enabled, 'verified': fan.verified,
                         'verified_type': fan.verified_type, 'remark': fan.remark, 'status_id': fan.status_id, 'allow_all_comment': fan.allow_all_comment, 'avatar_large': fan.avatar_large,
                         'avatar_large': fan.avatar_large, 'verified_reason': fan.verified_reason, 'follow_me': fan.follow_me, 'online_status': fan.online_status, 'bi_followers_count': fan.bi_followers_count,
                         'lang': fan.lang, 'star': fan.star, 'mbtype': fan.mbtype, 'mbrank': fan.mbrank, 'block_word': fan.block_word, 'tags': fan.tags
                                 })

    conn.commit()
    # print 'inserted'
    # '''使用游标关闭数据库的链接'''
    cursor.close()

#插入粉丝信息
def insert_fan(id, idstr, screen_name, name, province, city, location, description, url, profile_image_url, profile_url, domain, weihao, gender, followers_count,
               friends_count, statuses_count, favourites_count, created_at, following, allow_all_act_msg, geo_enabled, verified, verified_type, remark, status_id,
               allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count, lang, star, mbtype, mbrank, block_word, tags):
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    sql = '''insert into fans
                  (id, idstr, screen_name, name, province, city, location, description, url, profile_image_url, profile_url, domain, weihao, gender, followers_count, 
                  friends_count, statuses_count, favourites_count, created_at, following, allow_all_act_msg, geo_enabled, verified, verified_type, remark, status_id, 
                  allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count, lang, star, mbtype, mbrank, block_word, tags)
                  values
                  (:id, :idstr, :screen_name, :name, :province, :city, :location, :description, :url, :profile_image_url, :profile_url, :domain, :weihao, :gender, 
                  :followers_count, :friends_count, :statuses_count, :favourites_count, :created_at, :following, :allow_all_act_msg, :geo_enabled, :verified, 
                  :verified_type, :remark, :status_id, :allow_all_comment, :avatar_large, :verified_reason, :follow_me, :online_status, :bi_followers_count, :lang, 
                  :star, :mbtype, :mbrank, :block_word, :tags)'''

    cursor.execute(sql, {'id': id, 'idstr': idstr, 'screen_name': screen_name, 'name': name, 'province': province, 'city': city, 'location': location, 'description': description,
                         'url': url, 'profile_image_url': profile_image_url, 'profile_url': profile_url, 'domain': domain, 'weihao': weihao, 'gender': gender,
                         'followers_count': followers_count, 'friends_count': friends_count, 'statuses_count': statuses_count, 'favourites_count': favourites_count,
                         'created_at': created_at, 'following': following, 'allow_all_act_msg': allow_all_act_msg, 'geo_enabled': geo_enabled, 'verified': verified,
                         'verified_type': verified_type, 'remark': remark, 'status_id': status_id, 'allow_all_comment': allow_all_comment, 'avatar_large': avatar_large,
                         'avatar_large': avatar_large, 'verified_reason': verified_reason, 'follow_me': follow_me, 'online_status': online_status, 'bi_followers_count': bi_followers_count,
                         'lang': lang, 'star': star, 'mbtype': mbtype, 'mbrank': mbrank, 'block_word': block_word, 'tags': tags
                         })
    conn.commit()
    print 'inserted'
    # '''使用游标关闭数据库的链接'''
    cursor.close()

#插入NBA信息
def insert_nba_info(id, screen_name, name, province, city, location, description , url, profile_image_url, domain, gender, followers_count, friends_count, statuses_count,
favourites_count, created_at, following , geo_enabled, verified, status, allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count):
    # '''创建一个数据库，文件名'''
    conn = sqlite3.connect('test.db')
    # '''创建游标'''
    cursor = conn.cursor()
    sql = '''insert into user
                  (id, screen_name, name, province, city, location, description , url, profile_image_url, domain, gender, followers_count, friends_count, statuses_count,
favourites_count, created_at, following , geo_enabled, verified, status, allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count)
                  values
                  (:id, :screen_name, :name, :province, :city, :location, :description, :url, :profile_image_url, :domain, :gender, 
                  :followers_count, :friends_count, :statuses_count, :favourites_count, :created_at, :following, :geo_enabled, :verified, 
                  :status, :allow_all_comment, :avatar_large, :verified_reason, :follow_me, :online_status, :bi_followers_count
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

#存入微博信息
def save_weibo(wbList):
    for wb in wbList:
        # wb.displayWeibo()
        insert_weibo(wb.created_at, wb.id, wb.text, wb.source, wb.favorited, wb.truncated, wb.in_reply_to_status_id,wb.in_reply_to_user_id,
wb.in_reply_to_screen_name, wb.mid, wb.reposts_count, wb.comments_count, wb.user)

#存入评论信息
def save_comment(cmtList):
    for cmt in cmtList:
        insert_comment(cmt.created_at, cmt.id, cmt.text, cmt.source, cmt.mid, cmt.user, cmt.cmtUid, cmt.status)

#存入粉丝信息
def save_fans(fansList):
    for u in fansList:
        insert_fan(u.id, u.idstr, u.screen_name, u.name, u.province, u.city, u.location, u.description, u.url, u.profile_image_url, u.profile_url, u.domain,
                    u.weihao, u.gender, u.followers_count, u.friends_count, u.statuses_count, u.favourites_count, u.created_at, u.following, u.allow_all_act_msg,
                    u.geo_enabled, u.verified, u.verified_type, u.remark, u.status_id, u.allow_all_comment, u.avatar_large, u.verified_reason, u.follow_me,
                    u.online_status, u.bi_followers_count, u.lang, u.star, u.mbtype, u.mbrank, u.block_word, u.tags)

#存入转发信息
def save_repost(repList):
    for rep in repList:
        insert_repost(rep.author, rep.created_at, rep.id, rep.text, rep.source, rep.favorited, rep.truncated, rep.in_reply_to_status_id,
                 rep.in_reply_to_user_id,rep.in_reply_to_screen_name, rep.mid, rep.reposts_count, rep.comments_count, rep.user, rep.retweeted_status)