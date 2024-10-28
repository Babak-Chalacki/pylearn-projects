import telebot
import random
from telebot import types
from persiantools.jdatetime import JalaliDate 
bot = telebot.TeleBot("7465142195:AAF22px6dMaFjLomfnWkg6XZCI8CBuN-_Vc", parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f"{first_name} خوش آمدی!")
    bot.send_message(message.chat.id,"برای بازی کردن => /game \n محاسبه تاریخ تولد => /age \n تبدیل متن به صدا => /voice \n نمایش بزرگترین عدد => /max \n نمایش بزرگترین اندیس => /argmax")
@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(message.chat.id,"برای بازی کردن => /game \n محاسبه تاریخ تولد => /age \n تبدیل متن به صدا => /voice \n نمایش بزرگترین عدد => /max \n نمایش بزرگترین اندیس => /argmax")
    
@bot.message_handler(commands=["age"])
def exchange_age(message):
        bot.send_message(message.chat.id,"تاریخ خود را به صورت خورشیدی وارد کنید")

@bot.message_handler(func=lambda message: message.text.count('/') == 2 and all(part.isdigit() for part in message.text.split('/')))
def calculate_age(message):
    try:
        birth_date_str = message.text.split('/')
        year = int(birth_date_str[0])
        month = int(birth_date_str[1])
        day = int(birth_date_str[2])
        birthdate = JalaliDate(year, month, day)
        today = JalaliDate.today()
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        bot.send_message(message.chat.id, f"سن شما: {age} سال")
    
    except Exception as e:
        bot.send_message(message.chat.id, "تاریخ وارد شده نامعتبر است. لطفا دوباره تلاش کنید.")

current_number = None
@bot.message_handler(commands=["game"])
def play_game(message):
    global current_number
    current_number = random.randint(0,100)
    bot.send_message(message.chat.id,f"send a number between 0 and 100")

@bot.message_handler(func=lambda m:True)
def guess_handler(message):
    global current_number
    if current_number is None:
     bot.send_message(message.chat.id,"برای بازی کردن => /game \n محاسبه تاریخ تولد => /age \n تبدیل متن به صدا => /voice \n نمایش بزرگترین عدد => /max \n نمایش بزرگترین اندیس => /argmax")
     return
    try:
        user_number = int(message.text)
        if current_number > user_number:
            bot.reply_to(message,"بزرگ تر")
        elif current_number < user_number:
            bot.reply_to(message,"کوچک تر")
        else:
            bot.send_message(message.chat.id,"آفرین")
            current_number = None
            
    except ValueError:
        bot.send_message(message.chat.id,"لطفا شمار مناسب وارد کنید")
     
    
    
    
    
    




@bot.message_handler(commands=['voice'])
def voice_handler(message):
    bot.reply_to(message,"جمله خود را به صورت انگلیسی وارد کنید")
   
   
   
   
   
   
   
   
   
   
    
@bot.message_handler(commands=['max'])
def voice_handler(message):
    bot.reply_to(message,"رشته اعداد خود را وارد کنید")
    
    
    
    
    
    
    
    
    
    
@bot.message_handler(commands=['argmax'])
def voice_handler(message):
    bot.reply_to(message,"رشته اعداد خود را وارد کنید")
   
   
   
   
   
    
bot.infinity_polling()