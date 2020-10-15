#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import session, redirect, escape, request, render_template, url_for, jsonify, current_app
from flask import render_template
from flask_api import status
from functools import wraps
from utils.short_uuid import get_short_uuid, set_redis_value
from utils.operate_nosql import RedisObj


def login_require(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        username = request.args.get("username")
        password = request.args.get("password")
        if username == "test1" and password == "test1":
            return fn(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper


# just an example
def login():
    return "login page"


def home_page():
    if request.method == "GET":
        return render_template("index.tmpl")


# @login_require
def short_service():
    if request.method == "POST":
        req_data = request.get_json(cache=False, silent=True)
        if req_data:
            long_url_value = req_data["url"]
            redis_instance = RedisObj(token="")
            short_url_key = get_short_uuid(redis_instance)
            set_status = set_redis_value(
                redis_instance, short_url_key, long_url_value)
            print(set_status)
            # 待确认返回状态嘛

            if set_status:
                return jsonify({"value": short_url_key})
        else:
            return "bad request", status.HTTP_400_BAD_REQUEST

# curl -i -H "Content-Type: application/json" -X POST -d '{"url": "https://www.baidu.com"}' http://182.254.247.157:5000/short_service
