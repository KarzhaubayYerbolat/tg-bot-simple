# simple-tg-bot

Необходимо вставить свои настройки в файле bot_webhook_handler/bot/config.py
  BOT_TOKEN = 'YOUR_BOT_TOKEN'
  WEBHOOK_URL = 'WEBHOOK_URL'
  TELEGRAM_API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'
Переходим по ссылке "webapp_url/setwebhook/" для устанавки вебхука для вашего Telegram бота.
Запустить сервер django - python manage.py runserver
