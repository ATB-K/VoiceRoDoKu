# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
from .base_reader import BaseReader

class KakuyomuReader(BaseReader):
    """
    カクヨム
    """

    URL = "http://kakuyomu.jp/"
    URL_S = "https://kakuyomu.jp/"

    def __init__(self):
        pass
    
    def __del__(self):
        pass

    @classmethod
    def is_this_novel(self, url):
        if KakuyomuReader.URL in url:
            return True
        if KakuyomuReader.URL_S in url:
            return True

        return False

    def get_episode_list(self, url):
        # htmlを取得
        html = request.urlopen(url)

        # htmlをパース
        soup = BeautifulSoup(html, "html.parser")

        # 小説名を記録
        title = soup.find('li', {'class': 'widget-toc-chapter'})
        self.NOVEL_TITLE = title.get_text().replace('\n','')

        # リストの要素抽出
        episode = soup.find('ol', {'class': 'widget-toc-items'})

        # 抽出要素をhtml文書として再度パースする
        soup = BeautifulSoup(str(episode), "html.parser")

        # 文章を行ごとに取得
        ep_list = []
        element = soup.find_all('a')
        for i in element:
            ep_list.append([i.get_text().replace('\n',''), self.URL + i.get("href").lstrip("/")])
        
        return ep_list

    def get_episode(self, url):
        # htmlを取得
        html = request.urlopen(url)

        # htmlをパース
        soup = BeautifulSoup(html, "html.parser")

        # なろう本文の要素抽出
        episode = soup.find('div', {'class': 'widget-episodeBody'})

        # 抽出要素をhtml文書として再度パースする
        soup = BeautifulSoup(str(episode), "html.parser")

        # 文章を行ごとに取得
        strings = []
        element = soup.find_all("p")
        for i in element:
            if i.string != None:
                strings.append(i.string)
        
        return strings

# 単体試験
if __name__ == "__main__":
    # 対象判定
    if KakuyomuReader.is_this_novel(""):
        print(True)

    reader = KakuyomuReader()

    # 文章取得
    episode = reader.get_episode("")
    for i in episode:
        print("[" + i.string + "]")

    # 小説一覧取得
    episode_list = reader.get_episode_list("")
    for i in episode_list:
        print(i)
