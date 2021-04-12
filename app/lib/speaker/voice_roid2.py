import pywinauto
import comtypes
import time

from .base_speaker import BaseSpeaker

class VoiceRoid2(BaseSpeaker):
    """
    VoiceRoid2制御クラス
    """

    # VOICEROID2の起動待ち時間(秒)
    VOICEROID2_START_TIMEOUT = 10

    def __init__(self):
        # インスタンス変数初期化
        self.__voiceroid2_app     = None
        self.__textBoxEditControl = None
        self.__playButtonControl  = None
    
    def start(self, path):
        # VoiceRoid2の起動
        self.__open_voiceroid2(path)

        # VoiceRoid2の制御を取得
        voiceroid2 = self.__search_voiceroid2()

        if voiceroid2:
            # 発声内容入力領域を取得
            self.__textBoxEditControl = self.__get_textBox(voiceroid2)

            # 発声ボタンを取得
            self.__playButtonControl = self.__get_buttons(voiceroid2)

    def stop(self):
        # 発声終了を待つ
        self.speak("")

        # ウィンドウを取得
        mainwin = self.__voiceroid2_app[u'Edit']

        # Alt+F4 を送信
        mainwin.type_keys("%FX")

        # 表示されるダイアログを制御
        try:
            self.__voiceroid2_app['確認']['はい(&Y)Button'].close_click()
        except:
            pass

    def speak(self, text):
        # テキスト登録
        while True:
            try:
                # テキストエリアに入力
                self.__textBoxEditControl.set_edit_text(text)
            except comtypes.COMError:
                # このエラーはテキスト制御のビジーなのでリトライ
                continue
            except AttributeError:
                # 対象オブジェクトが無ければ処理しない
                break
            else:
                # 再生ボタン押下
                self.__playButtonControl.click()
                
                # リトライを抜ける
                break
            finally:
                # 正常/異常ともに1秒Waitする
                time.sleep(1)

    # プライベートメソッド
    def __open_voiceroid2(self, path):
        # VOICEROID2を起動
        # (既に起動済みなら多重起動はされないので考慮とかしない)
        try:
            self.__voiceroid2_app = pywinauto.Application().start(path)
        except pywinauto.application.AppStartError:
            pass

    def __search_voiceroid2(self):
        # デスクトップのエレメント
        parentUIAElement = pywinauto.uia_element_info.UIAElementInfo()

        # 起動時間定義一杯まで起動を待つ
        for i in range(VoiceRoid2.VOICEROID2_START_TIMEOUT):
            del i

            # voiceroidを捜索する
            voiceroid2 = self.__search_child_byname("VOICEROID2", parentUIAElement)

            # *がついている場合
            if voiceroid2 == False:
                voiceroid2 = self.__search_child_byname("VOICEROID2*", parentUIAElement)
            
            # 発見できていればリトライを抜ける
            if voiceroid2 != False:
                break
            else:
                time.sleep(1)
        
        return voiceroid2

    def __search_child_byclassname(self, class_name, uiaElementInfo, target_all = False):
        target = []
        # 全ての子要素検索
        for childElement in uiaElementInfo.children():
            # ClassNameの一致確認
            if childElement.class_name == class_name:
                if target_all == False:
                    return childElement
                else:
                    target.append(childElement)
        if target_all == False:
            # 無かったらFalse
            return False
        else:
            return target

    def __search_child_byname(self, name, uiaElementInfo):
        # 全ての子要素検索
        for childElement in uiaElementInfo.children():
            # Nameの一致確認
            if childElement.name == name:
                return childElement
        # 無かったらFalse
        return False
    
    def __get_textBox(self, voiceroid2):
        # テキスト要素のElementInfoを取得
        TextEditViewEle = self.__search_child_byclassname("TextEditView", voiceroid2)
        textBoxEle      = self.__search_child_byclassname("TextBox", TextEditViewEle)

        # テキストのコントロール返却
        return pywinauto.controls.uia_controls.EditWrapper(textBoxEle)

    def __get_buttons(self, voiceroid2):
        # テキスト領域を取得
        TextEditViewEle = self.__search_child_byclassname("TextEditView", voiceroid2)

        # ボタンを取得
        buttonsEle = self.__search_child_byclassname("Button", TextEditViewEle, target_all = True)

        # 再生ボタンを探す
        playButtonEle = ""
        for buttonEle in buttonsEle:
            # テキストブロックを捜索
            textBlockEle = self.__search_child_byclassname("TextBlock", buttonEle)
            if textBlockEle.name == "再生":
                playButtonEle = buttonEle
                break

        # ボタンコントロールを返却
        return pywinauto.controls.uia_controls.ButtonWrapper(playButtonEle)

# 単体試験
if __name__ == "__main__":
    # VOICEROID2のパス
    path = r"C:\Program Files (x86)\AHS\VOICEROID2\VoiceroidEditor.exe"

    akari = VoiceRoid2()

    akari.start(path)
    akari.speak("私の名前は紲星あかりです。")
    akari.speak("これはPythonからの制御試験です。")

    del akari
