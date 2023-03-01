# -*- coding: utf-8 -*-
# filename: template_msg.py

from access import access
import requests
import time


def send_finish_msg(video_name, video_url, to_user):
    ACCESS_TOKEN = "58_t0Vvjhfv6hGMJGnFfEaoZedLOishdqqSy-OMeNSpi7Ns_KfeDpe7-lDGbLHQpy-ZmOh" \
                   "-tm0byo6_Hu9lYXqjKX2q1XqPWjxJtSfPrifguJTkTMCrtEPbGyXhRMqt210348zBm8erlcUqjUvLFWTeADAQHE "

    ACCESS_TOKEN = access(url="https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token=",
                          access_token=ACCESS_TOKEN)

    # ————————发送模板消息——————————————
    ''' touser 是 接收者openid
        template_id 是 模板ID
        url 否 模板跳转链接(海外帐号没有跳转能力)
        miniprogram 否 跳小程序所需数据，不需跳小程序可不用传该数据
        appid 是 所需跳转到的小程序appid(该小程序appid必须与发模板消息的公众号是绑定关联关系，暂不支持小游戏)
        pagepath 否 所需跳转到小程序的具体页面路径，支持带参数,(示例index?foo=bar)，暂不支持小游戏
        data 是 模板数据
        color 否 模板内容字体颜色，不填默认为黑色'''

    push_url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + str(ACCESS_TOKEN)
    t = time.time() - 60 * 60 * 24 * 30
    time_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

    data = {
        "touser": to_user,
        "template_id": "WCdSGiS7iCumtTn7zf_2do-uF06CCSqh_QSMpMNUmbk",
        "url": video_url,
        "miniprogram":{
             "appid":"wx778eeb7a5571e2e5",
             "pagepath":"pages/vdemo?url=" + video_url
           },
        "data": {
            "first": {"value": "视频转换完成！", "color": "#173177"},
            "keyword1": {"value": video_name, "color": "#173177"},
            "keyword2": {"value": "完成：点击详情查看", "color": "#173177"},
            "keyword3": {"value": time_string, "color": "#173177"},
            "remark": {"value": "余额：100次", "color": "#173177"}
        }
    }

    requests.post(url=push_url, json=data)


def send_failed_msg(video_name, failed_reason, to_user):
    access_token = "58_t0Vvjhfv6hGMJGnFfEaoZedLOishdqqSy-OMeNSpi7Ns_KfeDpe7-lDGbLHQpy-ZmOh" \
                   "-tm0byo6_Hu9lYXqjKX2q1XqPWjxJtSfPrifguJTkTMCrtEPbGyXhRMqt210348zBm8erlcUqjUvLFWTeADAQHE "

    access_token = access(url="https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token=",
                          access_token=access_token)

    # ————————发送模板消息——————————————
    push_url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + str(access_token)
    t = time.time() - 60 * 60 * 24 * 30
    time_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

    data = {
        "touser": to_user,
        "template_id": "WCdSGiS7iCumtTn7zf_2do-uF06CCSqh_QSMpMNUmbk",
        "data": {
            "first": {"value": "视频转换失败！", "color": "#173177"},
            "keyword1": {"value": video_name, "color": "#173177"},
            "keyword2": {"value": "失败：" + failed_reason, "color": "#173177"},
            "keyword3": {"value": time_string, "color": "#173177"},
            "remark": {"value": "余额：100次", "color": "#173177"}
        }
    }

    requests.post(url=push_url, json=data)
