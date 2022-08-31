
from aiogram import Dispatcher, Bot, types, executor
from random import choice

bot = Bot(token='5413288721:AAFE8S-ADmbFhFmdOoeD8q4gpBLliWpVvhE', parse_mode="HTML")
dp = Dispatcher(bot)

q = ['Скамер', 'Эгоист', 'Дрочун', 'Гей', 'Красавчик', 'Урод', 'Говно', 'Шрек', 'Спонсор сахариуса', 'Хуй', 'Путин', 'Хацкер', 'Далбаёб', 'Секси', 'Любитель сосочков', 'А4', 'Файзик гей', 'Музей пидарасов', 'Диабло GAY', 'ТРАХтарист', 'Мактрахер', 'Гачи-Мучи', 'Собака', 'Олд', 'Лох', 'Длинный хуй', 'Короткий хуй', 'Понос шакала', 'Сперма дракона', 'Петушиный клюв', 'Сранимешник', 'Залупа кита', 'Милашка', 'Топ', 'Даша-путешественница']

@dp.message_handler(content_types=['text'])
async def members(message: types.Message):
    t = message.text
    if t == '.я' or t == '.Я':
        text = choice(q)
        await message.reply(f'<b>Ты {text}</b>')
    
    elif message.text == '.хелп' or message.text == '.help':
        qw = ['No Helps xD', '<b>Тебе повезло пон, ибо на это смс 50% выподения, хотя это дохуя, ладно!\n\nКароче пока ток такие команды:</b>\n<code>.адм</code> <b>|</b> <code>.adm</code> <b>-</b> <i>список админов чата</i>\n<code>.я</code> <b>|</b> <code>.ты</code> <b>-</b> <i>говорит кто ты | чел реплея</i>\n\n<code>.help</code> <b>|</b> <code>.хелп</code> <b>-</b> <i>доступные команды</i>']
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
        admins = await bot.get_chat_administrators(message.chat.id)
        for i in admins:
            qу.append(f'''{w} <a href='https://t.me/{i.username}'>{i.user.full_name}</a>''')
            w = w + 1
        await message.answer('\n'.join(qу), disable_web_page_preview=True)

    elif t == '1':
        await message.reply(f"{message.chat.get_member_count()}")

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

async def pon(dp):
    await on_startup(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=pon)
