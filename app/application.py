from flask import Flask

from app.lib.logger import server_handler

# Flask
app = Flask(__name__, instance_relative_config=True)

# 標準設定ファイル読み込み
app.config.from_object("setting")

# ロガー設定
app.logger.addHandler(server_handler())

# アプリ内定義
CMD_SHUTDOWN = "SHUTDOWN"
CMD_START = "START"
CMD_STOP = "STOP"
CMD_URL = "URL"
