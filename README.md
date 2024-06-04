# Telegram Forward Bot

This is a Telegram bot built with the `python-telegram-bot` library. The bot forwards messages sent to it to a specified Telegram user (the bot owner) and allows the owner to reply to those messages, which are then sent back to the original sender without revealing the owner's identity. It also includes a `/start` command to welcome users when they first interact with the bot.

## Features

- Forwards messages from users to the bot owner.
- Allows the bot owner to reply to users anonymously.
- Provides a welcome message with the `/start` command.

## Prerequisites

- Python 3.7+
- Telegram bot token

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/proxygod/telegram-forward-bot.git
    cd telegram-forward-bot
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add your Telegram bot token and your Telegram Chat ID:
    ```plaintext
    TELEGRAM_TOKEN = your-telegram-bot-token
    YOUR_TELEGRAM_ID = your-telegram-chat-id
    ```

## Usage

1. Run the bot:
    ```bash
    python bot.py
    ```

2. Start a conversation with your bot on Telegram by sending the `/start` command.

3. Send messages to the bot, and they will be forwarded to the bot owner.

4. The bot owner can reply to forwarded messages, and the replies will be sent back to the original sender without revealing the owner's identity.

## Files

- `bot.py`: The main script that runs the bot.
- `requirements.txt`: A list of dependencies required for the bot.
- `.env`: A file to store environment variables (not included in the repository).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library for providing the framework to build Telegram bots easily.

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. Contributions are welcome!

## Contact

For any inquiries or issues, please reach out to `your.email@example.com`.

