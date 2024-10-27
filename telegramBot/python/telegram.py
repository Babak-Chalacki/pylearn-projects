import random
import telebot
from telebot import types

markUp_keyboard = types.ReplyKeyboardMarkup(row_width=3)
key1 = types.KeyboardButton('برگشت به عقب =>')
key2 = types.KeyboardButton('فال حافظ')
key3 = types.KeyboardButton('ماشین حساب')
key4 = types.KeyboardButton('راهنما')
key5 = types.KeyboardButton('چت بات')
key6 = types.KeyboardButton('دانلود')
markUp_keyboard.add(key1,key2,key3,key4,key5,key6)


bot = telebot.TeleBot("7465142195:AAF22px6dMaFjLomfnWkg6XZCI8CBuN-_Vc", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "چطوری جونه دل, سره کیفی عزیز!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'چطور می‌توانم کمکت کنم؟')


@bot.message_handler(commands=['fal'])
def send_fal(message):
    fal_list = [
        'به سفر خواهی رفت',
        'به فنا میری',
        'به خاک میری'
    ]
    selected_fal = random.choice(fal_list)
    bot.send_message(message.chat.id, selected_fal)





@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "درود":
        bot.send_message(message.chat.id, "بازم عشقی")
    elif message.text == "خوبی":
        bot.send_message(message.chat.id, "خیلی عشقی")
    elif message.text == "جون":
        photo = open('telegramBot/m.jpg','rb')
        bot.send_photo(message.chat.id,photo)
    else:
        bot.send_message(message.chat.id, "پیام شما دریافت شد.", reply_markup=markUp_keyboard)

bot.infinity_polling()