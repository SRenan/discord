# Discord bot

Discord bot using the [python API](https://discordpy.readthedocs.io/en/latest/api.html).

## Installation

The bot is meant to run permanently on a Raspberry Pi. From a clean install of Raspbian or
Retropi, the following should install all the prerequisites

```
# python and libraries
sudo apt update
sudo apt install python3-pip
sudo apt install libffi-dev libnacl-dev ffmpeg
# discord api
python3 -m pip install -U discord.py
python3 -m pip install -U discord.py[voice]
```

Finally, the token for the bot must be included separately in a `token.txt` file.


To start the bot

```
python3 bot4.py
```


## Features
- Play sounds
- Play sounds on user login
- Count and store online users (for external use)

## TODO
- Add GPIO based on online users
- Use multiple files
- Use cogs
