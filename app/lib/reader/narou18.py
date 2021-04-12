# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from .base_reader import BaseReader

class Narou18Reader(BaseReader):
    """
    ノクターン・ミッドナイト・ムーンライト
    """

    URL = "http://novel18.syosetu.com/"
    URL_S = "https://novel18.syosetu.com/"

    COOKIE = {'over18' : 'yes'} 
    HEADERS = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}

    def __init__(self):
        pass
    
    def __del__(self):
        pass

    @classmethod
    def is_this_novel(self, url):
        if Narou18Reader.URL in url:
            return True
        if Narou18Reader.URL_S in url:
            return True

        return False

    def get_episode_list(self, url):
        # htmlを取得
        html = requests.get(url=url, headers=self.HEADERS, cookies=self.COOKIE).content

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
                ep_list.append([i.string, self.URL_S + i.get("href")])
        else:
            # 短編小説の場合
            ep_list.append([self.NOVEL_TITLE, url])
        
        return ep_list

    def get_episode(self, url):
        # htmlを取得
        html = requests.get(url=url, headers=self.HEADERS, cookies=self.COOKIE).content

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
    if Narou18Reader.is_this_novel(""):
        print(True)

    reader = Narou18Reader()

    # 文章取得
    episode = reader.get_episode("")
    for i in episode:
        print("[" + i.string + "]")

    # 小説一覧取得
    episode_list = reader.get_episode_list("")
    for i in episode_list:
        print(i)