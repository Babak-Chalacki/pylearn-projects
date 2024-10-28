import telebot
import random
import os
import gtts
from telebot import types
from persiantools.jdatetime import JalaliDate 
bot = telebot.TeleBot("7465142195:AAF22px6dMaFjLomfnWkg6XZCI8CBuN-_Vc", parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f"{first_name} خوش آمدی!")
    bot.send_message(message.chat.id,"برای بازی کردن => /game \n محاسبه تاریخ تولد => /age \n تبدیل متن به صدا => /voice \n نمایش بزرگترین عدد => /max \n نمایش بزرگترین اندیس => /argmax")
@bot.message_handler(commands=['menu'])
@bot.message_handler(func=lambda m:m.text == "منو")
def menu(message):
    bot.send_message(message.chat.id,"برای بازی کردن => /game \n محاسبه تاریخ تولد => /age \n تبدیل متن به صدا => /voice \n نمایش بزرگترین عدد => /max \n نمایش بزرگترین اندیس => /argmax")
    
@bot.message_handler(commands=["age"])
def ask_for_birth_date(message):
    bot.send_message(message.chat.id, "لطفاً تاریخ تولد خود را به صورت خورشیدی وارد کنید (سال/ماه/روز)")
    bot.send_message(message.chat.id,"به عنوان مثال 1382/10/27")

@bot.message_handler(func=lambda message: message.text.count('/') == 2 and all(part.isdigit() for part in message.text.split('/')))
def calculate_age(message):
    try:
        year, month, day = map(int, message.text.split('/'))
        birthdate = JalaliDate(year, month, day)
        today = JalaliDate.today()
        
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
            
        bot.send_message(message.chat.id, f"سن شما: {age} سال")
    except Exception as e:
        bot.send_message(message.chat.id, "لطفاً تاریخ صحیحی وارد کنید.")
        
    
    
@bot.message_handler(commands=['argmax'])
def voice_handler(message):
    bot.reply_to(message,"رشته اعداد خود را وارد کنید")
   
   
@bot.message_handler(func=lambda m: True)
def find_argmax_index(message):
    try:
        number_list = [int(num) for num in message.text.split(',')]
        
        max_value = max(number_list)
        max_index = number_list.index(max_value)
        
        bot.send_message(message.chat.id, f"اندیس بزرگترین عدد ({max_value}): {max_index}")
    except ValueError:
        bot.send_message(message.chat.id, "لطفاً اعداد صحیح وارد کنید.")
        
        
    
@bot.message_handler(commands=['max'])
def voice_handler(message):
    bot.reply_to(message,"رشته اعداد خود را وارد کنید")
    
@bot.message_handler(func=lambda m: True)
def find_max_number(message):
    try:
        number_list = [int(num) for num in message.text.split(',')]
        
        max_value = max(number_list)
        
        bot.send_message(message.chat.id, f"بزرگترین عدد: {max_value}")
    except ValueError:
        bot.send_message(message.chat.id, "لطفاً اعداد صحیح وارد کنید.")

    
    
    
    

      
        
        
        
@bot.message_handler(commands=['voice'])
def voice_handler(message):
    marker_keys = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    menuKey = types.KeyboardButton("منو")
    marker_keys.add(menuKey)
    bot.reply_to(message,"جمله خود را به صورت انگلیسی وارد کنید",reply_markup=marker_keys)
 
@bot.message_handler(func=lambda m:True)
def voice_creator(message):
 try:
        tts = gtts.gTTS(message.text.strip(), lang="en", slow=False) 
        tts.save('voice.mp3')
        
        with open('voice.mp3', 'rb') as audio_file:
            bot.send_audio(message.chat.id, audio_file)
        os.remove('voice.mp3')
        empty_key = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,"برای ارسال دوباره /voice را وارد کنید",reply_markup=empty_key)
        
 except Exception as e:
        bot.reply_to(message, "خطا در پردازش: " + str(e))

    
        

        
current_number = None
@bot.message_handler(commands=["game"])
@bot.message_handler(func=lambda m: m.text == "شروع دوباره")
def play_game(message):
    global current_number
    current_number = random.randint(0,100)
    marker_key = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    newGame = types.KeyboardButton("شروع دوباره")
    marker_key.add(newGame)
    bot.send_message(message.chat.id,f"یک شمار بین 0 تا 100 انتخاب کنید",reply_markup=marker_key)
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
            empty_keyboard = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, "بازی تمام شد.", reply_markup=empty_keyboard)
            
    except ValueError:
        bot.send_message(message.chat.id,"لطفا شمار مناسب وارد کنید")
     
    
    
  
bot.infinity_polling()