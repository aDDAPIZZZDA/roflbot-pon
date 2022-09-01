
from aiogram import Dispatcher, Bot, types, executor
from random import choice

bot = Bot(token='5413288721:AAFE8S-ADmbFhFmdOoeD8q4gpBLliWpVvhE', parse_mode="HTML")
dp = Dispatcher(bot)

q = ['Скамер', 'Ванючька пердючька', 'Жмот-хуеглот', 'Жадина гавядина', 'Везучий! Щанс выподения этого смс 2%!', 'Камень', 'Полуфабрикат', 'Лысый', 'Натурал', 'Понский пон', 'Жена математички', 'Ароматный писюн', 'Ебанат натрия', 'Хороший', 'Раб <a href="tg://user?id=1615591694">картошки</a>', 'Очко', 'Эгоист', 'Дрочун', 'Гей', 'Красавчик', 'Урод', 'Говно', 'Шрек', 'Спонсор сахариуса', 'Хуй', 'Путин', 'Хацкер', 'Далбаёб', 'Секси', 'Любитель сосочков', 'А4', 'Файзик гей', 'Музей пидарасов', 'Диабло GAY', 'ТРАХтарист', 'Мактрахер', 'Гачи-Мучи', 'Собака', 'Олд', 'Лох', 'Длинный хуй', 'Короткий хуй', 'Понос шакала', 'Сперма дракона', 'Петушиный клюв', 'Сранимешник', 'Залупа кита', 'Милашка', 'Топ', 'Даша-путешественница']

@dp.message_handler(content_types=['text'])
async def members(message: types.Message):
    t = message.text
    if t == '.я' or t == '.Я':
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
        try:
            await message.reply_to_message.delete()
        except:
            pass
        w = 1
        qу = []
        admins = await message.chat.get_administrators()
        for i in admins:
            qу.append(f'''{w} <a href='tg://user?id={i.user.id}'>{i.user.full_name}</a>''')
            w = w + 1
        await message.answer(f'Всего администраторов в чате: {w}' + '\n'.join(qу), disable_web_page_preview=True)

    elif t == '1':
        pon4ik = message.chat.get_member_count()
        await message.reply(f"{pon4ik}")
    
    elif t == '.термукс' or t == '.т':
        termux = types.InlineKeyboardMarkup()
        q1 = types.InlineKeyboardButton(text='⚡️ Скачать', url='https://t.me/EVIL_APK/376')
        termux.add(q1)

        try:
            await message.delete()
        except:
            pass

        await message.reply('<b>ПОСЛЕДНЯЯ ВЕРСИЯ TERMUX</b>', reply_markup=termux)

    elif t == '.боты' or t == '.bots' or t == '/bots' or t == '/bots@Music_Chat_ROBOT':
        bots = types.InlineKeyboardMarkup()
        ch1 = types.InlineKeyboardButton('Часть 1', url='https://t.me/c/1304250069/88')
        ch2 = types.InlineKeyboardButton('Часть 2', url='https://t.me/c/1304250069/111')
        ch3 = types.InlineKeyboardButton('Часть 3', url='https://t.me/c/1304250069/136')
        ch4 = types.InlineKeyboardButton('Часть 4', url='https://t.me/c/1304250069/196')
        ch5 = types.InlineKeyboardButton('Часть 5', url='https://t.me/c/1304250069/234')
        ch6 = types.InlineKeyboardButton('Часть 6', url='https://t.me/c/1304250069/303')
        ch7 = types.InlineKeyboardButton('Часть 7', url='https://t.me/c/1304250069/387')
        ch8 = types.InlineKeyboardButton('Часть 8', url='https://t.me/c/1304250069/423')
        ch9 = types.InlineKeyboardButton('Часть 9', url='https://t.me/c/1304250069/452')
        ch10 = types.InlineKeyboardButton('Часть 10', url='https://t.me/c/1304250069/479')
        ch11 = types.InlineKeyboardButton('Часть 11', url='https://t.me/c/1304250069/529')
        ch12 = types.InlineKeyboardButton('Часть 12', url='https://t.me/c/1304250069/601')
        ch13 = types.InlineKeyboardButton('Часть 13', url='https://t.me/c/1304250069/641')
        ch14 = types.InlineKeyboardButton('Часть 14', url='https://t.me/c/1304250069/687')
        ch15 = types.InlineKeyboardButton('Часть 15', url='https://t.me/c/1304250069/733')
        ch16 = types.InlineKeyboardButton('Часть 16', url='https://t.me/c/1304250069/763')
        bots.add(ch1, ch2, ch3)
        bots.add(ch4, ch5, ch6)
        bots.add(ch7, ch8, ch9)
        bots.add(ch10, ch11, ch12)
        bots.add(ch13, ch14)
        bots.add(ch15, ch16)
        try:
            await message.delete()
        except:
            pass

        await message.reply('<b>⬇️⬇️ ПОЛЕЗНЫЕ БОТЫ ⬇️⬇️</b>', reply_markup=bots)


async def on_startup(dp: Dispatcher):
    ADMINS = [
        910207255,
        -1001283685896,
        5184725450,
    ]
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "<b>Бот успешно запущен/перезапущен! ✅</b>")
        except:pass

    await dp.bot.set_my_commands([
        types.BotCommand('start', 'пон | старт'),
        types.BotCommand('help', 'Помощь по боту'),
        types.BotCommand('bots', 'пон | список крутых ботов'),
    ])

async def pon(dp):
    await on_startup(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=pon)
