from app.application import CMD_SHUTDOWN, CMD_START, CMD_STOP, CMD_URL, app
from app.lib.common_reader import Reader
from app.services.speak_service import start_speak, stop_speak
from flask import render_template


def post_request(request):
    """
    POSTリクエスト処理

    Parameters
    ----------
    request : request
        リクエスト情報

    Returns
    -------
    String
        html情報
    """

    html = ""

    post_value = request.get_data().decode('utf-8')

    # ノベル一覧取得
    if CMD_URL in post_value:
        app.logger.info("Command = [" + CMD_URL + "]")

        # value取得
        url = post_value.split("===")

        reader = Reader(url[-1])

        # 小説のエピソード一覧を取得
        novels = reader.get_episode_list(url[-1])

        # 小説タイトルを取得
        title = reader.get_title()

        html = render_template("NovelList.html", title=title, novel=novels)

    # 小説読み上げ開始
    if CMD_START in post_value:
        app.logger.info("Command = [" + CMD_START + "]")

        # value取得
        url = post_value.split("===")

        start_speak(url[-1])

    # 小説読み上げ停止
    if CMD_STOP in post_value:
        app.logger.info("Command = [" + CMD_STOP + "]")

        stop_speak()

    # シャットダウン要求
    if CMD_SHUTDOWN in post_value:
        app.logger.info("Command = [" + CMD_SHUTDOWN + "]")

        showtdown(request)

    return html

def get_request(request):
    """
    GETリクエスト処理

    Parameters
    ----------
    request : request
        リクエスト情報

    Returns
    -------
    String
        html情報
    """
    
    return render_template("VoiceRoDoKu.html")

def showtdown(request):
    """
    シャットダウン処理

    Parameters
    ----------
    request : request
        リクエスト情報

    Returns
    -------
    None
        なし
    """

    func = request.environ.get('werkzeug.server.shutdown')

    if func is None:
        app.logger.error("showtdown fail")
        raise RuntimeError('Not running with the Werkzeug Server')
    else:
        app.logger.info("showtdown Done")
        func()
