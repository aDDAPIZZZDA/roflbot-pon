from telebot import TeleBot
from random import choice

bot = TeleBot('5413288721:AAFE8S-ADmbFhFmdOoeD8q4gpBLliWpVvhE')

q = ['Скамер', 'Эгоист', 'Дрочун', 'Гей', 'Красавчик', 'Урод', 'Говно', 'Шрек', 'Спонсор сахариуса', 'Хуй', 'Путин', 'Хацкер', 'Далбаёб', 'Секси', 'Любитель сосочков', 'А4', 'Файзик гей', 'Музей пидарасов', 'Диабло GAY', 'ТРАХтарист', 'Мактрахер', 'Гачи-Мучи', 'Собака', 'Олд', 'Лох', 'Длинный хуй', 'Короткий хуй', 'Понос шакала', 'Сперма дракона', 'Петушиный клюв', 'Сранимешник', 'Залупа кита', 'Милашка', 'Топ', 'Даша-путешественница']

@bot.message_handler(commands=['helps'])
def help(message):
    qw = ['No Helps xD', '<b>Тебе повезло пон, ибо на это смс 20% выподения!\n\nКароче пока ток такие команды:</b>\n<code>.адм</code> <b>|</b> <code>.adm</code> <b>-</b> <i>список админов чата</i>\n<code>.мозг</code> <b>-</b> <i>кидает видео мозг</i>\n<code>.я</code> <b>|</b> <code>.ты</code> <b>-</b> <i>говорит кто ты | чел реплея</i>']
    text = choice(qw)
    bot.send_message(message.chat.id, f"{text}", parse_mode="HTML")

@bot.message_handler(content_types=['text'])
def members(message):
    if message.text.lover() == '.я':
        text = choice(q)
        bot.send_message(message.chat.id, reply_to_message_id=message.message_id, text=f'<b>Ты {text}</b>', parse_mode="HTML")

    elif message.text.lover() == '.ты':
        text = choice(q)
        try:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except:
            pass
        try:
            bot.send_message(message.chat.id, reply_to_message_id=message.reply_to_message.message_id, text=f"<b>Ты {text}</b>", parse_mode="HTML")
        except:
            bot.send_message(message.chat.id, '<b>Только на реплей!</b>', parse_mode="HTML")

    elif message.text.lover() == '.адм' or message.text.lover() == '.adm':
        try:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except:
            pass
        w = 1
        qу = []
        for i in bot.get_chat_administrators(chat_id=message.chat.id):
            qу.append(f'''{w}) <a href='https://t.me/{i.user.username}'>{i.user.first_name}</a>''')
            w = w + 1
        bot.send_message(message.chat.id, '\n'.join(q), disable_web_page_preview=True, parse_mode="HTML")

    elif message.text == '1':
        bot.send_message(message.chat.id, bot.chat_member_handler())

while True:
    try:
        bot.polling()
    except Exception as e:
        print(e)
        continue