# -*- coding: utf-8 -*-#
# filename: handle.py

import reply
import receive
import web
import mail

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            #后台打日志
            recMsg = receive.parse_xml(webData)

            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                mail.send_mail(recMsg.FromUserName, recMsg.Content)
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = '已发送'
                replyMsg = reply.TextMsg(toUser, fromUser, content)

                return replyMsg.send()
            else:
                print("暂且不处理")
                return "success"

        except Exception as Argment:
            return Argment

