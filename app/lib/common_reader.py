from app.application import app
from app.lib.reader.aozora import AozoraReader
from app.lib.reader.arcadia import ArcadiaReader
from app.lib.reader.hameln import HamelnReader
from app.lib.reader.kakuyomu import KakuyomuReader
from app.lib.reader.narou import NarouReader
from app.lib.reader.narou18 import Narou18Reader

# Reader定義
READER_LIST = [
    AozoraReader,    # 青空文庫
    ArcadiaReader,   # Arcadia
    HamelnReader,    # ハーメルン
    KakuyomuReader,  # カクヨム
    NarouReader,     # 小説家になろう
    Narou18Reader,   # ノクターン・ミッドナイト・ムーンライト
]

class Reader:
    """
    小説オブジェクトの抽象化クラス
    """

    def __init__(self, url):
        for reader in READER_LIST:
            if reader.is_this_novel(url):
                self.reader = reader()
                break # elseに入らない
        else:
            app.logger.error("search reader failure. url -> [" + url + "]")
    
    # 小説タイトル取得
    def get_title(self):
        return self.reader.NOVEL_TITLE

    # 小説一覧取得
    def get_episode_list(self, url):
        # エピソード一覧取得
        novels = self.__get_episode_list(url)

        return self.__to_map_list(novels)

    # 小説本文取得
    def get_episode(self, url):
        return self.reader.get_episode(url)

    # 小説エピソード一覧取得
    def __get_episode_list(self, url):
        return self.reader.get_episode_list(url)

    # 小説一覧画面生成
    def __to_map_list(self, novelList):
        novels = list()
        for episode in novelList:
            dic = dict()
            dic["name"] = episode[0] # エピソード名称
            dic["url"] = episode[1]  # 参照URL
            novels.append(dic)

        return novels
