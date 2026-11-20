import telebot
TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
bot.reply_to(message, "أهلاً بك في متجرنا! كيف يمكنني مساعدتك اليوم؟")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
bot.reply_to(message, "وصلت رسالتك! جاري معالجة طلبك.")
bot.polling()
