# -*- coding: utf-8 -*-
# filename: access.py

import werobot
import requests


def access(url, access_token):
    robot = werobot.WeRoBot(token='fairy1228')
    robot.config['APP_SECRET'] = '20c5db6a7fc44a637ed764fe1b564dd0'
    robot.config['APP_ID'] = 'wx29fe80992e2c7eac'
    client = robot.client

    url = url + access_token
    req = requests.get(url).text
    a = eval(req).get('errcode')
    # print(a)
    # ————————刷新ACCESS_TOKEN——————————
    # 判断ACCESS_TOKEN 是不是 42001 ，是说明过期，需要刷新
    if a == 40001:
        access_token = client.get_access_token()

    return access_token

