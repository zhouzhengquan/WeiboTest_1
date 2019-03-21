# -*- coding: utf-8 -*-
import sqlite
from weibo import APIClient

import webbrowser  # python内置的包

# #粉丝模块
def get_fans_api_data(client):
    #1.获取全部粉丝数、关注数、微博数
    counts = client.users__counts(uids=7029702604L)
    print counts
    #2.获取一段时间新增粉丝，需商业API
    #3.获取粉丝个人信息
    #3.1获取粉丝列表
    friends = client.friendships__followers(uid=7029702604L)
    print friends
    #3.2获取粉丝个人信息
    length =len(friends['users'])
    for i in range(0, length):
        info = client.users__show(['friends']['users']['id'])
        print info

    #4.获取粉丝感兴趣的标签
    #4.1获取粉丝列表，4.2获取粉丝标签为商业API，不可用
    friends = client.friendships__followers(uid=7029702604L)
    print friends


#微博模块
def get_weibos_api_data(client):
    #1.获取当前用户发布的微博
    # uid = 7029702604L
    # items = client.statuses.user_timeline.get(uid = 7029702604L)
    # for i in range(0, len(items.statuses)):
    #
    #     created_at = items.statuses[i]['created_at']
    #     id = items.statuses[i]['id']
    #     text = items.statuses[i]['text']
    #     sqlite.insert_weibo(uid, created_at, id, text)
    #     print u'微博：' + items.statuses[i]['text']

    # #2.获取单个微博转发情况
    # ids = client.statuses.user_timeline.ids.get()['statuses']
    # print ids

    report_items = client.statuses.repost_timeline.get(id=4265317284622515)
    print report_items
    #3.获取单个微博评论
    # print client.statuses.comments__show(id=4349409951039337)
    # for i in range(0, len(comments)):
    #     print u'微博评论：' + comments[i]['text']


    #4.获取账号下所有评论
    uid = 7029702604L
    comments2 = client.comments__to_me()['comments']
    for i in range(0, len(comments2)):
        created_at = comments2[i]['created_at']
        id = comments2[i]['id']
        text = comments2[i]['text']
        sqlite.insert_comment(uid, created_at, id, text)
        print u'微博评论：' + comments2[i]['text']

def main():
    APP_KEY = '2930531009'  # 注意替换这里为自己申请的App信息
    APP_SECRET = '34f8328dcfa4f1f5b0bdd982f34e2038'
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
    # r = client.request_access_token(code)
    # access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
    # expires_in = r.expires_in
    # print "access_token: ", access_token
    # print "expires_in: ", expires_in

    access_token = '2.00EmujfHLzM1MD53800b9de8pKSjtD'
    expires_in = '1710752419'
    # 设置得到的access_token
    client.set_access_token(access_token, expires_in)

    # sqlite.create_table(cursor)

    # get_fans_api_data(client)
    get_weibos_api_data(client)



if __name__ == '__main__':
    main()