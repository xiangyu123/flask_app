#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
from flask import current_app


class RedisObj:
    """store short url data in redis"""

    def __init__(self, token="", ttl=7200):
        self.token = token
        self.redis = redis.Redis(**current_app.config.get("REDIS_DB_URL"))
        self.ttl = ttl

    def set(self, key, value):
        self.refresh(key)
        return self.redis.setex(key, self.ttl, value)
        # return self.redis.setex(self.token, key, self.ttl, value)

    def get(self, key):
        self.refresh(key)
        return self.redis.get(key)
        # return self.redis.get(self.token, key)

    def exist(self, key):
        return self.redis.exists(key)
        # return self.redis.exists(self.token, key)

    def refresh(self, key):
        self.redis.expire(self.token, self.ttl)
        # self.redis.expire(self.token, self.ttl)


# try:
#     #host is the redis host,the redis server and client are required to open, and the redis default port is 6379
#     pool = redis.ConnectionPool(host='10.0.64.113', password = 'xxxxx', port=6379, db=3)
#     print("connected success.")
# except:
#     print("could not connect to redis.")
# r = redis.Redis(connection_pool=pool)
