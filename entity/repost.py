# -*- coding: UTF-8 -*-

class Repost:
    '所有转发的基类'
    repCount = 0

    def __init__(self, author, created_at, id, text, source, favorited, truncated, in_reply_to_status_id,
                 in_reply_to_user_id,in_reply_to_screen_name, mid, reposts_count, comments_count, user, retweeted_status):
        self.author = author
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
        self.retweeted_status = retweeted_status
        Repost.repCount += 1

    def displayRepost(self):
        print "author : ", self.author,", created_at: ", self.created_at, ", id: ", self.id, ", text: ", self.text,\
            "source : ", self.source,", favorited: ", self.favorited, ", truncated: ", self.truncated, ", in_reply_to_status_id: ", self.in_reply_to_status_id,\
            "in_reply_to_user_id : ", self.in_reply_to_user_id,", in_reply_to_screen_name: ", self.in_reply_to_screen_name, ", mid: ", self.mid, ", reposts_count: ", self.reposts_count,\
            "comments_count : ", self.comments_count,", user: ", self.user, ", retweeted_status: ", self.retweeted_status
