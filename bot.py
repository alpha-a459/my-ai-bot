import telebot
import google.generativeai as genai
import os

# ضع توكن تليجرام هنا
TELEGRAM_TOKEN = "8464625663:AAFptD3bd2VajufVxMAOOe50qtpRQhmLGfk"
# ضع مفتاح جوجل هنا
GEMINI_KEY = "AIzaSyByO1EWE7Po4-wDjL5iKJh0krOHCFebu48"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "حدث خطأ في معالجة الطلب")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
