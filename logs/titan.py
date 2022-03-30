#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-03-31 01:04:13
# @Author  : Elijahxb (xbelijah@gmail.com)
# @Link    : www.junyipan.top:8090
# @Version : 1.0.0
import logging
from functools import cached_property


class Titan(object):
    @cached_property
    def Platform():
        logger = logging.getLogger("Platform")