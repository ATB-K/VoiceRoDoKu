# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
from .base_reader import BaseReader

class ArcadiaReader(BaseReader):
    """
    Arcadia
    """

    URL = "http://www.mai-net.net/"
    URL_S = "https://www.mai-net.net/"

    def __init__(self):
        pass
    
    def __del__(self):
        pass

    @classmethod
    def is_this_novel(self, url):
        if ArcadiaReader.URL in url:
            return True
        if ArcadiaReader.URL_S in url:
            return True

        return False

    def get_episode_list(self, url):
        # htmlを取得
        html = request.urlopen(url)

        # htmlをパース
        soup = BeautifulSoup(html, "html.parser")

        # リストの要素抽出
        episode = soup.find('table', {'id': 'table'})

        # 抽出要素をhtml文書として再度パースする
        soup = BeautifulSoup(str(episode), "html.parser")

        # 文章を行ごとに取得
        ep_list = []
        element = soup.find_all("a")
        for i in element:
            ep_list.append([i.string, self.URL + i.get("href")])
        
        # 1話題名を少説名に設定
        self.NOVEL_TITLE = ep_list[0][0]
        
        return ep_list

    def get_episode(self, url):
        # htmlを取得
        html = request.urlopen(url)

        # htmlをパース
        soup = BeautifulSoup(html, "html.parser")

        # 本文の要素抽出
        episode = soup.find('blockquote')

        # 抽出要素をhtml文書として再度パースする
        soup = BeautifulSoup(str(episode), "html.parser")

        # 文章を行ごとに取得
        strings = []
        element = soup.getText().split("。")
        for i in element:
            strings.append(i.replace('\n',''))
        
        return strings

# 単体試験
if __name__ == "__main__":
    # 対象判定
    if ArcadiaReader.is_this_novel(""):
        print(True)

    reader = ArcadiaReader()

    # 文章取得
    episode = reader.get_episode("")
    for i in episode:
        print(i)

    # 小説一覧取得
    episode_list = reader.get_episode_list("")
    for i in episode_list:
        print(i)

