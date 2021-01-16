# Line_Bot 
https://tw.linebiz.com/login/
登入帳號 先至 Line Official Account Manager 主頁中
• 點擊「聊天」 ，設定回應模式
• 在「基本設定」> 設定「回應模式」為：聊天機器人
• 在「進階設定」> 設定「自動回應訊息」為：停用 .設定「Webhook」為：啟用 並且點選「Message API 設定」，啟用「Message API」
  Webhook網址
使用ngrok
• 開啟 ngrok，輸入ngrok http 12345 取得 Webhook URL 後面加/callback
• 在此「Webhook 網址」中填入：https://your_webhook_url/callback
• 點選下方 「Line Developers」

• 在 Line Developers 中登入後點選個人頁面
• 於左邊選單中點選先前輸入過的服務提供者名稱
• 點擊右側 Channel 中的官方帳號

• token =  Message API > Channel access token (long-lived)
• secret =  Basic settings > Channel secret

python 環境安裝 Line Bot API 套件
pip install line-bot-sdk

ngrok取得url 取得token,secre 使用python環境 路徑切到程式資料夾 執行flask
python Demo2-1.py

要接收語音，必須使用以下程式碼 pip install SpeechRecognition
• 語音訊息是 AudioMessage
• Server 會將語音存在 recording.mp3
• LINE會壓縮語音，取樣率僅 10000 Hz

• 可以透過附檔的 ffmpeg.exe 進行轉檔
• 必須將 ffmpeg.exe 跟主程式 Demo_2-3.py 放在一起
• 轉檔的程式如下
import os
os.system('ffmpeg -y -i from.mp3 to.wav')
• -y：無條件覆蓋檔案
• from.mp3：原始檔案路徑
• to.wav：要轉成的檔案
