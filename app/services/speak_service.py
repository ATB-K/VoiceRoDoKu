import ctypes
from multiprocessing import Value

from app.application import app
from app.lib.common_reader import Reader
from app.lib.common_speaker import Speaker

# 定数
ALIVE = 1
KILL = 0

# グローバル変数
READER  = Value(typecode_or_type=ctypes.c_int64)
SPEAKER = Value(typecode_or_type=ctypes.c_int64)
READER = KILL
SPEAKER = KILL

def start_speak(url):
    """
    読み上げ開始処理

    Parameters
    ----------
    url : String
        リクエスト情報

    Returns
    -------
    None
        なし
    """

    global READER
    global SPEAKER

    if READER == ALIVE:
        app.logger.warn("Already Start")
        return
    else:
        app.logger.info("Start Speaker")

    # 小説読み上げ・VR2の起動を記録
    READER = ALIVE
    SPEAKER = ALIVE

    reader = Reader(url)

    speaker = Speaker()
    
    speaker.start()

    # 文章を取得
    context = reader.get_episode(url)

    # 読み上げ処理
    for text in context:
        if READER == ALIVE:
            speaker.speak(text)
        else:
            app.logger.warn("Stop Interrupt")
            break
    else:
        READER = KILL

    # 停止処理
    speaker.stop()

    # VR2の停止を記録
    SPEAKER = KILL

    app.logger.info("End Speaker")

def stop_speak():
    """
    読み上げ終了処理

    Parameters
    ----------
    None
        なし

    Returns
    -------
    None
        なし
    """

    global READER
    global SPEAKER

    # 小説読み上げの停止
    READER = KILL
