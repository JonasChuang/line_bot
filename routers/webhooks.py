import os,re
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, StickerMessage, \
    StickerSendMessage
from pydantic import BaseModel
access_token_str="wWGqSfuVclCkwoH40ojM+pHdhCLYizeeHsDIkaWonUULikT9K5ZSDiIMhrTB/T3dMvvh+ftc+3zqzBH/84uoGRVyeXoH6foDB7xLX9I1bBTuWLhWqlieYyUa8htd3U/VCi1cB3pSQQwVq7i9j0ddnQdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(access_token_str)
#line_bot_api.push_message("U67ec9b0663d3334ec2225d64dcbd1dab")

handler = WebhookHandler("63127196231ef02f9064c2a244d6c503")

router = APIRouter(
    prefix="/webhooks",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)


class Line(BaseModel):
    destination: str
    events: List[Optional[None]]


@router.post("/line")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="chatbot handle body error.")
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    print("!!!!!!!!!!!!!!!!!!!!!!")
    print(event)
    message=event.message.text
    print("收到:"+event.message.text)
    print("!!!!!!!!!!!!!!!!!!!!!!")
    if re.match("誰最漂亮",message):
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="容容最漂亮")
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )


@handler.add(MessageEvent, message=StickerMessage)
def sticker_text(event):
    # Judge condition
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(package_id='6136', sticker_id='10551379')
    )