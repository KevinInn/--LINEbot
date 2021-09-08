from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re, random
app = Flask(__name__)

line_bot_api = LineBotApi('vtS/h3UlE2hU2wocdyqLyUcFw/Eh8I2c0ueOSm+ABoIMyJRbgYj4+/7pD5eSUE57csURtiTcsTcmO0eCOA+IRD4MygWb4H97xZW/s9gK/V4ERxtCx9iiiawH/qfWM4qd8m4+cLxHKWXK8871EiWMyQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7745846b896f954a34db51915faf63d4')

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

flex_message_chinesefood = FlexSendMessage(
            alt_text='中華',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://cdn.pixabay.com/photo/2016/02/17/10/41/dumplings-1204814_1280.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://spot.line.me/search?cid=L3-9PM4EQ"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "LINE熱點-中華料理",
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "瀏覽店家",
                        "uri": "https://spot.line.me/search?cid=L3-9PM4EQ"
                        }
                    }
                    ],
                    "flex": 0
                }
            }
)
flex_message_japanfood = FlexSendMessage(
            alt_text='日式',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://cdn.pixabay.com/photo/2015/10/06/19/10/sushi-975075_1280.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://spot.line.me/search?cid=L3-87JP9Q"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "LINE熱點-日式料理",
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "瀏覽店家",
                        "uri": "https://spot.line.me/search?cid=L3-87JP9Q"
                        }
                    }
                    ],
                    "flex": 0
                }
            }
)
flex_message_koreanfood = FlexSendMessage(
            alt_text='韓式',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://cdn.pixabay.com/photo/2017/07/19/03/13/pot-2517765_1280.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://spot.line.me/search?cid=LC-1Q84YR"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "LINE熱點-韓式料理",
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "瀏覽店家",
                        "uri": "https://spot.line.me/search?cid=LC-1Q84YR"
                        }
                    }
                    ],
                    "flex": 0
                }
            }
)
flex_message_indianfood = FlexSendMessage(
            alt_text='印度',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://cdn.pixabay.com/photo/2016/10/31/04/24/indian-food-1784879_1280.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://spot.line.me/search?cid=LC-6R7YWQ"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "LINE熱點-印度料理",
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "瀏覽店家",
                        "uri": "https://spot.line.me/search?cid=LC-6R7YWQ"
                        }
                    }
                    ],
                    "flex": 0
                }
            }
)
flex_message_thaifood = FlexSendMessage(
            alt_text='泰式',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://cdn.pixabay.com/photo/2016/08/18/20/04/food-1603763_1280.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://spot.line.me/search?cid=LC-4R0D7J"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "LINE熱點-泰式料理",
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "瀏覽店家",
                        "uri": "https://spot.line.me/search?cid=LC-4R0D7J"
                        }
                    }
                    ],
                    "flex": 0
                }
            }
)
flex_message_vietnamfood = FlexSendMessage(
            alt_text='越南',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://cdn.pixabay.com/photo/2015/07/22/09/50/rice-noodles-855077_1280.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://spot.line.me/search?cid=LC-4RV32Q"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "LINE熱點-越南料理",
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "瀏覽店家",
                        "uri": "https://spot.line.me/search?cid=LC-4RV32Q"
                        }
                    }
                    ],
                    "flex": 0
                }
            }
)
flex_message_frenchfood = FlexSendMessage(
            alt_text='法式',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://cdn.pixabay.com/photo/2016/10/22/17/10/bread-1761197_1280.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://spot.line.me/search?cid=LC-G3Q2EJ"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "LINE熱點-法式料理",
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "瀏覽店家",
                        "uri": "https://spot.line.me/search?cid=LC-G3Q2EJ"
                        }
                    }
                    ],
                    "flex": 0
                }
            }
)
flex_message_italianfood = FlexSendMessage(
            alt_text='法式',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://cdn.pixabay.com/photo/2018/07/18/19/12/pasta-3547078_1280.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://spot.line.me/search?cid=LC-87RP9Q"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "LINE熱點-義式料理",
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "瀏覽店家",
                        "uri": "https://spot.line.me/search?cid=LC-87RP9Q"
                        }
                    }
                    ],
                    "flex": 0
                }
            }
)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    #recommend = 'none'
    if re.match('晚餐吃什麼', message):
        RANDOM = int(((random.random()) * 10)) % 8 + 1# 0 <= RANDOM <= 1
        if RANDOM == 1:
            #日式料理
            line_bot_api.reply_message(event.reply_token, flex_message_japanfood)
        elif RANDOM == 2:
            #中華料理
            line_bot_api.reply_message(event.reply_token, flex_message_chinesefood)
        elif RANDOM == 3:
            #韓式料理
            line_bot_api.reply_message(event.reply_token, flex_message_koreanfood)
        elif RANDOM == 4:
            #印度料理
            line_bot_api.reply_message(event.reply_token, flex_message_indianfood)
        elif RANDOM == 5:
            #泰式料理
            line_bot_api.reply_message(event.reply_token, flex_message_thaifood)
        elif RANDOM == 6:
            #越南料理
            line_bot_api.reply_message(event.reply_token, flex_message_vietnamfood)
        elif RANDOM == 7:
            #法式料理
            line_bot_api.reply_message(event.reply_token, flex_message_frenchfood)
        elif RANDOM == 8:
            #義式料理
            line_bot_api.reply_message(event.reply_token, flex_message_italianfood)

    else:
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='請輸入:晚餐吃什麼，以得到推薦'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)