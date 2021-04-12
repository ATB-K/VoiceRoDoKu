# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class BaseSpeaker(metaclass = ABCMeta):
    """
    読み上げオブジェクトのベースクラス
    """

    @abstractmethod
    def start(self, path):
        """
        読み上げソフトの起動処理を行う

        Parameters
        ----------
        path : String
            読み上げソフトウェアへの設定値

        Returns
        -------
        None
            なし
        """
        pass

    @abstractmethod
    def stop(self):
        """
        読み上げソフトの終了処理を行う

        Parameters
        ----------
        None
            なし

        Returns
        -------
        None
            なし
        """
        pass

    @abstractmethod
    def speak(self, text):
        """
        文章を読み上げる

        Parameters
        ----------
        text : String
            読み上げる文章

        Returns
        -------
        None
            なし
        """
        pass