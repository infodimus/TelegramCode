import telebot

def send_message_to_channel(token, channel_name, message):
    """
    Sends a message to a Telegram channel using a bot.

    Parameters:
    - token (str): The API token of the Telegram bot.
    - channel_name (str): The username or ID of the Telegram channel.
    - message (str): The message to be sent.
    """
    # Initialize the bot with its token
    bot = telebot.TeleBot(token)

    # Send the message to the channel
    bot.send_message(channel_name, message)
    print("Message sent to the channel!")

bot_token = 'my bot token62353gd1326e32h3'  # Replace with your Telegram bot's token
channel_name = '@mychannelqwerty'  # Replace with your channel's username 
#channel_name = '-100123456789'  # Replace with your channel's ID
message = 'Hello, this is a message from my Telegram bot to the channel!'

send_message_to_channel(bot_token, channel_name, message)
