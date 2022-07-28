import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/start', '/help', '/setup')
    bot.send_message(message.chat.id, f"Hello {message.from_user.username}!", reply_markup=keyboard)


@bot.message_handler(commands=['search'])
def search(message):
    bot.send_message(message.chat.id, "Search information!")


@bot.message_handler(commands=['buttons'])
def buttons(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Btn1', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Btn2', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Btn3', callback_data=3))
    bot.send_message(message.chat.id, "Show buttons!", reply_markup = markup)


@bot.callback_query_handler(func=lambda call:True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id = call.id, text='You select some button!')
    answer = ''
    if call.data == '1':
        answer = 'It was 1!'
    elif call.data == '2':
        answer = 'It was 2!'
    elif call.data == '3':
        answer = 'It was 3!'
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id) # hide buttons




# bot.polling()
bot.infinity_polling(timeout=10, long_polling_timeout = 5)