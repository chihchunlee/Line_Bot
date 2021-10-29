# 使用requests
# import requests
# import json
#
# with open("setting.json", "r", encoding="utf8") as jfile:
#     jdata = json.load(jfile)
#
# # telegramApp下載>搜尋BotFather>/start>建立新機器人/newbot>替機器人命名>使用者名稱_bot
# # t.me/使用者名稱_bot 找到機器人 可以找到token
# token = jdata["TelegramBotToken"]
#
# # 搜尋<使用者名稱_bot>點選進入聊天室>按下start>隨意輸入訊息
# # 瀏覽器輸入https://api.telegram.org/bot<token>/getUpdates
# # 找到聊天室id "from":{"id":"<chat_id>"
# chat_id = jdata["chat_id"]
#
# def telegram_bot_sendText(msg):
#     url = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}"
#     r = requests.post(url.format(token,chat_id,msg))
#     return r.json()
#
# test = telegram_bot_sendText("hi!C.C")
#
# print(test)

# 使用telegram

# pip install python-telegram-bot
import telegram
import json

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

token = jdata["TelegramBotToken"]
chat_id = jdata["chat_id"]

def telegram_bot_sendText(msg):
    bot = telegram.Bot(token=token)
    return  bot.sendMessage(chat_id=chat_id, text=msg)

test = telegram_bot_sendText("hi!C.C")

print(test)

