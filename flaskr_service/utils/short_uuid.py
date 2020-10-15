#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
import shortuuid


def get_short_uuid(redis_obj):
    while True:
        short_uuid = shortuuid.encode(uuid.uuid4())[:7]
        if redis_obj.exist(short_uuid):
            continue
        return short_uuid


def set_redis_value(redis_obj, key, value):
    redis_obj.set(key, value)
