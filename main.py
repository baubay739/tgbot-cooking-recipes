import telebot

bot_token = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
channel_id = '@YOUR_TELEGRAM_CHANNEL_NAME_HERE'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['recipe'])
def handle_recipe(message):
    # This function is triggered when the user sends the command "/recipe"

    # Get the recipe text, photo, and video from the user's message
    recipe_text = message.text.split('/recipe ')[1]
    photo_file_id = message.photo[-1].file_id
    video_file_id = message.video.file_id

    # Send the recipe to the designated Telegram channel
    bot.send_message(channel_id, recipe_text)
    bot.send_photo(channel_id, photo_file_id)
    bot.send_video(channel_id, video_file_id)

bot.polling()
