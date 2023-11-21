import telebot
import random
import string

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '6753266245:AAGtwbl_dmzZ-6fbw98DHnyLogODXOLCKVE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_text = "Great to see you. Please use /generate <number> to use this bot!"
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown")

@bot.message_handler(commands=['generate'])
def generate_strings(message):
    try:
        # Extract the number from the command
        command_parts = message.text.split()
        num_strings = int(command_parts[1])

        # Generate strings
        strings = [generate_random_string() for _ in range(num_strings)]

        # Send the generated strings as separate messages
        for s in strings:
            bot.send_message(message.chat.id, f"Generated Code: `{s}`", parse_mode="Markdown")

    except (IndexError, ValueError):
        bot.reply_to(message, "Invalid command. Use /generate <number>")

def generate_random_string():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(7))

bot.polling()
