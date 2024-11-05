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

Some functions require a homies.json file to function

```{json}
[{
  "name": "username",
  "intro: "path/to/mp3"
}]
```

## Running the bot

To start the bot
```
python3 bot6.py
```

Or via cron, run the bot for 23hours every day
```
0 11 * * * timeout 82800 /usr/local/bin/python3 /home/pi/mygit/discord/bot6/bot6.py
```


## Features
- Play sounds
- Play sounds on user login
- Capture images from camera
    - Face/eyes/body etection with opencv
- Count and store online users (for external use)

