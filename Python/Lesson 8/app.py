import telebot
import scripts


from config import TOKEN


# # Погода - Parse (температура зараз (відчувається), мін, макс, )
# # Курс валют - API (USD, EUR, PLN)
# # Ковід інф - API інфа по україні
# # Орки - Parse - втрати*


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    preview_message = "Тут можна побачити всяку інфу."
    bot.send_message(message.chat.id, f"Вітаю {message.from_user.username}! {preview_message}")


@bot.message_handler(commands=['buttons'])
def buttons(message):
    markup = telebot.types.InlineKeyboardMarkup() 
    markup.add(telebot.types.InlineKeyboardButton(text='🌡️ Погода на сьогодні', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='💵 Курс валют', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='😷 Ковід інформація', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='💀 Оркопад', callback_data=4))
    bot.send_message(message.chat.id, "Show buttons!", reply_markup = markup)


@bot.callback_query_handler(func=lambda call:True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id = call.id, text='You select some button!')
    answer = ''
    if call.data == '1':
        photo, data = scripts.weather()
        bot.send_photo(call.message.chat.id, caption=data, photo=photo, parse_mode='HTML')
    elif call.data == '2':
        photo, data = scripts.courses()
        bot.send_photo(call.message.chat.id, caption=data, photo=photo, parse_mode='HTML')
    elif call.data == '3':
        photo, data = scripts.covid()
        bot.send_photo(call.message.chat.id, caption=data, photo=photo, parse_mode='HTML')
    elif call.data == '4':
        photo, data = scripts.ork()
        bot.send_photo(call.message.chat.id, caption=data, photo=photo, parse_mode='HTML')


bot.infinity_polling(timeout=10, long_polling_timeout = 5)