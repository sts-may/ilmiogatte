import telebot
import random
import os
from datetime import datetime
from telebot import types

# ===== НАСТРОЙКИ (берём из переменных окружения) =====
BOT_TOKEN = os.environ["8676158894:AAFD8B8SRqzog47litgoL8x_FttEYxmHTAI"]
CHAT_ID   = os.environ["656506167"]

TARGET_DATE = datetime(2026, 11, 3, 20, 40)

PHOTOS = [
    "https://i.pinimg.com/1200x/e7/ec/62/e7ec625ab06ad88984f8f2875a8f61ab.jpg",
    "https://i.pinimg.com/1200x/a5/80/38/a5803883c01b9f647af205bbdec3054e.jpg",
    "https://i.pinimg.com/1200x/22/51/53/225153ec4e15b227a90a2d9dd9b28cc0.jpg",
    "https://i.pinimg.com/736x/6d/31/e8/6d31e81849ee9cef26c6754c030c4422.jpg",
    "https://i.pinimg.com/736x/0c/40/07/0c4007f2b403898d2c116fe917d830c0.jpg",
    "https://i.pinimg.com/1200x/5a/9b/74/5a9b740483b0c1a4fc085d402e676ea2.jpg",
    "https://i.pinimg.com/736x/4c/1b/25/4c1b2567cc4a0759bbbfad2e70fbbf4f.jpg",
    "https://i.pinimg.com/736x/f9/d2/9d/f9d29d8fc3dea593c89f9bf58958dda0.jpg",
    "https://i.pinimg.com/1200x/08/75/f5/0875f539b5610ef0ecde1f077e5eedbc.jpg",
    "https://i.pinimg.com/736x/de/69/18/de69181012a3bb470442de46f309a7c7.jpg",
    "https://i.pinimg.com/1200x/64/e8/d9/64e8d95a8365be56dfd25b55f38690a7.jpg",
    "https://i.pinimg.com/736x/16/4f/7d/164f7db54f229775a7dc2c26ba5b6b78.jpg",
    "https://i.pinimg.com/736x/b9/1e/68/b91e68e7e018849fab0ca4866784a48a.jpg",
    "https://i.pinimg.com/1200x/44/d0/86/44d0865c412ebfe3801ea6ddbba1db7e.jpg",
    "https://i.pinimg.com/736x/ec/a0/ff/eca0ffff89ad454947d989c031b92443.jpg",
    "https://i.pinimg.com/1200x/5c/e9/b1/5ce9b1a46c528b38ef7530eafd08d8a6.jpg",
    "https://i.pinimg.com/736x/37/a9/8a/37a98ae8f633d1ad9b71a785b089d045.jpg",
    "https://i.pinimg.com/736x/f8/a7/eb/f8a7eb306721b14c379b3b2ca8950837.jpg",
    "https://i.pinimg.com/736x/3d/bc/48/3dbc48b717f634e93dae7637ae9e6dcb.jpg",
    "https://i.pinimg.com/736x/d6/29/90/d6299098e979886bad403fef90421055.jpg",
    "https://i.pinimg.com/736x/f0/a8/0d/f0a80d5ec21e729f7ed2933749d88b0f.jpg",
    "https://i.pinimg.com/736x/a9/99/09/a999092288bdaf83c8178c4f8a5bb89a.jpg",
    "https://i.pinimg.com/736x/93/29/2f/93292fd5fcdf8a32f383036f7896fcd3.jpg",
    "https://i.pinimg.com/1200x/78/24/aa/7824aaa64641f63d389381b32ef195d0.jpg",
    "https://i.pinimg.com/1200x/31/18/9b/31189b1c17af500bfe2a20275b167a9c.jpg",
    "https://i.pinimg.com/1200x/9c/05/19/9c051945377cf93e85796b72950cac8f.jpg",
    "https://i.pinimg.com/736x/dd/6c/88/dd6c88c955454182d20785ee9056cf99.jpg",
    "https://i.pinimg.com/736x/c0/ae/c1/c0aec17d8e8304b8de94aa4b5494ac2e.jpg",
    "https://i.pinimg.com/736x/ea/c3/00/eac30020ec20c83d21772d9fb5901076.jpg",
    "https://i.pinimg.com/736x/2c/37/84/2c3784f8b575a86c0907dca7d6860320.jpg",
    "https://i.pinimg.com/1200x/39/43/cf/3943cf8ce4832d915c5294d306b1c95e.jpg",
    "https://i.pinimg.com/736x/46/75/1e/46751e9b84b98eea205618cec0150e5d.jpg",
    "https://i.pinimg.com/736x/17/25/f6/1725f6e3ab59ce0926b6ecff7795e517.jpg",
    "https://i.pinimg.com/736x/ed/0e/ec/ed0eec1409126f7336fcab6e513fca09.jpg",
    "https://i.pinimg.com/736x/46/cb/2f/46cb2f2908c141f29167361a0838b26f.jpg",
    "https://i.pinimg.com/1200x/e5/78/b6/e578b6b5f9262ae31acaf7fb9d14f714.jpg",
    "https://i.pinimg.com/736x/95/b8/fc/95b8fc519f71824e546823d3b9765d25.jpg",
    "https://i.pinimg.com/736x/c6/8d/ed/c68deda15284db05766f94697408884a.jpg",
    # Добавляй сколько хочешь!
]

bot = telebot.TeleBot(BOT_TOKEN)


def plural(n, forms):
    n = abs(n)
    if 11 <= n % 100 <= 14:
        return forms[2]
    m = n % 10
    if m == 1:
        return forms[0]
    if 2 <= m <= 4:
        return forms[1]
    return forms[2]


def build_message():
    delta = TARGET_DATE - datetime.now()
    total = int(delta.total_seconds())

    if total <= 0:
        return "🎉 Сегодня тот самый день! 💕"

    d = total // 86400
    h = (total % 86400) // 3600
    m = (total % 3600) // 60

    if d > 0:
        return (f"💕 Осталось до встречи с тобой:\n"
                f"🗓 {d} {plural(d, ('день', 'дня', 'дней'))}\n"
                f"⏰ {h} {plural(h, ('час', 'часа', 'часов'))}\n"
                f"⏳ {m} {plural(m, ('минута', 'минуты', 'минут'))}")
    if h > 0:
        return (f"💕 Осталось до встречи с тобой:\n"
                f"⏰ {h} {plural(h, ('час', 'часа', 'часов'))}\n"
                f"⏳ {m} {plural(m, ('минута', 'минуты', 'минут'))}")
    if m > 0:
        return (f"💕 Осталось до встречи с тобой:\n"
                f"⏳ {m} {plural(m, ('минута', 'минуты', 'минут'))}\n"
                f"🔥 Совсем скоро!")
    return "💕 Встреча уже здесь! Я рядом 💕"


def send_countdown(chat_id):
    try:
        bot.send_photo(chat_id, random.choice(PHOTOS), caption=build_message())
    except Exception as e:
        bot.send_message(chat_id, f"Ошибка: {e}")


def make_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton("🔄 Обновить"))
    return kb


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! 💕 Нажми кнопку 👇",
        reply_markup=make_keyboard()
    )
    send_countdown(message.chat.id)


@bot.message_handler(func=lambda m: m.text == "🔄 Обновить")
def refresh(message):
    send_countdown(message.chat.id)


@bot.message_handler(func=lambda m: True)
def any_message(message):
    bot.send_message(message.chat.id, "Нажми кнопку 👇", reply_markup=make_keyboard())


print("🤖 Бот запущен!")
bot.infinity_polling()