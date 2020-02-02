import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands = ['start'])
def start(message):
    """stic = open('media/hello.webp', 'rb')
    bot.send_sticker(message.chat.id, stic)
    bot.send_message(message.chat.id, 'Привет {0.first_name}! На связи {1.first_name}'.format(message.from_user, bot.get_me()),
    parse_mode='html')"""
    markup = types.ReplyKeyboardMarkup( resize_keyboard=True )
    itembtn1 = types.KeyboardButton('Кто ты?')
    itembtn2 = types.KeyboardButton('Дай мне рандомное число')
    itembtn3 = types.KeyboardButton('Ты тупой бот')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def function_name(message):
    if message.text == 'Кто ты?':
        bot.send_message(message.chat.id, 'Мое имя PodavanBot, я - нейросеть котрая готова обучаться!')
    elif message.text == 'Дай мне рандомное число':
        bot.send_message(message.chat.id, random.randint(0,100))
    elif message.text == 'Ты тупой бот':
        bot.send_message(message.chat.id, 'Возможно я еще глуп, но я способен обучаться')
    else:
        inlineK = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text = 'Я все сказал', callback_data='Я все сказал')
        item2 = types.InlineKeyboardButton(text = 'Таков путь', callback_data='Таков путь')
        inlineK.add(item1, item2)
        bot.send_message(message.chat.id, 'Я тебя не понял', reply_markup=inlineK)


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    try:
        if call.message:
            if call.data == 'Я все сказал':
                bot.send_message(call.message.chat.id, 'Хорошо, сэр!')
            else:
                bot.send_message(call.message.chat.id, 'Таков путь!')
    except:
        print('Поймал ошибку')
    bot.edit_message_text(chat_id=call.message.chat.id, message_id = call.message.message_id,text='Я тебя не понял', reply_markup=None)
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="$$$$ЭТО мое уведомленt$$$$")
bot.polling(none_stop = True)
