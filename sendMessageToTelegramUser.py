# Do not forget
# pip install pyTelegramBotAPI

import telebot

bot_token = 'my bot token 3264324286428323457qqq'  # Replace with your Telegram bot's token
message = 'Hello, this is a test message from my Telegram bot!'

#chat_id of the destination user
chat_id = "1234567890" # Replace with user_id/chat_id of the destination user

def send_telegram_message(token, chat_id, message):
    """
    Sends a message to a specific Telegram chat using a bot.

    Parameters:
    - token (str): The API token of the Telegram bot.
    - chat_id (str): The chat ID of the recipient.
    - message (str): The message to be sent.
    """
    # Initialize the bot with its token
    bot = telebot.TeleBot(token)

    # Send the message
    bot.send_message(chat_id, message)
    print("Message sent!")


send_telegram_message(bot_token, chat_id, message)
