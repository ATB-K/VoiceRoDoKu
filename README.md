# VoiceRoDoKu

## 説明 (Description)

<img src="https://raw.githubusercontent.com/ATB-K/VoiceRoDoKu/doc/image/VoiceRoDoKu.png">

AHS社の[VOICEROID2](https://www.ah-soft.com/voiceroid/)を制御してWeb小説を朗読させるソフトです。(読み上げ時は画面左の立ち絵は口パクします)</br>
対応Webサイトは下記です。
| サイト名 | リンク |
| --- | --- |
| 青空文庫| https://www.aozora.gr.jp/ |
| Arcadia | http://www.mai-net.net/ |
| ハーメルン | https://syosetu.org/ |
| カクヨム | https://kakuyomu.jp/ |
| 小説家になろう | https://syosetu.com/ |
</br>

## 使い方 (Usage)

1. 起動後に「Get」ボタン横のテキストボックスにWeb小説のURLを入力します。
2. 「Get」ボタンを押下すると、タイトルとエピソード一覧が読み込まれます。
3. 朗読させたいエピソードを選択します。
4. 「START」ボタンを押下して読み上げが開始されます。
5. 「STOP」ボタンで読み上げを終了します。

### ※注意

- pywinautoの制約により、読み上げ中はVOICEROID2のアプリにアクティブウィンドウが頻繁に切り替わります。</br>頑張ったけどどーしようも無いのでAHS社さんがIF作ってくれることに期待しましょう。

## 依存関係 (Requirement)

- requirements.txt に記載済み

## インストール方法 (Install)

- Python
- Binary

## ライセンス (Licence)

- 紲星あかりの立ち絵は [からい](https://seiga.nicovideo.jp/user/illust/12960693) 氏の配布物です。</br>
- 使用に関しては[こちら](https://seiga.nicovideo.jp/seiga/im9233706)でダウンロードできる素材のreadme.txtを確認してください。

## Author

[ATB](https://github.com/ATB-K)