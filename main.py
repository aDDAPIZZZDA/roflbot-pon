from aiogram import Dispatcher, Bot, types, executor
from random import choice

bot = Bot(token='5413288721:AAFE8S-ADmbFhFmdOoeD8q4gpBLliWpVvhE', parse_mode="HTML")
dp = Dispatcher(bot)

q = ['Скамер', 'Ванючька пердючька', 'Жмот-хуеглот', 'Жадина гавядина', 'хуй вонючий', 'гандон пердасос', 'Везучий! Щанс выподения этого смс 2%!', 'Камень', 'Полуфабрикат', 'Лысый', 'Натурал', 'Понский пон', 'Жена математички', 'Ароматный писюн', 'Ебанат натрия', 'Хороший', 'Раб <a href="tg://user?id=1615591694">картошки</a>', 'Очко', 'Эгоист', 'Дрочун', 'Гей', 'Красавчик', 'Урод', 'Говно', 'Шрек', 'Спонсор сахариуса', 'Хуй', 'Путин', 'Хацкер', 'Далбаёб', 'Секси', 'Любитель сосочков', 'А4', 'Файзик гей', 'Музей пидарасов', 'Диабло GAY', 'ТРАХтарист', 'Мактрахер', 'Гачи-Мучи', 'Собака', 'Олд', 'Лох', 'Длинный хуй', 'Короткий хуй', 'Понос шакала', 'Сперма дракона', 'Петушиный клюв', 'Сранимешник', 'Залупа кита', 'Милашка', 'Топ', 'Даша-путешественница']

@dp.message_handler(content_types=['text'])
async def texts(message: types.Message):
    t = message.text
    message_id = 0
    if message.message_id == message_id:
    #    try:
        await bot.send_message(-1001283685896, f"<b>В ЧАТЕ ДОШЛИ ДО СООБЩЕНИЯ, АЙДИ КОТОРОГО БЫЛО ЗАНЕСЕНО КАК 'розыгрыш админки'!!!\nНаш победитель: <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>")
        await message.pin()
      #  except:pass
    if t.split(" ")[0] == '.розыгрыш_админки':
        message_id = t.split(" ")[1]
        await message.reply("<b>Ура!\nАйди сообщения было сохранено!\nКогда сообщение приобретет айди {message_id}, то бот постарается уведомить всех админов в лс а так же напишет в чат!!</b>")

    elif t == '.я' or t == '.Я':
        text = choice(q)
        await message.reply(f'<b>Ты {text}</b>')
    
    
    elif t == '.я -acc':
        await message.reply(f'<b>Ты:\nТвой полный ник: {message.from_user.full_name}\nТвой айди(ID): {message.from_user.id}\nТвой юзернейм: @{message.from_user.username}\nПермалинк на тебя: {message.from_user.mention}\nВсё.</b>')
    
    elif t == '/start' or t == '/start@Music_Chat_ROBOT':
        await message.reply("<b>Ку :)\nКароч чтоб посмотреть команды напиши либо <code>.help</code> либо <code>.хелп</code>\nХорошего дня!</b>")
    
    elif t == '.хелп' or t == '.help' or t == '/help' or t == '/help@Music_Chat_ROBOT':
        qw = [
            'No Helps xD',
            '''<b>Тебе повезло пон, ибо на это смс шанс выпадения 50%!
Хотя это дохуя, ладно!
            
Кароче пока ток такие команды:</b>
<code>.адм</code> <b>|</b> <code>.adm</code> <b>-</b> <i>список админов чата</i>
<code>.я</code> <b>|</b> <code>.ты</code> <b>-</b> <i>говорит кто ты | чел реплея</i>
<code>.термукс</code> <b>|</b> <code>.т</code> <b>-</b> <i>последняя версия термукса</i>
<code>.боты</code> <b>-</b> <i>полезные боты (16 частей)</i>

<code>.я -acc</code> <b>-</b> <i>говорит инфу о твоем аккаунте</i>

<code>.хелп</code> <b>|</b> <code>.help</code> <b>-</b> <i>доступные команды</i>'''
        ]
        text = choice(qw)
        await message.reply(text)

    elif t == '.ты' or t == '.Ты':
        try:
            await message.delete()
        except:pass

        if message.reply_to_message:
            text = choice(q)
            kf = f"<b>Ты {text}</b>"
            await message.reply_to_message.reply(kf)
        else:
            await message.reply('<b>Только на реплей!</b>')

    elif t == '.адм' or t == '.adm':
        w = 1
        qу = []
        admins = await bot.get_chat_administrators(message.chat.id)
        for i in admins:
            qу.append(f'''{w} <a href='https://t.me/{i.user.username}'>{i.user.full_name}</a>''')
            w = w + 1
        await message.answer(f'Всего администраторов в чате: {w}\n' + '\n'.join(qу), disable_web_page_preview=True)

    elif t == '1':
        pon4ik = await bot.get_chat_member_count(message.chat.id)
        ponnn = await bot.get_chat_member_count(message.chat.id)
        await message.reply(f"{pon4ik}\n{ponnn}")
    
    elif t == '.термукс' or t == '.т':
        termux = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(text='⚡️ Скачать', url='https://t.me/EVIL_APK/376')
                ]
            ]
        )

        try:
            await message.delete()
        except:
            pass

        await message.answer('<b>ПОСЛЕДНЯЯ ВЕРСИЯ TERMUX</b>', reply_markup=termux)

    elif t == '.боты' or t == '.bots' or t == '/bots' or t == '/bots@Music_Chat_ROBOT':
        bots = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton('Часть 1', url='https://t.me/c/1304250069/88'),
                    types.InlineKeyboardButton('Часть 2', url='https://t.me/c/1304250069/111'),
                    types.InlineKeyboardButton('Часть 3', url='https://t.me/c/1304250069/136')
                ],
                [
                    types.InlineKeyboardButton('Часть 4', url='https://t.me/c/1304250069/196'),
                    types.InlineKeyboardButton('Часть 5', url='https://t.me/c/1304250069/234'),
                    types.InlineKeyboardButton('Часть 6', url='https://t.me/c/1304250069/303'),
                ],
                [
                    types.InlineKeyboardButton('Часть 7', url='https://t.me/c/1304250069/387'),
                    types.InlineKeyboardButton('Часть 8', url='https://t.me/c/1304250069/423'),
                    types.InlineKeyboardButton('Часть 9', url='https://t.me/c/1304250069/452')
                ],
                [
                    types.InlineKeyboardButton('Часть 10', url='https://t.me/c/1304250069/479'),
                    types.InlineKeyboardButton('Часть 11', url='https://t.me/c/1304250069/529'),
                    types.InlineKeyboardButton('Часть 12', url='https://t.me/c/1304250069/601')
                ],
                [
                    types.InlineKeyboardButton('Часть 13', url='https://t.me/c/1304250069/641'),
                    types.InlineKeyboardButton('Часть 14', url='https://t.me/c/1304250069/687')
                ],
                [
                    types.InlineKeyboardButton('Часть 15', url='https://t.me/c/1304250069/733'),
                    types.InlineKeyboardButton('Часть 16', url='https://t.me/c/1304250069/763')
                ]
            ]
        )

        await message.answer('<b>⬇️⬇️ ПОЛЕЗНЫЕ БОТЫ ⬇️⬇️</b>', reply_markup=bots)
    

async def on_startup(bot):
    ADMINS = [
        910207255,
        -1001283685896,
        5184725450,
    ]
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "<b>Бот успешно запущен/перезапущен! ✅</b>")
        except:pass

    #await bot.set_my_commands([
    #    types.BotCommand('start', 'пон | старт'),
    #    types.BotCommand('help', 'Помощь по боту'),
    #    types.BotCommand('bots', 'пон | список крутых ботов'),
    #])

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
