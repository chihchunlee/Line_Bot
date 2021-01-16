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

# create flask server
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
# 在MessageEvent的JSON中，存有一個replyToken
# 可使用於即時回覆訊息
# 可經由 event.reply_token 取得
# 屬於被動式回覆，不需要付錢
# 回覆用戶的訊息依照不同類型分為不同物件，如：
# 文字訊息：TextSendMessage
# 貼圖： StickerSendMessage
# 圖片訊息：ImageSendMessage
# 地點：LocationSendMessage

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user info & message
    user_id = event.source.user_id
    msg = event.message.text
    user_name = line_bot_api.get_profile(user_id).display_name
    
    # get msg details
    print('msg from [', user_name, '](', user_id, ') : ', msg)

# 回覆訊息
# line_bot_api.reply_message(token, message_objects)
# 文字訊息：TextSendMessage(text= ‘欲回覆文字’)
# 回覆 文字 貼圖 圖片 位置
    line_bot_api.reply_message(event.reply_token, 
                               [TextSendMessage(text = '回覆文字'),
                                StickerSendMessage(package_id='1',sticker_id='1'),
                                ImageSendMessage(original_content_url='https://www.iii.org.tw/assets/images/nav-all/logo.png', 
                                                 preview_image_url='https://www.iii.org.tw/assets/images/nav-all/logo.png'),
                                LocationSendMessage(
                                     title='Store Location',
                                     address='Taipei 101',
                                     latitude=25.033981,
                                     longitude=121.564506)
                                ])
    
    # push text_msg
    line_bot_api.push_message(user_id,
                              TextSendMessage(text = '您好^^'))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)