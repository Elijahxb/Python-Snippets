#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-03-29 20:29:29
# @Author  : Elijahxb (xbelijah@gmail.com)
# @Link    : www.junyipan.top:8090
# @Version : 1.0.0

from celery import Celery

app = Celery("Elijahxb's Celery App")
app.config_from_object("apps.celery_app.setting")