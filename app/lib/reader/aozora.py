# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
from .base_reader import BaseReader

class AozoraReader(BaseReader):
    """
    青空文庫
    """

    URL = "http://www.aozora.gr.jp/"
    URL_S = "https://www.aozora.gr.jp/"

    def __init__(self):
        pass
    
    def __del__(self):
        pass

    @classmethod
    def is_this_novel(self, url):
        if AozoraReader.URL in url:
            return True
        if AozoraReader.URL_S in url:
            return True

        return False

    def get_episode_list(self, url):
        # htmlを取得
        html = request.urlopen(url)

        # htmlをパース
        soup = BeautifulSoup(html, "html.parser")

        # 小説名を記録
        title = soup.find('h1', {'class': 'title'})
        self.NOVEL_TITLE = title.string

        # リストの要素抽出
        episode = soup.find('div', {'class': 'index_box'})

        # 抽出要素をhtml文書として再度パースする
        soup = BeautifulSoup(str(episode), "html.parser")

        # 文章を行ごとに取得
        ep_list = []
        element = soup.find_all("a")
        for i in element:
            ep_list.append([i.string, self.URL + i.get("href")])
        
        return [[self.NOVEL_TITLE, url]]

    def get_episode(self, url):
        # htmlを取得
        html = request.urlopen(url)

        # htmlをパース
        soup = BeautifulSoup(html, "html.parser")

        # ルビが振られた漢字を削除(ルビだけ残す)
        for tag in soup.findAll(["rb"]):
            # タグとその内容の削除
            tag.decompose()

        # 本文の要素抽出
        episode = soup.find('div', {'class': 'main_text'})

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
    if AozoraReader.is_this_novel(""):
        print(True)

    # 文章取得
    reader = AozoraReader()

    episode = reader.get_episode("")
    for i in episode:
        print(i)

    # 小説一覧取得
    episode_list = reader.get_episode_list("")
    for i in episode_list:
        print(i)
