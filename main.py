
import os

# if os.getenv('API_ENV') != 'production':
#     from dotenv import load_dotenv

#     load_dotenv()

import uvicorn

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from routers import webhooks

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(webhooks.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/liff", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


#if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
# import requests
# from typing import Union
# from fastapi import FastAPI,Request
# from linebot.v3 import (
#     WebhookHandler
# )
# from linebot.v3.exceptions import (
#     InvalidSignatureError
# )
# from linebot.v3.messaging import (
#     Configuration,
#     ApiClient,
#     MessagingApi,
#     ReplyMessageRequest,
#     TextMessage
# )
# from linebot.v3.webhooks import (
#     MessageEvent,
#     TextMessageContent
# )
# access_token_str="wWGqSfuVclCkwoH40ojM+pHdhCLYizeeHsDIkaWonUULikT9K5ZSDiIMhrTB/T3dMvvh+ftc+3zqzBH/84uoGRVyeXoH6foDB7xLX9I1bBTuWLhWqlieYyUa8htd3U/VCi1cB3pSQQwVq7i9j0ddnQdB04t89/1O/w1cDnyilFU="
# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# configuration = Configuration(access_token=access_token_str)
# handler = WebhookHandler('63127196231ef02f9064c2a244d6c503')


# #@app.route("/callback", methods=['POST'])
# @app.get("/callback")
# def callback():
#     # get X-Line-Signature header value
#     signature = Request.headers['X-Line-Signature']
    
#     # get request body as text
#     body = Request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         app.logger.info("Invalid signature. Please check your channel access token/channel secret.")

#         #abort(400)

#     return 'OK'


# @handler.add(MessageEvent, message=TextMessageContent)
# def handle_message(event):
#     with ApiClient(configuration) as api_client:
#         line_bot_api = MessagingApi(api_client)
#         line_bot_api.reply_message_with_http_info(
#             ReplyMessageRequest(
#                 reply_token=event.reply_token,
#                 messages=[TextMessage(text=event.message.text)]
#             )
#         )

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
