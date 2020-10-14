'''
Author: your name
Date: 2020-10-14 13:08:58
LastEditTime: 2020-10-14 20:33:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /short_url_service/flaskr_service/utils/operate_nosql.py
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis


class ShortUrlStore:
    """store short url data in redis"""

    def __init__(self, token, url='redis://localhost:6379', ttl=7200):
        self.token = token
        self.redis = redis.Redis.from_url(url)
        self.ttl = ttl

    def set(self, key, value):
        self.refresh()
        return self.redis.hset(self.token, key, value)

    def get(self, key, value):
        self.refresh()
        return self.redis.hget(self.token, key)

    def incr(self, key):
        self.refresh()
        return self.redis.hincrby(self.token, key, 1)

    def refresh(self):
        self.redis.expire(self.token, self.ttl)
