# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
from send import Finish
from send import Failed

urls = (
    '/wx', 'Handle',
    '/wx/finish', 'Finish',
    '/wx/failed', 'Failed'
)


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

