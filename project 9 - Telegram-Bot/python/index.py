import telebot
import random
import os
import gtts
import qrcode  
from telebot import types
from persiantools.jdatetime import JalaliDate 

bot = telebot.TeleBot("TOKEN", parse_mode=None)

user_states = {}

STATE_GAME = "game"
STATE_VOICE = "voice"
STATE_AGE = "age"
STATE_ARGMAX = "argmax"
STATE_MAX = "max"
STATE_QRCODE = "qrcode"  
@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f"{first_name} خوش آمدی!")
    show_menu(message)

def show_menu(message):
    bot.send_message(message.chat.id, "برای بازی کردن => /game \n محاسبه تاریخ تولد => /age \n تبدیل متن به صدا => /voice \n نمایش بزرگترین عدد => /max \n نمایش بزرگترین اندیس => /argmax \n تولید QR Code => /qrcode \n نمایش راهنما => /help")

@bot.message_handler(commands=['menu'])
@bot.message_handler(func=lambda m: m.text == "منو")
def menu(message):
    show_menu(message)

@bot.message_handler(commands=["age"])
def ask_for_birth_date(message):
    bot.send_message(message.chat.id, "لطفاً تاریخ تولد خود را به صورت خورشیدی وارد کنید (سال/ماه/روز)\nبه عنوان مثال 1382/10/27")
    user_states[message.chat.id] = STATE_AGE

@bot.message_handler(func=lambda message: message.chat.id in user_states and user_states[message.chat.id] == STATE_AGE)
def calculate_age(message):
    try:
        year, month, day = map(int, message.text.split('/'))
        birthdate = JalaliDate(year, month, day)
        today = JalaliDate.today()
        
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
            
        bot.send_message(message.chat.id, f"سن شما: {age} سال")
        del user_states[message.chat.id]

    except Exception:
        bot.send_message(message.chat.id, "لطفاً تاریخ صحیحی وارد کنید.")

@bot.message_handler(commands=['argmax'])
def argmax_prompt(message):
    bot.reply_to(message,"رشته اعداد خود را وارد کنید (مثال: 1,2,3)")
    user_states[message.chat.id] = STATE_ARGMAX

@bot.message_handler(func=lambda m: m.chat.id in user_states and user_states[m.chat.id] == STATE_ARGMAX)
def find_argmax_index(message):
    try:
        number_list = [int(num) for num in message.text.split(',')]
        
        max_value = max(number_list)
        max_index = number_list.index(max_value)
        
        bot.send_message(message.chat.id, f"اندیس بزرگترین عدد ({max_value}): {max_index}")
        del user_states[message.chat.id]

    except ValueError:
        bot.send_message(message.chat.id, "لطفاً اعداد صحیح وارد کنید.")

@bot.message_handler(commands=['max'])
def max_prompt(message):
    bot.reply_to(message,"رشته اعداد خود را وارد کنید (مثال: 1,2,3)")
    user_states[message.chat.id] = STATE_MAX

@bot.message_handler(func=lambda m: m.chat.id in user_states and user_states[m.chat.id] == STATE_MAX)
def find_max_number(message):
    try:
        number_list = [int(num) for num in message.text.split(',')]
        
        max_value = max(number_list)
        
        bot.send_message(message.chat.id, f"بزرگترین عدد: {max_value}")
        del user_states[message.chat.id]

    except ValueError:
        bot.send_message(message.chat.id, "لطفاً اعداد صحیح وارد کنید.")

@bot.message_handler(commands=['voice'])
def voice_prompt(message):
    marker_keys = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    menuKey = types.KeyboardButton("منو")
    marker_keys.add(menuKey)
    bot.reply_to(message,"جمله خود را به صورت انگلیسی وارد کنید", reply_markup=marker_keys)
    
    user_states[message.chat.id] = STATE_VOICE

@bot.message_handler(func=lambda m: m.chat.id in user_states and user_states[m.chat.id] == STATE_VOICE)
def voice_creator(message):
    if message.text == "منو":
        show_menu(message)
        return
    
    try:
        tts = gtts.gTTS(message.text.strip(), lang="en", slow=False) 
        tts.save('voice.mp3')
        
        with open('voice.mp3', 'rb') as audio_file:
            bot.send_audio(message.chat.id, audio_file)
        
        os.remove('voice.mp3')
        
        empty_key = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,"برای ارسال دوباره /voice را وارد کنید", reply_markup=empty_key)
        
        del user_states[message.chat.id]
        
    except Exception as e:
        bot.reply_to(message, "خطا در پردازش: " + str(e))

@bot.message_handler(commands=["game"])
def play_game_start(message):
    user_states[message.chat.id] = random.randint(0, 100)
    
    marker_key = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    newGame = types.KeyboardButton("شروع دوباره")
    marker_key.add(newGame)
    
    bot.send_message(message.chat.id,"یک شمار بین 0 تا 100 انتخاب کنید", reply_markup=marker_key)

@bot.message_handler(func=lambda m: m.chat.id in user_states and isinstance(user_states[m.chat.id], int))
def guess_handler(message):
    try:
        user_number = int(message.text)
        current_number = user_states[message.chat.id]
        
        if current_number > user_number:
            bot.reply_to(message,"بزرگ تر")
        elif current_number < user_number:
            bot.reply_to(message,"کوچک تر")
        else:
            bot.send_message(message.chat.id,"آفرین")
            del user_states[message.chat.id]
            empty_keyboard = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, "بازی تمام شد.", reply_markup=empty_keyboard)

    except ValueError:
        bot.send_message(message.chat.id,"لطفا شمار مناسب وارد کنید")

@bot.message_handler(commands=['qrcode'])
def qrcode_prompt(message):
    bot.send_message(message.chat.id, "لطفاً متنی که می‌خواهید QR Code آن تولید شود را وارد کنید.")
    user_states[message.chat.id] = STATE_QRCODE  
@bot.message_handler(func=lambda m: m.chat.id in user_states and user_states[m.chat.id] == STATE_QRCODE)
def generate_qrcode(message):
    try:
        qr_img = qrcode.make(message.text.strip())
        
        qr_img_path = 'qrcode.png'
        qr_img.save(qr_img_path)

        with open(qr_img_path, 'rb') as qr_file:
            bot.send_photo(chat_id=message.chat.id, photo=qr_file)

        os.remove(qr_img_path)

        del user_states[message.chat.id] 

    except Exception as e:
        bot.reply_to(message, f"خطا در تولید QR Code: {str(e)}")

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "دستورات موجود:\n"
        "/start - خوش آمدگویی\n"
        "/menu - نمایش منو\n"
        "/age - محاسبه سن\n"
        "/argmax - پیدا کردن اندیس بزرگترین عدد\n"
        "/max - پیدا کردن بزرگترین عدد\n"
        "/voice - تبدیل متن به صدا\n"
        "/game - بازی حدس عدد\n"
        "/qrcode - تولید QR Code از متن\n"
        "/help - نمایش این راهنما"
    )
    bot.send_message(chat_id=message.chat.id, text=help_text)

bot.infinity_polling()