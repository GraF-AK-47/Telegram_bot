Инструкция по запуску Telegram-прогноз бота на Render:

1. Создайте аккаунт на https://render.com (можно через Google).
2. Создайте новый репозиторий на GitHub и загрузите туда bot.py и requirements.txt.
3. На Render создайте New Web Service → подключите свой репозиторий.
4. В настройках Environment Variables добавьте:
   TOKEN = ваш токен бота
   CHAT_ID = ваш Telegram ID
5. В поле Start Command укажите:
   python bot.py
6. Нажмите Deploy.

Бот начнёт работать 24/7 и будет присылать прогнозы по команде /prognoz.
