# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractclassmethod, abstractmethod

class BaseReader(metaclass = ABCMeta):
    """
    小説オブジェクトのベースクラス
    """

    NOVEL_TITLE = ""
    
    @abstractclassmethod
    def is_this_novel(self, url):
        """
        URLから自オブジェクトが処理すべきか判定する

        Parameters
        ----------
        url : String
            小説 or 小説一覧へのURL

        Returns
        -------
        bool
            判定結果
                true:自オブジェクトが処理する
                false:自オブジェクトは対象でない
        """
        pass

    @abstractmethod
    def get_episode_list(self, url):
        """
        URLからエピソード一覧を取得する

        Parameters
        ----------
        url : String
            小説一覧へのURL

        Returns
        -------
        list(list)
            [[エピソード名, URL文字列],...]
        """
        pass

    @abstractmethod
    def get_episode(self, url):
        """
        URLからエピソード内容を取得する

        Parameters
        ----------
        url : String
            小説へのURL

        Returns
        -------
        list
            句読点単位で分割した小説の本文
        """
        pass