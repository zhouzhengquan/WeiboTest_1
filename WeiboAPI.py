# -*- coding: utf-8 -*-
import webbrowser
import sqlite
from entity import weibo, repost, comment,fan, user
from weibo import APIClient
from retry import retry
import requests
import csv_read
import json
import time

#通过uid获取用户信息
def get_userInfo(client):
    uids = csv_read.csv_read('nba_uid.csv')
    a = []
    for i in range(1, 11):
        u = uids[i]
        print u
        if i%3 == 0:
            a.append(u)
            s = ','.join(a)
            print s
            payload = {'uids': s, 'access_token': '2.00JjZUDC7fZTtB0483f581e407KckJ'}
            ret = requests.get('https://c.api.weibo.com/2/users/show_batch/other.json', params=payload)
            print '获取用户信息url：', ret.url
            print ret.text
            a = []
        else:
            a.append(u)

# 获取粉丝个人信息
def get_fans_info(client, access_token, uid):
    fansList = []
    cursor = 0
    length = 2
    while length > 1:
        print 'cursor:', cursor
        friends = client.friendships__followers(access_token = access_token,uid=uid, count = 3, cursor=cursor)
        print friends
        cursor = friends['next_cursor']
        length = len(friends['users'])
        print 'length:',length
        for i in range(0, length):
            if friends['users'][i].has_key('id'):
                id = friends['users'][i]['id']
                idstr = friends['users'][i]['idstr']
                screen_name = friends['users'][i]['screen_name']
                name = friends['users'][i]['name']
                province = friends['users'][i]['province']
                city = friends['users'][i]['city']
                location = friends['users'][i]['location']
                description = friends['users'][i]['description']
                url = friends['users'][i]['url']
                profile_image_url = friends['users'][i]['profile_image_url']
                profile_url = friends['users'][i]['profile_url']
                domain = friends['users'][i]['domain']
                weihao = friends['users'][i]['weihao']
                gender = friends['users'][i]['gender']
                followers_count = friends['users'][i]['followers_count']
                friends_count = friends['users'][i]['friends_count']
                statuses_count = friends['users'][i]['statuses_count']
                favourites_count = friends['users'][i]['favourites_count']
                created_at = friends['users'][i]['created_at']
                following = friends['users'][i]['following']
                allow_all_act_msg = friends['users'][i]['allow_all_act_msg']
                geo_enabled = friends['users'][i]['geo_enabled']
                verified = friends['users'][i]['verified']
                verified_type = friends['users'][i]['verified_type']
                remark = friends['users'][i]['remark']
                status_id = friends['users'][i]['status_id']
                allow_all_comment = friends['users'][i]['allow_all_comment']
                avatar_large = friends['users'][i]['avatar_large']
                verified_reason = friends['users'][i]['verified_reason']
                follow_me = friends['users'][i]['follow_me']
                online_status = friends['users'][i]['online_status']
                bi_followers_count = friends['users'][i]['bi_followers_count']
                lang = friends['users'][i]['lang']
                star = friends['users'][i]['star']
                mbtype = friends['users'][i]['mbtype']
                mbrank = friends['users'][i]['mbrank']
                block_word = friends['users'][i]['block_word']

                payload = {'uids': id,'access_token':'2.00JjZUDC7fZTtB0483f581e407KckJ'}
                ret = requests.get('https://c.api.weibo.com/2/tags/tags_batch/other.json', params=payload)

                tags = ret.text

                f = fan.Fan(id, idstr, screen_name, name, province, city, location, description, url, profile_image_url, profile_url, domain, weihao, gender,
                            followers_count, friends_count, statuses_count, favourites_count, created_at, following, allow_all_act_msg, geo_enabled, verified,
                            verified_type, remark, status_id, allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count, lang, star, mbtype,mbrank, block_word, tags)
                # u.displayUser()
                fansList.append(f)

    return fansList

#获取NBA信息
def get_nba_Info(client, uid):
    user = client.users__show(uid=uid)
    print user
    id = user['id']
    screen_name = user['screen_name']
    name = user['name']
    province = user['province']
    city = user['city']
    location = user['location']
    description = user['description']
    url = user['url']
    profile_image_url = user['profile_image_url']
    domain = user['domain']
    gender = user['gender']
    followers_count = user['followers_count']
    friends_count = user['friends_count']
    statuses_count = user['statuses_count']
    favourites_count = user['favourites_count']
    created_at = user['created_at']
    following = user['following']
    geo_enabled = user['geo_enabled']
    verified = user['verified']
    status = str(user['status'])
    allow_all_comment = user['allow_all_comment']
    avatar_large = user['avatar_large']
    verified_reason = user['verified_reason']
    follow_me = user['follow_me']
    online_status = user['online_status']
    bi_followers_count = user['bi_followers_count']
#     u = user.User(id, screen_name, name, province, city, location, description , url, profile_image_url, domain, gender, followers_count, friends_count, statuses_count,
# favourites_count, created_at, following ,c , geo_enabled, verified, status, allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count)
    sqlite.insert_nba_info(id, screen_name, name, province, city, location, description , url, profile_image_url, domain, gender, followers_count, friends_count, statuses_count,
favourites_count, created_at, following ,geo_enabled, verified, status, allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count)
    print 'inserted'
#粉丝模块
# @retry(tries=3, delay=2)
def get_fans_api_data(client, access_token, uid):
    #1.获取全部粉丝数、关注数、微博数
    # payload = { 'uids': uid, 'access_token': access_token}
    # ret = requests.get('https://c.api.weibo.com/2/users/counts_batch/other.json', params=payload)
    # print '获取用户的粉丝数、关注数、微博数url：', ret.url
    # print ret.text

    #2.获取NBA的信息
    get_nba_Info(client, uid)

    #获取用户信息
    # get_userInfo(client)


    #3.获取粉丝个人信息
    # start = time.clock()
    # fans = get_fans_info(client, access_token, uid)
    # for n in range(0, 400000):
    #     sqlite.save_fans(fans)
    # end = time.clock()
    # print "run: %f s" % (end - start)
    #4.获取粉丝感兴趣的标签
    #4.1获取粉丝列表，4.2获取粉丝标签为商业API，不可用
    # friends = client.friendships__followers(uid=1883881851L)
    # print friends
    # # 4.获取粉丝感兴趣的标签
    # payload = { 'uids':'1883881851','access_token': '2.00JjZUDC7fZTtB0483f581e407KckJ'}
    # ret = requests.get('https://c.api.weibo.com/2/tags/tags_batch/other.json', params=payload)
    # print '获取粉丝标签url：', ret.url
    # print ret.text

#获取账号下所有微博的转发
def get_repost(uid, client, access_token, id):
    repList = []

    payload = {'access_token':access_token, 'id': id}
    ret = requests.get('https://c.api.weibo.com/2/statuses/repost_timeline/all.json',params=payload)
    items = json.loads(ret.text.encode('utf-8'))['reposts']

    for i in range(0, len(items)):
        if items[i].has_key('id') and items[i].has_key('text'):
            created_at = items[i]['created_at']
            id = items[i]['id']
            text = items[i]['text']
            source = items[i]['source']
            favorited = items[i]['favorited']
            truncated = items[i]['truncated']
            in_reply_to_status_id = items[i]['in_reply_to_status_id']
            in_reply_to_user_id = items[i]['in_reply_to_user_id']
            in_reply_to_screen_name = items[i]['in_reply_to_screen_name']
            mid = items[i]['mid']
            reposts_count = items[i]['reposts_count']
            comments_count = items[i]['comments_count']
            user = str(items[i]['user'])
            retweeted_status = str(items[i]['retweeted_status'])
            rep = repost.Repost(uid, created_at, id, text, source, favorited, truncated, in_reply_to_status_id, in_reply_to_user_id,
                                in_reply_to_screen_name, mid, reposts_count, comments_count, user, retweeted_status)
            rep.displayRepost()
            repList.append(rep)
    print repList
    sqlite.save_repost(repList)
    return

# 获取当前用户发布的微博
def get_weibo(client, access_token, uid):
    wbList = []
    page = 1
    length = 20

    while length >19 and page <3:
        payload = {'uids':uid,'access_token':access_token,'page':page}
        ret = requests.get('https://c.api.weibo.com/2/statuses/user_timeline_batch.json',params=payload)
        print ret.text
        items = json.loads(ret.text.encode('utf-8'))['statuses']
        # print items
        length = len(items)
        page = page + 1
        for i in range(0, length):
            if items[i].has_key('id') and items[i].has_key('text'):
                created_at = items[i]['created_at']
                id = items[i]['id']
                text = items[i]['text']
                source = items[i]['source']
                favorited = items[i]['favorited']
                truncated = items[i]['truncated']
                in_reply_to_status_id = items[i]['in_reply_to_status_id']
                in_reply_to_user_id = items[i]['in_reply_to_user_id']
                in_reply_to_screen_name = items[i]['in_reply_to_screen_name']

                mid = items[i]['mid']
                reposts_count = items[i]['reposts_count']
                comments_count = items[i]['comments_count']

                # annotations = items[i]['annotations']
                user = str(items[i]['user'])

                wb = weibo.Weibo(created_at,  id, text, source, favorited, truncated, in_reply_to_status_id,in_reply_to_user_id,in_reply_to_screen_name,
                                  mid, reposts_count, comments_count, user)
                # wb.displayWeibo()
                wbList.append(wb)
                get_repost(uid, client, access_token, id)

    print len(wbList)
    return wbList

# 获取账号下所有评论
def get_comment(client, access_token, uid):
    cmtList = []
    page = 1
    length = 50

    while length >0 and page <3:
        payload = {'uid':uid,'access_token':access_token,'page':page}
        ret = requests.get('https://c.api.weibo.com/2/comments/to_me/other.json',params=payload)
        items = json.loads(ret.text.encode('utf-8'))['comments']
        length = len(items)
        print length
        page = page + 1
        for i in range(0, length):
            if items[i].has_key('id') and items[i].has_key('text'):
                created_at = items[i]['created_at']
                id = items[i]['id']
                text = items[i]['text']
                source = items[i]['source']
                mid = items[i]['mid']
                user = str(items[i]['user'])
                status = str(items[i]['status'])
                cmtUid = items[i]['user']['id']
                cmt = comment.Comment(created_at, id, text, source, mid, user, cmtUid, status)
                cmt.displayComment()
                cmtList.append(cmt)

        print len(cmtList)
    return cmtList

#微博模块
@retry(tries=3, delay=2)
def get_weibos_api_data(client, access_token, uid):
    #1.获取当前用户发布的微博
    weibo = get_weibo(client, access_token, uid)
    sqlite.save_weibo(weibo)

    #2.获取单个微博转发情况
    # report_items = client.statuses.repost_timeline.get(id=4248672260891942)
    # print report_items

    # 3.获取单个微博评论
    # comments = client.comments__show(id=4248672260891942)
    # print '评论：', comments

    #4.获取账号下所有评论
    comment = get_comment(client, access_token, uid)
    sqlite.save_comment(comment)

def get_api_data(client, access_token, uid):
    try:
        get_fans_api_data(client, access_token, uid)
        get_weibos_api_data(client, access_token, uid)
    except Exception:
        print Exception.message


def main():

    APP_KEY = '1735879932'  # 注意替换这里为自己申请的App信息
    APP_SECRET = 'b2fc940caf0ddf92c00fa0d016f1550d'
    CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'  # 回调授权页面

    # 利用官方微博SDK
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    print "clint: ", client

    # # 得到授权页面的url，利用webbrowser打开这个url
    # url = client.get_authorize_url()
    # print url
    # webbrowser.open_new(url)
    #
    # # 获取code=后面的内容
    # print '输入url中code后面的内容后按回车键：'
    # code = raw_input()
    # # code = '5b95256d0591183f06ebf8a9c4a46835'
    # r = client.request_access_token(code)
    # access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
    # expires_in = r.expires_in
    # print "access_token: ", access_token
    # print "expires_in: ", expires_in

    access_token = '2.00JjZUDC7fZTtB0483f581e407KckJ'
    expires_in = '1711877591'
    uid = 1883881851

    # access_token = '2.00JXH7OG7fZTtBab4706696c0QHh8u'
    # expires_in = '1554231598'
    # 设置得到的access_token
    client.set_access_token(access_token, expires_in)

    sqlite.create_tables()
    # get_api_data(client, access_token, uid)
    get_fans_api_data(client, access_token, uid)

if __name__ == '__main__':
    main()