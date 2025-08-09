import telebot
import time
import requests

TOKEN = "8324601730:AAFy1Az7BD34lgi6MKovioZb0Vb0erYZwwg"
CHAT_ID = 5943995738  # твой Telegram ID
bot = telebot.TeleBot(TOKEN)

def get_expert_opinion(match):
    # Заглушка — здесь можно подключить парсинг с сайтов
    return "Эксперты считают, что будет Тотал меньше 2.5"

def get_match_prediction(match):
    # Здесь можно подключить API с коэффициентами и статистикой
    return "Мой прогноз: Победа первой команды, вероятность 68%"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я анализирую матчи и собираю мнение экспертов. Напиши /prognoz Название матча")

@bot.message_handler(commands=["prognoz"])
def prognoz(message):
    match = message.text.replace("/prognoz", "").strip()
    if not match:
        bot.send_message(message.chat.id, "Укажи название матча, например: /prognoz Кривбасс Металлист")
        return
    expert = get_expert_opinion(match)
    my_pred = get_match_prediction(match)
    bot.send_message(message.chat.id, f"Матч: {match}\n{expert}\n{my_pred}")

if __name__ == "__main__":
    bot.polling(none_stop=True)
