import json
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .config import TELEGRAM_API_URL, WEBHOOK_URL


@csrf_exempt
def telegram_bot(request):
    if request.method == 'POST':
        message = json.loads(request.body.decode('utf-8'))
        message = message['message']['text']
        chat_id = message['message']['chat']['id']
        if message == '/start':
            username = message['message']['from']['username']
            reply_text = f'Привет, {username}!'
        else:
            reply_text = f'Я умею обрабатывать только команду /start'
        send_message("sendMessage", chat_id, reply_text)
        return HttpResponse('ok')


def send_message(method, chat_id, text):
    return requests.post(f'{TELEGRAM_API_URL + method}?chat_id={chat_id}&text={text}')


def setwebhook(request):
    response = requests.post(TELEGRAM_API_URL + 'setWebhook?url=' + WEBHOOK_URL)
    return HttpResponse(f"{response.text}")
