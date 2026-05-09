#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8489579070:AAHGrY14mbQd6F3mNfzyz3bZUz8hDsXWWts")
    API_ID = int(os.environ.get("API_ID", "31169764"))
    API_HASH = os.environ.get("API_HASH", "a2c20bda0ee2113467c8c229663f97f6")
    AUTH_USERS = "1411895712"

