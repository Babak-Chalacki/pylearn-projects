import telebot
import random
from telebot import types

bot = telebot.TeleBot("7465142195:AAF22px6dMaFjLomfnWkg6XZCI8CBuN-_Vc", parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f"{first_name} خوش آمدی!")

@bot.message_handler(commands=["game"])
def play_game(message):
    
    global current_number 
    current_number = random.randint(0, 100) 
    bot.send_message(message.chat.id, f"عدد بین 0 تا 100 را حدس بزنید!{current_number}")

@bot.message_handler(func=lambda m: True)
def handle_guess(guess_message):
    global current_number
    if current_number is None:
        # bot.send_message(guess_message.chat.id, "لطفاً ابتدا بازی را شروع کنید با دستور /game")

        
        return
    try:
            user_guess = int(guess_message.text) 
            
            if user_guess > current_number:
                bot.send_message(guess_message.chat.id, "عدد کوچک‌تر است!")
            elif user_guess < current_number:
                bot.send_message(guess_message.chat.id, "عدد بزرگ‌تر است!")
            else:
                bot.send_message(guess_message.chat.id, f"تبریک! عدد درست را حدس زدید!")
                markUp_keys = types.ReplyKeyboardMarkup(row_width=2)
                key1 = types.KeyboardButton("شروع دوباره")
                markUp_keys.add(key1)
                bot.send_message(guess_message.chat.id, "برای شروع دوباره، دکمه زیر را فشار دهید:", reply_markup=markUp_keys)
                current_number = None
    except ValueError:
            bot.send_message(guess_message.chat.id, "لطفاً یک عدد معتبر وارد کنید.")

bot.infinity_polling()