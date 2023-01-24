# Misa Alert Telegram Bot
Simple bot to display alerts about the level of the Misa river in Senigallia,Italy using data from the protezione civile hydrometers.

The makefile for creating the virtual environment is not made by me, but the creator wants it open source :)

## How to run the bot
1. Create a new bot with @BotFather and get the HTTP API Token
2. Get the api endpoint of the sensors (Ask me on telegram @AleShark)
3. Get the chat or user id you want the bot to send messages to
4. Put all these three information into a file called ReservedSettings.py in the src/ folder.
5. Clone the project
6. Create the virtual environment with ```make virtualenv```
7. Activate the virtual environment with ```source env/bin/activate```
8. Install the requirements with ```make requirements```

Now you're ready to go
