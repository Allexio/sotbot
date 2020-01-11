# SotBot
A Sea of Thieves discord bot that lets users explore SoT at their own pace and store charted islands in a database, that they can then query at a time of their choosing.
Such information includes the islands, their locations, their type, which animals live on them, which NPCs live on them.
The database starts off empty and grows as players make their discoveries and chart out the map.
## installation:
### Prerequisites:
* latest python3 (https://www.python.org/downloads/)
* latest discord.py (```pip install discord.py```)
### How to set up:
* create an application on discord https://discordapp.com/developers/applications/ (takes two clicks)
* make a bot for the application you create (on the left click on "bot" and then click on "add bot")
* save that bot's token as an environment variable on your system called "discord_sot_token" (you might need to restart after this!!)
* invite the bot to your server
* download contents of this git
* run ```python bot.py``` in your favourite command line
* (optional) if you want to change the prefix, edit the PREFIX variable in bot.py 
    ie. change it from ```PREFIX = "sot"``` to ```PREFIX = "[whatever prefix you want here]"```
* You are now free to use commands in your discord to interact with the bot!
## General Use:
Use the ```help``` command for a list of commands that you can execute and what they do.
