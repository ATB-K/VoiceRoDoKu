import configparser

ACTIVE = "Active"
VOICEROID2 = "VoiceRoid2"
SP_VOICE = "SpVoice"
SOFTALK = "Softalk"

SELECT = "Select"
PATH = "Path"

class Config:
    """
    設定情報を保持する。

    Attributes
    ----------
    active : String
        有効な音声設定
    voiceroid2 : String
        voiceroid2へのパス
    spvoice : String
        spvoiceの選択名
    softalk : String
        softalkへのパス
    """

    def __init__(self):
        config = configparser.RawConfigParser()

        config.read('config.ini')

        # 有効な設定
        self.active = config.get(ACTIVE, SELECT)

        # VoiceRoid2
        self.voiceroid2 = config.get(VOICEROID2, PATH)

        # SpVoice
        self.spvoice = config.get(SP_VOICE, SELECT)

        # Softalk
        self.softalk = config.get(SOFTALK, PATH)

        self.config = config

    def save(self):

        config = self.config

        # 有効な設定
        config.set(ACTIVE, SELECT, self.active)

        # VoiceRoid2
        config.set(VOICEROID2, PATH, self.voiceroid2)

        # SpVoice
        config.set(SP_VOICE, SELECT, self.spvoice)

        # Softalk
        config.set(SOFTALK, PATH, self.softalk)

        with open('config.ini', 'w') as file:
            self.config.write(file)

if __name__ == "__main__":
    conf = Config()

    print(conf.active)
    print(conf.voiceroid2)

    conf.save()
