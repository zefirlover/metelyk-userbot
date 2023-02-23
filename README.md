# Metelyk Userbot 🦋

Metelyk Userbot is a project that uses a self-operated Telegram account that is using to set reactions to every post in some Telegram channel written on python using a Pyrogram framework. Documentation for Pyrogram can be found here: https://docs.pyrogram.org/

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

To set up project locally you need to have an up to date version of Python to be installed in your system. We recommend using the latest versions of both Python 3 and pip. Then, you can use:

```
git clone https://github.com/zefirlover/metelyk-userbot.git
```

to downloan a project. Then, go to project folder and use _pip_ to install Pyrogram:

```
pip3 install -U pyrogram
``` 

More installing options you can found here: https://docs.pyrogram.org/intro/install

## Running the project

First, to start a bot, you need to set some variables in script.py:

```
api_id = "your_api_id"
api_hash = "your_api_hash"

chat_id = "your_channel_id"
reaction = "🤡" # your reaction
```

You need to obtain a valid Telegram API key (api_id and api_hash pair) for your Telegram account that will be used by userbot. To do that:
1. Visit https://my.telegram.org/apps and log in with your Telegram account.
2. Fill out the form with your details and register a new Telegram application.
3. Done. The API key consists of two parts: api_id and api_hash. Keep it secret.

To get up a chat_id you need to get a link to the channel (it will have a look like `t.me/somechannel`), then rewrite it in format `@somechannel`.

The other possible solution can look like this:

1. Create a Telegram channel if you haven't already.
2. Add your Telegram bot as an administrator of the channel.
3. Go to the following URL in your web browser: https://api.telegram.org/bot<your-bot-token>/getUpdates. Replace <your-bot-token> with the token for your Telegram bot.
4. Send a message to the channel.
5. Look for the "chat" object in the JSON response. The "id" field of the "chat" object contains the chat ID.

Here's an example of what the JSON response might look like:

```
{
  "ok": true,
  "result": [
    {
      "update_id": 123456789,
      "message": {
        "message_id": 1,
        "from": {
          "id": 123456789,
          "is_bot": false,
          "first_name": "John",
          "last_name": "Doe",
          "username": "johndoe",
          "language_code": "en"
        },
        "chat": {
          "id": -100123456789,  // Channel ID is negative
          "title": "My Telegram Channel",
          "username": "mytelegramchannel",
          "type": "channel"
        },
        "date": 1645594965,
        "text": "Hello, world!"
      }
    }
  ]
}
```

In this example, the chat ID is -100123456789. Note that the chat ID for a channel is always negative, and you need to include the negative sign in the chat ID when pasting it to the `chat_id = 'someid'` row.

## Built With

* [Pyrogram](https://docs.pyrogram.org/) - A Telegram userbot framework written on Python
