import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# المفاتيح الخاصة بك
CHANNEL_ACCESS_TOKEN = 'LE+tq2EFuI6PF+drxOhXyHVZWfkIC2rCgUVyh1Y3cuR7awNrcUan2vWm3YEt43SjA7Offz6NOS56F/Mkj4pzlTIM5F+lFMDRftKI5i7wh5bveY5qxaXHDWM68ADBgmoiRl2DGEn3qFV0MvD3ZsBAJAdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '3780d899b3f7f4431e882392ed164eca'

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers.get('X-Line-Signature', '')
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if text.lower() == 'ping':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Pong! Tommy Protect is Active 🛡️')
        )

@app.route("/", methods=['GET'])
def home():
    return "Tommy Protect Bot is Online!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
