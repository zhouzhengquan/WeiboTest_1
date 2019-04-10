# -*- coding: UTF-8 -*-

class Weibo:
    '所有微博的基类'
    wbCount = 0

    def __init__(self, created_at,  id, text, source, favorited, truncated, in_reply_to_status_id,in_reply_to_user_id,
in_reply_to_screen_name, mid, reposts_count, comments_count,user):
        self.created_at = created_at
        self.id = id
        self.text = text
        self.source = source
        self.favorited = favorited
        self.truncated = truncated
        self.in_reply_to_status_id = in_reply_to_status_id
        self.in_reply_to_user_id = in_reply_to_user_id
        self.in_reply_to_screen_name = in_reply_to_screen_name
        self.mid = mid
        self.reposts_count = reposts_count
        self.comments_count = comments_count
        self.user = user
        Weibo.wbCount += 1

    # def displayWeibo(self):
    #     print "author : ", self.author, ", created_at: ", self.created_at, ", id: ", self.id, ", text: ", self.text