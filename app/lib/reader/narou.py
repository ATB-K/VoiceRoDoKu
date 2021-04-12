# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
from .base_reader import BaseReader

class NarouReader(BaseReader):
    """
    小説家になろう
    """

    URL = "http://ncode.syosetu.com"
    URL_S = "https://ncode.syosetu.com"

    def __init__(self):
        pass
    
    def __del__(self):
        pass

    @classmethod
    def is_this_novel(self, url):
        if NarouReader.URL in url:
            return True
        if NarouReader.URL_S in url:
            return True

        return False

    def get_episode_list(self, url):
        # htmlを取得
        html = request.urlopen(url)

        # htmlをパース
        soup = BeautifulSoup(html, "html.parser")

        # 小説名を記録
        title = soup.find('p', {'class': 'novel_title'})
        self.NOVEL_TITLE = title.string

        # リストの要素抽出
        episode = soup.find('div', {'class': 'index_box'})

        ep_list = []
        if episode != None:
            # 抽出要素をhtml文書として再度パースする
            soup = BeautifulSoup(str(episode), "html.parser")

            # 文章を行ごとに取得
            element = soup.find_all("a")
            for i in element:
                ep_list.append([i.string, self.URL + i.get("href")])
        else:
            # 短編小説の場合
            ep_list.append([self.NOVEL_TITLE, url])
        
        return ep_list

    def get_episode(self, url):
        # htmlを取得
        html = request.urlopen(url)

        # htmlをパース
        soup = BeautifulSoup(html, "html.parser")

        # なろう本文の要素抽出
        episode = soup.find('div', {'id': 'novel_honbun'})

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
    if NarouReader.is_this_novel(""):
        print(True)

    reader = NarouReader()

    # 文章取得
    episode = reader.get_episode("")
    for i in episode:
        print("[" + i.string + "]")

    # 小説一覧取得
    episode_list = reader.get_episode_list("")
    for i in episode_list:
        print(i)