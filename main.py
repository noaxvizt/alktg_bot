from aiogram import Bot, executor, Dispatcher
from config import *
import os
from pdf_work import make_pdf
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
blackwhite_color_mode = 1
from email_work import send_email
"""
0-black_white
1-color
"""


def get_length_in_dir(dir_path):
    files = os.listdir(path=dir_path)
    print(len(files), dir_path)
    return len(files)


@dp.message_handler(commands=["start"])
async def start(message):
    await message.delete()
    await message.answer(text="Это бот для конвертации фото в пдф"
                              "\nПришлите мне свои фото. После отправьте команду /end"
                              "\nПоменять режим на черно-белый /blackwhite, на цветной /color")
    global status_num
    status_num = 1
    if 'bot' + str(message.chat.id) not in os.listdir("data"):
        os.mkdir('data/bot' + str(message.chat.id))
    else:
        for i in os.listdir('data/bot' + str(message.chat.id)):
            try:
                os.remove(f'data/bot' + str(message.chat.id) + '/' + i)
            except Exception:
                pass


@dp.message_handler(commands=['end'])
async def send_image(message):
    make_pdf(f'data/bot{message.chat.id}', blackwhite_color_mode)
    document = open(f"data/bot{message.chat.id}/pdf_file.pdf", 'rb')
    await bot.send_document(chat_id=message.chat.id, document=document)
    await bot.send_message(chat_id=message.chat.id, text="Хотите отправить пдф на почту. "
                                                         "Если да то используйте "
                                                         "{/send адрес тема_сообщения}")


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    try:
        await message.photo[-1].download(f'data/bot{message.chat.id}/image{get_length_in_dir(f"data/bot{message.chat.id}") + 1}.jpg')
    except TypeError:
        await message.answer(text="Произошла ошибка, нажмите /start чтобы начать сначала")


@dp.message_handler(commands=['color'])
async def color(message):
    global blackwhite_color_mode
    blackwhite_color_mode = 1
    await bot.send_message(chat_id=message.chat.id,
                           text='Режим поменян на цветной')


@dp.message_handler(commands=['blackwhite'])
async def wlackwhite(message):
    global blackwhite_color_mode
    blackwhite_color_mode = 0
    await bot.send_message(chat_id=message.chat.id,
                           text='Режим поменян на черно-белый')


@dp.message_handler(commands=['send'])
async def email(message):
    print(message.text)
    await send_email(message.text.split()[1], f"data/bot{message.chat.id}/pdf_file.pdf", message.text.split()[1])
    await bot.send_message(chat_id=message.chat.id,
                           text="Отправлено")


@dp.message_handler()
async def echo(message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Пришлите мне фото, либо нажмите /start чтобы начать сначала')

if __name__ == '__main__':
    executor.start_polling(dp)