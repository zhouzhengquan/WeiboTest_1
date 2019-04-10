# -*- coding: UTF-8 -*-

class User:
    userCount = 0

    def __init__(self, id, screen_name, name, province, city, location, description , url, profile_image_url, domain, gender, followers_count, friends_count, statuses_count,
favourites_count, created_at, following ,c , geo_enabled, verified, status, allow_all_comment, avatar_large, verified_reason, follow_me, online_status, bi_followers_count):
        self.id = id
        self.screen_name = screen_name
        self.name = name
        self.province = province
        self.city = city
        self.location = location
        self.description = description
        self.url = url
        self.profile_image_url = profile_image_url
        self.domain = domain
        self.gender = gender
        self.followers_count = followers_count
        self.friends_count = friends_count
        self.statuses_count = statuses_count
        self.favourites_count = favourites_count
        self.created_at = created_at
        self.following = following
        self.c = c
        self.geo_enabled = geo_enabled
        self.verified = verified
        self.status = status
        self.allow_all_comment = allow_all_comment
        self.avatar_large = avatar_large
        self.verified_reason = verified_reason
        self.follow_me = follow_me
        self.online_status = online_status
        self.bi_followers_count = bi_followers_count
        User.userCount += 1

    # def displayUser(self):
    #     print "id : ", self.id, "screen_name : ", self.screen_name, "name : ", self.name, "province : ", self.province, "city : ", self.city, "location : ", self.location, \
    #         "description : ", self.description, "gender : ", self.gender, "followers_count : ", self.followers_count, "friends_count : ", self.friends_count, \
    #         "statuses_count : ", self.statuses_count, "favourites_count : ", self.favourites_count, "tags : ", self.tags