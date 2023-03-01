# -*- coding: utf-8 -*-#
# filename: send.py
import web
from template_msg import send_finish_msg, send_failed_msg
from urllib.parse import quote


class Finish(object):
    def POST(self):
        try:
            data = web.input()
            send_finish_msg(data.video_name, quote(data.video_url), data.to_user)
        except Exception as Argment:
            return Argment


class Failed(object):
    def POST(self):
        try:
            data = web.input()
            send_failed_msg(data.video_name, data.failed_reason, data.to_user)
        except Exception as Argment:
            return Argment
