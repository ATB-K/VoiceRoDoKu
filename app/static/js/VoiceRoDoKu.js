// 口パク処理変数
var isChangeFace

// 読み込み完了時イベント
window.onload = function () {
    chengeMargin();
    loadingDone();
};

// ウィンドウサイズ変更イベント
window.addEventListener("resize", function(event) {
    chengeMargin();
});

// 動的サイズ変更
function chengeMargin() {
    // コントロール部のマージン変更
    p_width = document.getElementById("character").clientWidth;
    document.getElementById("disp-control").style.marginLeft = (p_width + "px");

    // 小説リスト高さ変更
    l_height = document.getElementById("character").clientHeight;
    document.getElementById("select-novel").style.height = ((l_height - 138) + "px");
}

// 読み込み完了処理
function loadingDone() {
    const spinner = document.getElementById('loading');
    spinner.classList.add('loaded');
}

// 乱数生成
function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

// 表情切り替え
function changeFace(){
    var pics_src = new Array("/static/images/akari-a.png","/static/images/akari-he.png","/static/images/akari-hu.png");
    document.getElementById("character").src = pics_src[getRandomInt(3)];
}

// 口パク処理開始
function startSpeak() {
    isChangeFace = setInterval(changeFace, 400);
}

// 口パク処理終了
function stopSpeak() {
    clearTimeout(isChangeFace);
    document.getElementById("character").src = "/static/images/akari-mu.png";
}

// GETボタン押下時
function btnGet() {
    // URLを取得
    url = document.getElementById("novel-url").value;
    if (url != "") {
        getNovel(url);
    }
}

// 各エピソード選択時
function btnEpisode(btn) {
    // 現在の選択行を取得
    current = document.getElementsByClassName("active");

    // 現在の選択行を削除
    [].forEach.call(current, function(elem) {
        elem.classList.remove('active');
    })

    // 選択行を更新
    btn.classList.add("active");
}

// STARTボタン押下時
function btnStart() {
    // 選択行を取得
    current = document.getElementsByClassName("active");

    // 隠し項目のURLを取得
    url = current[0].children[0].value;

    // 口パク処理開始
    startSpeak();

    // Flaskへコマンド送信
    sendControl("START===" + url);
}

// STOPボタン押下時
function btnStop() {
    // 口パク処理終了
    stopSpeak();

    // Flaskへコマンド送信
    sendControl("STOP");
}

// 小説一覧リクエスト処理
function getNovel(url) {
    xhr = new XMLHttpRequest();
    xhr.open('POST', location.href, true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    xhr.send("URL" + "===" + url);

    // 応答データ処理
    xhr.onreadystatechange = function() {
        if(xhr.readyState === 4 && xhr.status === 200) {
            // URL欄をクリア
            document.getElementById("novel-url").value = "";

            // 取得htmlを反映
            document.getElementById('novel-list').innerHTML = xhr.responseText;

            // 小説タイトル設定
            title = document.getElementById('novel-title').value;
            document.getElementById('title').innerText = title;
        }
    }
}

// 操作コマンドを送信
function sendControl(msg) {
    xhr = new XMLHttpRequest();
    xhr.open('POST', location.href, true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    xhr.send(msg);

    // 応答データ処理
    xhr.onreadystatechange = function() {
        if(xhr.readyState === 4 && xhr.status === 200) {
            // 何もしない
        }
    }
}