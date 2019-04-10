# -*- coding: UTF-8 -*-

class Fan:
    fanCount = 0

    def __init__(self, id, idstr, screen_name, name, province, city, location, description, url, profile_image_url, profile_url, domain, weihao, gender, followers_count,
                 friends_count, statuses_count, favourites_count, created_at, following, allow_all_act_msg, geo_enabled, verified, verified_type, remark, status_id,
                 allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count, lang, star, mbtype, mbrank, block_word, tags):
        self.id = id
        self.idstr = idstr
        self.screen_name = screen_name
        self.name = name
        self.province = province
        self.city = city
        self.location = location
        self.description = description
        self.url = url
        self.profile_image_url = profile_image_url
        self.profile_url = profile_url
        self.domain = domain
        self.weihao = weihao
        self.gender = gender
        self.followers_count = followers_count
        self.friends_count = friends_count
        self.statuses_count = statuses_count
        self.favourites_count = favourites_count
        self.created_at = created_at
        self.following = following
        self.allow_all_act_msg = allow_all_act_msg
        self.geo_enabled = geo_enabled
        self.verified = verified
        self.verified_type = verified_type
        self.remark = remark
        self.status_id = status_id
        self.allow_all_comment = allow_all_comment
        self.avatar_large = avatar_large
        self.verified_reason = verified_reason
        self.follow_me = follow_me
        self.online_status = online_status
        self.bi_followers_count = bi_followers_count
        self.lang = lang
        self.star = star
        self.mbtype = mbtype
        self.mbrank = mbrank
        self.block_word = block_word
        self.tags = tags
        Fan.fanCount += 1

    # def displayUser(self):
    #     print "id : ", self.id, "idstr: ", self.idstr, "screen_name : ", self.screen_name, "name : ", self.name, "province : ", self.province, "city : ", self.city, "location : ", self.location, \
    #         "description : ", self.description, "url: ", self.url, "profile_image_url: ", self.profile_image_url, "gender : ", self.gender, "followers_count : ", self.followers_count, "friends_count : ", self.friends_count, \
    #         "statuses_count : ", self.statuses_count, "favourites_count : ", self.favourites_count, "tags : ", self.tags