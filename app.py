
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('s//zcdFrDph+6ez1oNhNL2Bz72L81N5MboXcT+6ntt2FEjHCTfg+3fliwWAcrb9hQaRCDiLICDMLkdJ47PymdXLfw0YVJSUZhyQKJ8Tt/PSTlHpCh/PWDd6/4vcSC/F4RtxP+1nSg12z/7NRgPxgsQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('65348d8c44aebcb7219fb72173948348')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
