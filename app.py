import os
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import BotCommand

# Load environment variables from .env file
load_dotenv()

# Get necessary configuration details from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
YOUR_TELEGRAM_ID = int(os.getenv("YOUR_TELEGRAM_ID"))

# Dictionary to store user IDs and their corresponding chat IDs
user_chat_ids = {}

# Define the message handler function
def forward_message(update, context):
    # Store the user's chat ID
    user_chat_ids[update.message.from_user.id] = update.message.chat_id

    # Forward the message to your Telegram ID
    if update.message.from_user.id != YOUR_TELEGRAM_ID:
        context.bot.forward_message(chat_id=YOUR_TELEGRAM_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

# Define the reply handler function
def reply_to_sender(update, context):
    # Check if the reply is from the bot owner
    if update.message.from_user.id == YOUR_TELEGRAM_ID:
        # Get the chat ID of the original sender
        original_chat_id = user_chat_ids.get(update.message.reply_to_message.forward_from.id)
        if original_chat_id:
            # Copy the owner's message to the original sender, hiding original sender details
            context.bot.copy_message(chat_id=original_chat_id,
                                      from_chat_id=update.message.chat_id,
                                      message_id=update.message.message_id)

# Define the start command handler
def start(update, context):
    # Send a welcome message when user first interacts with the bot
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Dhihub.")
    context.bot.send_message(chat_id=update.effective_chat.id, text="To join Dhihub Premium, please request for the payment details.")
    context.bot.send_message(chat_id=update.effective_chat.id, text="You would be added to the Premium Channel once the payment is completed.")
    # Set the bot's description
    context.bot.set_my_commands([BotCommand("start", "Request for more details.")])
    context.bot.set_description("You can chat with me and request for prices and other inquiries for Dhihub Premium.")  # Add your bot description here

def main():
    # Initialize the Telegram bot
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register the start command handler
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)

    # Register the message handler for text messages
    text_handler = MessageHandler(Filters.text & (~Filters.command), forward_message)
    dispatcher.add_handler(text_handler)

    # Register the message handler for other types of messages
    dispatcher.add_handler(MessageHandler(~Filters.command, forward_message))

    # Register the reply handler with a higher priority than the message handler
    dispatcher.add_handler(MessageHandler(~Filters.command, reply_to_sender), group=1)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
