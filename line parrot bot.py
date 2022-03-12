from crypt import methods
from inspect import signature
from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import LinebotAPi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MassageEvent,TextMessage, TextSendMessage

    
line_bot_api = LineBotApi('貼上你的line bot channel token')
handler = WebhookHandler('貼上你的line bot channel secret')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.handers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, massage=TextMessage)
def handle_massage(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.massage.text))

if __name__ == '__main__':
    app.run()