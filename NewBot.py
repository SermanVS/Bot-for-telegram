import telebot
import os
import time
bot = telebot.TeleBot('')

@bot.message_handler(content_types = ["text"])
def find_file_ids(message):
    for file in os.listdir('botphotos/'):
        if file.split('.')[-1] == 'jpg':
            f = open('botphotos/'+file, 'rb')
            res = bot.send_photo(message.chat.id, f, None)
            print(res.photo[1])
        time.sleep(3)
        

if __name__ == '__main__':
    bot.polling(none_stop=True)
