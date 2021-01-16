# import flask related
from flask import Flask, request, abort
# import linebot related
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    LocationSendMessage, ImageSendMessage, StickerSendMessage
)

# create flask server •
# 架設web server 並且與LineBot連結 Handle所收到的POST請求
app = Flask(__name__)
# your linebot message API - Channel access token (from LINE Developer)
line_bot_api = LineBotApi('your Messaging API > Channel access token (long-lived)')
# your linebot message API - Channel secret
handler = WebhookHandler('your Basic settings > Channel secret')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        print('receive msg')
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# handle msg
# LINE Platform 將用戶訊息轉換為 JSON 後
# 可以分類為多種 Webhook event，最常見為用戶訊息事件(MessageEvent)
# 使用 Python decorator 搭配 handler.add 宣告欲接收並處理的 event
# 解析 event 內容，獲得用戶資訊與訊息
# event 由 JSON 格式轉成
# 參考 TextMessage JSON 格式解析資料，取得用戶專屬ID與傳送之訊息
# 利用 Line Bot API 取得用戶於 LINE 上設定之姓名

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user info & message
    user_id = event.source.user_id
    msg = event.message.text
    user_name = line_bot_api.get_profile(user_id).display_name
    
    # get msg details 將取得之資料印出
    print('msg from [', user_name, '](', user_id, ') : ', msg)

# run app 呼叫 app.run() 啟用 web server
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)