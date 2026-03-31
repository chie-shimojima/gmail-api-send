# Gmail API 送信プログラム（Python）

Google Gmail API を使って、Python からメールを送信するプログラムです。  
`.env` に宛先・件名・本文を入れて実行すると、Gmailからメールを送れます。

---

## ✅ できること
- Gmail API を使ってメール送信できる
- `.env` で宛先・件名・本文を変更できる

---

## ✅ 使用したもの
- Python 3
- Gmail API
- Google OAuth2 認証

---

## ✅ 必要ファイル
このフォルダに以下が入っている状態で動きます。

- `send_gmail.py`（メール送信プログラム）
- `credentials.json`（Google Cloudで作成したOAuth情報）
- `.env`（宛先・件名・本文を保存）
※ `token.json` は初回実行後に自動で作成されます

---

## ✅ 事前準備（Google Cloud）
1. Google Cloud でプロジェクトを作成
2. Gmail API を有効化
3. OAuth クライアントIDを作成（デスクトップアプリ）
4. `credentials.json` をダウンロードして、このフォルダに入れる
5. OAuth同意画面の「テストユーザー」に自分のGmailアドレスを追加する

---

## ✅ 事前準備（Pythonライブラリ）
ターミナルで以下をインストールします。

```bash
pip install google-api-python-client google-auth google-auth-oauthlib python-dotenv
