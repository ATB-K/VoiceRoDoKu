from app.application import app
from app.lib.config import VOICEROID2, Config
from app.lib.speaker.voice_roid2 import VoiceRoid2

# コンフィグ読み込み
__conf = Config()

# 現在有効な設定
ACTIVE = __conf.active

# 音声ソフト定義
SPEKER_LIST = [
    [VOICEROID2, VoiceRoid2(), __conf.voiceroid2] # VOICEROID2制御処理
]

class Speaker:
    """
    読み上げオブジェクトの抽象化クラス
    """

    def __init__(self):
        for item in SPEKER_LIST:
            if item[0] in ACTIVE:
                self.speaker = item[1] # 読み上げオブジェクト取得
                self.value   = item[2] # configの設定値を取得
                break # elseに入らない
        else:
            app.logger.error("search speaker failure. Active -> [" + ACTIVE + "]" )
    
    def start(self):
        self.speaker.start(self.value)

    def speak(self, text):
        self.speaker.speak(text)
    
    def stop(self):
        self.speaker.stop()
