import configparser
import telegram
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    try:
        config = configparser.ConfigParser()
        config.read('./config/config.ini')
    except Exception:
        return 'Invalid config', 400

    chat_id = config['bot']['chat_id']
    body = request.json

    if 'chat_id' in body:
        chat_id = body['chat_id']

    if 'text' not in body:
        return 'Text not defined. Quit', 400

    bot = telegram.Bot(token=config['bot']['token'])
    result = bot.send_message(chat_id=chat_id, text=body['text'])
    return result.to_json()
