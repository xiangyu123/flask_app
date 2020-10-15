#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import secrets
import views.views as views
from flask import Flask
from werkzeug.utils import import_string
from config import ProductionConfig


# configure Flask app
def create_app():
    app = Flask(__name__)
    cfg = import_string('config.ProductionConfig')()
    app.config.from_object(cfg)

    app.secret_key = secrets.token_hex(24)

    app.add_url_rule("/index", view_func=views.home_page)
    app.add_url_rule("/login", view_func=views.login)
    app.add_url_rule("/short_service",
                     view_func=views.short_service, methods=["POST"])

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
