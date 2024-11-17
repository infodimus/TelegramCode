import telebot
import requests
import smtplib
from datetime import datetime


   
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

def get_current_time():
    # datetime object containing current date and time
    now = datetime.now()
     
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    print("date and time =", dt_string)
    return dt_string



def get_exchange_rate(from_currency, to_currency):
    """
    Fetches the exchange rate from one currency to another using an API.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        exchange_rate = data['rates'][to_currency]
        return exchange_rate
    except Exception as e:
        return f"Error: {e}"


# Get exchange rates
usd_to_rub = get_exchange_rate("USD", "RUB")
eur_to_rub = get_exchange_rate("EUR", "RUB")
cny_to_rub = get_exchange_rate("CNY", "RUB")
ils_to_rub = get_exchange_rate("ILS", "RUB")

# Prepare message

dt_string = get_current_time()




bot_token = 'xxxxxxxx:yyyyyyyyy-zzzzzzzzzzzzzzzzzzzzzz'  # Replace with your Telegram bot's token
channel_name = '@channel_name'  # Replace with your channel's username or ID

message = (
    f"Currency Exchange Rates as of {dt_string}\n\n"
    f"1 USD = {usd_to_rub} RUB\n"
    f"1 EUR = {eur_to_rub} RUB\n"
    f"1 Chinese Yuan = {cny_to_rub} RUB\n"
    f"1 Israeli New Shekel = {ils_to_rub} RUB\n"
)


send_message_to_channel(bot_token, channel_name, message)




