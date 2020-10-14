#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import secrets
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from flask import Flask, session, redirect, escape, request

app = Flask(__name__)
app.secret_key = secrets.token_hex(24)

# init data
with open("config.yml", "r", encoding="utf-8") as f:
    configs = load(f, Loader=Loader)

REDIS_URL = configs.get("REDIS_URL")
TOKEN = configs.get("TOKEN")
