
from aiogram import Dispatcher, Bot, types, executor
from random import choice

bot = Bot(token='5413288721:AAFE8S-ADmbFhFmdOoeD8q4gpBLliWpVvhE', parse_mode="HTML")
dp = Dispatcher(bot)

q = ['Скамер', 'Эгоист', 'Дрочун', 'Гей', 'Красавчик', 'Урод', 'Говно', 'Шрек', 'Спонсор сахариуса', 'Хуй', 'Путин', 'Хацкер', 'Далбаёб', 'Секси', 'Любитель сосочков', 'А4', 'Файзик гей', 'Музей пидарасов', 'Диабло GAY', 'ТРАХтарист', 'Мактрахер', 'Гачи-Мучи', 'Собака', 'Олд', 'Лох', 'Длинный хуй', 'Короткий хуй', 'Понос шакала', 'Сперма дракона', 'Петушиный клюв', 'Сранимешник', 'Залупа кита', 'Милашка', 'Топ', 'Даша-путешественница']

@dp.message_handler(commands=['helps'])
async def help(message: types.Message):
    qw = ['No Helps xD', '<b>Тебе повезло пон, ибо шанс выпадения этого смс 20%!\n\nКароче пока ток такие команды:</b>\n<code>.адм</code> <b>|</b> <code>.adm</code> <b>-</b> <i>список админов чата</i>\n<code>.мозг</code> <b>-</b> <i>кидает видео мозг</i>\n<code>.я</code> <b>|</b> <code>.ты</code> <b>-</b> <i>говорит кто ты | чел реплея</i>']
    text = choice(qw)
    await message.answer(text)

@dp.message_handler(content_types=['text'])
async def members(message: types.Message):
    t = message.text
    if t.lover() == '.я':
        text = choice(q)
        await message.reply(f'<b>Ты {text}</b>')

    elif t.lover() == '.ты':
        text = choice

        try:
            await message.reply_to_message.delete()
        except:
            pass

        if message.reply_to_message:
            await message.reply(f"<b>Ты {text}</b>")
        else:
            await message.reply('<b>Только на реплей!</b>')

    elif t.lover() == '.адм' or t.lover() == '.adm':
        try:
            await message.reply_to_message.delete()
        except:
            pass
        w = 1
        qу = []
        admins = await bot.get_chat_administrators(message.chat.id)
        for i in admins:
            qу.append(f'''{w}) <a href='https://t.me/{i.user.username}'>{i.user.first_name}</a>''')
            w = w + 1
        await message.answer('\n'.join(q), disable_web_page_preview=True)

    elif t == '1':
        await message.reply(f"{message.chat.get_member_count()}")

async def on_startup():
    ADMINS = [
        910207255,
        -1001283685896,
    ]
    for admin in ADMINS:
        await bot.send_message(admin, "<b>Бот успешно запущен/перезапущен! ✅</b>")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)