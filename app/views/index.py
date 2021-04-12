from app.application import app
from app.services.index_service import get_request, post_request
from flask import Blueprint, request

POST = "POST"
GET = "GET"

bp_index = Blueprint("index", __name__)

@bp_index.route("/", methods=[GET, POST])
def index():
    """
    VoiceRoDoKuのGUI画面

    Parameters
    ----------
    request : request
        リクエスト情報

    Returns
    -------
    Text
        htmlの文字列
    """

    app.logger.info(request.method + " Access from [" + request.remote_addr + "]")

    if request.method == POST:
        html = post_request(request)
    else:
        html = get_request(request)

    return html
