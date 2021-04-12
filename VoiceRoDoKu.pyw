import threading

import requests
import webview

from app.application import CMD_SHUTDOWN, app
from app.lib.www import *

# GUIのURL
ROOT_URL = "http://" + app.config["SERVER_IP"] + ":" + app.config["SERVER_PORT"] + "/"

def start_flask():
    """
    Flaskのサーバを起動
    """

    app.run(host=app.config["SERVER_IP"], port=app.config["SERVER_PORT"])

def close_window():
    """
    閉じるボタン押下時の処理
    """

    # 停止コマンド送信
    requests.post(ROOT_URL, data=CMD_SHUTDOWN.encode("utf-8"))

if __name__ == "__main__":
    try:
        # 別スレッドでサーバ起動
        threading.Thread(target=start_flask).start()

        # GUI定義
        window = webview.create_window('VoiceRoDoKu', ROOT_URL, width=app.config["WIDTH"], height=app.config["HEIGHT"])

        # 閉じる処理追加
        window.closing += close_window

        # GUI起動
        webview.start(gui="cef")

    except Exception as e:
        import traceback
        traceback.print_exc()
