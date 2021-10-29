import requests
import json

with open("setting.json", "r", encoding="utf8" ) as jfile:
    jdata = json.load(jfile)


token = jdata["TOKEN"]

headers = {
    "Authorization" : "Bearer " + token,
    "Content-Type" : "application/x-www-from-urlencoded"
}


w = "屋\n" * 3

params = {"message": w}


url = "https://notify-api.line.me/api/notify"

r = requests.post(url, headers=headers, params=params)

if r.status_code == 200:
    print("已經送出通知訊息...")

else:
    print("錯誤!送出失敗")

# 英文限1000字 中文限854字
print(len(w))

# Json格式解析
# message 訊息
# imageThumbnail 縮圖
# imageFullsize 大圖
# imageFile 圖片檔案
# stickerPackageId 內建貼圖編號
# stickerId 內建貼圖編號內的id

# import requests
#
# def send_notify(token, msg, filepath=None, stickerPackageId=None, stickerId=None):
#     payload = {'message': msg}
#     headers = {
#         "Authorization": "Bearer " + token
#      }
#     if stickerPackageId and stickerId:
#         payload['stickerPackageId'] = stickerPackageId
#         payload['stickerId'] = stickerId
#
#     if filepath:
#         attachment = {'imageFile': open(filepath, 'rb')}
#         print(attachment)
#         r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload, files=attachment)
#     else:
#         print("attachment")
#         r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
#     return r.status_code, r.text
#
# # Test line notify
# token = ""
# send_notify(token=token, msg='更新來了！', filepath='')

