from flask import Flask, request, abort, jsonify
from linebot import LineBotApi, WebhookHandler
import json
import pyrebase
import pandas as pd
from linebot.exceptions import LineBotApiError, InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from rpa_selenium_scraping import WebScraping
from vision_machine_optical import VisionOCR

app = Flask(__name__)

with open('config/db_firebase.json', encoding='utf8') as config_file:
    data = json.load(config_file)
    config = data['firebase']
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    line_bot_api = LineBotApi(data['channel_secret_token'])
    handler = WebhookHandler(data['channel_secret'])


def log_line(val):
    with open('log.json', 'w') as log_line:
        json.dump(val, log_line)


def no_event(decoded):
    no_event = len(decoded['events'])
    for i in range(no_event):
        events = decoded['events'][i]
        event_handler(events)


def cryptocurrency_scrap():
    my_scrap = WebScraping('config/chromedriver')
    result = my_scrap.dynamic_scraping(
        uri='https://www.bitkub.com',
        html='table',
        key='class',
        val='deposit__table-wrapper dashboard__table',
        delay=1
    )
    dfs = pd.read_html(str(result))
    data = pd.DataFrame(dfs[0])
    excel = pd.ExcelWriter('static/excells/CryptocurrencyPrices.xlsx', engine='xlsxwriter')
    data.to_excel(excel, sheet_name='Sheet1')
    excel.save()


def event_handle_add():
    raw_json = request.get_json()
    json_line = json.dumps(raw_json)
    decoded = json.loads(json_line)
    return decoded


def get_profile(user_id):
    profile = line_bot_api.get_profile(user_id)
    displayName = profile.display_name
    userId = profile.user_id
    img = profile.picture_url
    status = profile.status_message
    result = {'displayName': displayName, 'userId': userId, 'img': img, 'status': status}
    return result


@app.route('/webhook', methods=['POST'])
def webhook():
    raw_json = request.get_json()
    json_line = json.dumps(raw_json)
    decoded = json.loads(json_line)
    log_line(raw_json)
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    event = decoded['events'][0]
    _type = event['type']
    handler.handle(body, signature)
    try:
        if _type == 'unfollow':
            userId = event['source']['userId']
            remove = db.child('userId_follow').order_by_child('userId').equal_to(userId).get()
            remove = remove.val()
            remove = remove.keys()
            for i in remove:
                db.child('user_follow').child(i).remove()
        elif _type == 'follow':
            userId = event['source']['userId']
            profile = get_profile(userId)
            inserted = {'displayName': profile['displayName'], 'userId': userId, 'img': profile['img'],
                        'status': profile['status']}
            db.child('user_follow').push(inserted)
        elif _type == 'message':
            message_type = event['message']['type']
            if message_type == 'text':
                try:
                    userId = event['source']['userId']
                    message = event['message']['text']
                    profile = get_profile(userId)
                    push_message = {'user_id': userId, 'message': message, 'display_name': profile['displayName'],
                                    'img': profile['img'],
                                    'status': profile['status']}
                    db.child('message_user').push(push_message)
                    handler.handle(body, signature)
                except InvalidSignatureError as v:
                    api_error = {'status_code': v.status_code, 'message': v.message}
                    abort(400)
                    jsonify(api_error)
            else:
                no_event(decoded)
    except LineBotApiError as e:
        abort(400)
        api_error = {'status_code': e.status_code, 'request_id': e.request_id, 'message': e.error.message,
                     'details': e.error.details}
        return jsonify(api_error)
    return jsonify(raw_json)


def event_handler(event):
    _type = event['message']['type']
    if _type == 'sticker':
        replyToken = event['replyToken']
        userId = event['source']['userId']
        line_bot_api.reply_message(replyToken, TextMessage(text='Please wait...'))
        cryptocurrency_scrap()
        url = 'https://dd0263ae5858.ngrok.io/static/CryptocurrencyPrices.xlsx'
        line_bot_api.push_message(userId, TextMessage(text=url))
    elif _type == 'image':
        img_id = event['message']['id']
        img_id = line_bot_api.get_message_content(img_id)
        with open('static/user_pic.png', 'wb') as fd:
            for chunk in img_id.iter_content():
                fd.write(chunk)
        replyToken = event['replyToken']
        userId = event['source']['userId']
        message = db.child('message_user').get()
        message_idx = [x.val() for x in message.each() if x.val()['user_id'] == userId]
        if message_idx[-1]['message'] == 'แปลงรูปภาพ':
            ocr = VisionOCR('static/user_pic.png')
            line_bot_api.reply_message(replyToken, TextSendMessage(text='กรุณารอสักครู่นะค่ะกำลังเข้าสู่กระบวนการ...'))
            text = ocr.document_google()
            line_bot_api.push_message(userId, TextSendMessage(text=text[0]))
        else:
            line_bot_api.reply_message(replyToken, TextMessage(text='รูปสวยดี'))


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    handle = event_handle_add()
    handle = handle['events'][0]
    message = handle['message']['text']
    if message == 'แปลงรูปภาพ':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='ทำการใส่รูปมาได้เลยค่ะ...'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='อื่นๆ...'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)