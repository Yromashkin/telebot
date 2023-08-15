import telebot
from telebot import types

token = "5901048500:AAGl0OC0TaHAResbHFd30Q4VyV4UBLWwVBQ"
url = "https://api.telegram.org/bot"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])    
def start(message):
    bot.send_message(message.chat.id, 'Привет меня зовут WebinariyBOT! \nЯ буду Вашим помощником в создании Вашей лучшей трансляции! \nЕсли хотите узнать о моих дополнительных функиях введите команду /help')

@bot.message_handler(commands=['video'])    
def video(message):
    btnvideo = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    btnexample1 = types.KeyboardButton("Пример видео малой студии")
    btnexample2 = types.KeyboardButton("Пример видео средней студии")
    btnexample3 = types.KeyboardButton("Пример видео большой светлой студии")
    btnexample4 = types.KeyboardButton("Пример видео большой темной студии")
    btnvideo.add(btnexample1, btnexample2, btnexample3, btnexample4)
    bot.send_message(message.chat.id, 'Выберете пример студии, которой Вы хотите посмотреть', reply_markup=btnvideo)

@bot.message_handler(content_types=['text'])
def textvideo(message):
    message.text == 'Пример видео малой студии'
    video = open('video/small.mp4', 'rb')
    bot.send_video(message.chat.id, video)
    btnvideo = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    btnexample1 = types.KeyboardButton("Пример видео малой студии")
    btnexample2 = types.KeyboardButton("Пример видео средней студии")
    btnexample3 = types.KeyboardButton("Пример видео большой светлой студии")
    btnexample4 = types.KeyboardButton("Пример видео большой темной студии")
    btnvideo.add(btnexample1, btnexample2, btnexample3, btnexample4)
    bot.send_message(message.chat.id, 'Выберете пример студии, которой Вы хотите посмотреть', reply_markup=btnvideo)

@bot.message_handler(content_types=['text'])
def textvideo(message):
    message.text == 'Пример видео средней студии'
    video = open('video/midle.mp4', 'rb')
    bot.send_video(message.chat.id, video)
    btnvideo = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    btnexample1 = types.KeyboardButton("Пример видео малой студии")
    btnexample2 = types.KeyboardButton("Пример видео средней студии")
    btnexample3 = types.KeyboardButton("Пример видео большой светлой студии")
    btnexample4 = types.KeyboardButton("Пример видео большой темной студии")
    btnvideo.add(btnexample1, btnexample2, btnexample3, btnexample4)
    bot.send_message(message.chat.id, 'Выберете пример студии, которой Вы хотите посмотреть', reply_markup=btnvideo)

@bot.message_handler(content_types=['text'])
def textvideo(message):
    message.text == 'Пример видео большой светлой студии'
    video = open('video/big_light.mp4', 'rb')
    bot.send_video(message.chat.id, video)
    btnvideo = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    btnexample1 = types.KeyboardButton("Пример видео малой студии")
    btnexample2 = types.KeyboardButton("Пример видео средней студии")
    btnexample3 = types.KeyboardButton("Пример видео большой светлой студии")
    btnexample4 = types.KeyboardButton("Пример видео большой темной студии")
    btnvideo.add(btnexample1, btnexample2, btnexample3, btnexample4)
    bot.send_message(message.chat.id, 'Выберете пример студии, которой Вы хотите посмотреть', reply_markup=btnvideo)

@bot.message_handler(content_types=['text'])
def textvideo(message):
    message.text == 'Пример видео большой темной студии'
    video = open('video/big_shadow.mp4', 'rb')
    bot.send_video(message.chat.id, video)
    btnvideo = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    btnexample1 = types.KeyboardButton("Пример видео малой студии")
    btnexample2 = types.KeyboardButton("Пример видео средней студии")
    btnexample3 = types.KeyboardButton("Пример видео большой светлой студии")
    btnexample4 = types.KeyboardButton("Пример видео большой темной студии")
    btnvideo.add(btnexample1, btnexample2, btnexample3, btnexample4)
    bot.send_message(message.chat.id, 'Выберете пример студии, которой Вы хотите посмотреть', reply_markup=btnvideo)

@bot.message_handler(commands=['foto'])    
def foto(message):
    btnfoto = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    btnfoto1 = types.KeyboardButton("Пример фото малой студии")
    btnfoto2 = types.KeyboardButton("Пример фото средней студии")
    btnfoto3 = types.KeyboardButton("Пример фото большой светлой студии")
    btnfoto4 = types.KeyboardButton("Пример фото большой темной студии")
    btnfoto.add(btnfoto1, btnfoto2, btnfoto3, btnfoto4)
    bot.send_message(message.chat.id, 'Выберете пример студии, которой Вы хотите посмотреть', reply_markup=btnfoto)

@bot.message_handler(content_types=['text'])
def textfoto(message):
    message.text == 'Пример фото малой студии'
    bot.send_media_group(message.chat.id, [      
     telebot.types.InputMediaPhoto(open('img/small/small.png', 'rb')),      
     telebot.types.InputMediaPhoto(open('img/small/small1.jpeg', 'rb')),
     telebot.types.InputMediaPhoto(open('img/small/small2.jpeg', 'rb')),      
     telebot.types.InputMediaPhoto(open('img/small/small3.jpeg', 'rb')) ])
    btnfoto = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    btnfoto1 = types.KeyboardButton("Пример фото малой студии")
    btnfoto2 = types.KeyboardButton("Пример фото средней студии")
    btnfoto3 = types.KeyboardButton("Пример фото большой светлой студии")
    btnfoto4 = types.KeyboardButton("Пример фото большой темной студии")
    btnfoto.add(btnfoto1, btnfoto2, btnfoto3, btnfoto4)
    bot.send_message(message.chat.id, 'Выберете пример студии, которой Вы хотите посмотреть', reply_markup=btnfoto)

@bot.message_handler(content_types=['text'])
def textfoto(message):
    if message.text == 'Пример фото малой студии':
       file = open('img/small.png', 'rb')
    bot.send_photo(message.chat.id, file)
    btnfoto = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    btnfoto1 = types.KeyboardButton("Пример фото малой студии")
    btnfoto2 = types.KeyboardButton("Пример фото средней студии")
    btnfoto3 = types.KeyboardButton("Пример фото большой светлой студии")
    btnfoto4 = types.KeyboardButton("Пример фото большой темной студии")
    btnfoto.add(btnfoto1, btnfoto2, btnfoto3, btnfoto4)
    bot.send_message(message.chat.id, 'Выберете пример студии, которой Вы хотите посмотреть', reply_markup=btnfoto)

@bot.message_handler(content_types=['text'])
def textfoto(message):
    if message.text == 'Пример фото малой студии':
       file = open('img/small.png', 'rb')
    bot.send_photo(message.chat.id, file)
    btnfoto = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    btnfoto1 = types.KeyboardButton("Пример фото малой студии")
    btnfoto2 = types.KeyboardButton("Пример фото средней студии")
    btnfoto3 = types.KeyboardButton("Пример фото большой светлой студии")
    btnfoto4 = types.KeyboardButton("Пример фото большой темной студии")
    btnfoto.add(btnfoto1, btnfoto2, btnfoto3, btnfoto4)
    bot.send_message(message.chat.id, 'Выберете пример студии, которой Вы хотите посмотреть', reply_markup=btnfoto)

@bot.message_handler(content_types=['text'])
def textfoto(message):
    if message.text == 'Пример фото малой студии':
       file = open('img/small.png', 'rb')
    bot.send_photo(message.chat.id, file)
    btnfoto = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    btnfoto1 = types.KeyboardButton("Пример фото малой студии")
    btnfoto2 = types.KeyboardButton("Пример фото средней студии")
    btnfoto3 = types.KeyboardButton("Пример фото большой светлой студии")
    btnfoto4 = types.KeyboardButton("Пример фото большой темной студии")
    btnfoto.add(btnfoto1, btnfoto2, btnfoto3, btnfoto4)
    bot.send_message(message.chat.id, 'Выберете пример студии, которой Вы хотите посмотреть', reply_markup=btnfoto)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Список команд: \n/info - показывает всю актуальную информацию о нашей организации; \n/example - показывает примеры наших студий; \n/foto - показывает фото наших студий /start выбор студии для бронирования;')

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Наши контакты \nтел: 8 (499) 322 37 62 \nпочта: zakaz@webinariy.pro \nадрес: Мясницкая улица д. 13, с. 18, Москва ООО «ВЕБИНАРИЙ» Адрес: 101000, г. Москва, ул. Мясницкая, д.13с18-18А')

bot.infinity_polling(none_stop=True)