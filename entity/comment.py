# -*- coding: UTF-8 -*-

class Comment:
    '所有评论的基类'
    cmtCount = 0

    def __init__(self, created_at, id, text, source, mid, user, cmtUid, status):
        self.created_at = created_at
        self.id = id
        self.text = text
        self.source = source
        self.mid = mid
        self.user = user
        self.cmtUid = cmtUid
        self.status = status
        Comment.cmtCount += 1

    def displayComment(self):
        print "created_at: ", self.created_at, ", id: ", self.id, ", text: ", self.text, ', source: ', self.source, ', mid: ', self.mid, ', user: ', self.user,
        ', cmtUid: ', self.cmtUid, ', status: ', self.status