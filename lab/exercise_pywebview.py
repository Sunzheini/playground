import os
import sys
import time
from threading import Thread
import webview


def start_webview():
    window = webview.create_window('erp-demo',
                                   # 'http://localhost:8000/',
                                   'https://erp-demo.herokuapp.com/',
                                   confirm_close=True,
                                   width=1920,
                                   height=1200,
                                   )
    webview.start()
    window.closed = os._exit(0)


def start_startdjango():
    if sys.platform in ['win32', 'win64']:
        os.system("python manage.py runserver {}:{}".format('127.0.0.1', '8000'))
        # time.sleep(10)
    else:
        os.system("python3 manage.py runserver {}:{}".format('127.0.0.1', '8000'))
        # time.sleep(10)


if __name__ == '__main__':
    # Thread(target=start_startdjango).start()
    start_webview()
