# Discord Bridge

<p align="center">
<img src="/logo.png" alt="the logo" width=250>
</p>
The python bot works as a bridge to connect discord to SMS, for those who do not have enough space on their phone for Discord, but would still like to be notified on their phone.

## Installation

dependencies:<br>
`python3 -m pip install -U git+https://github.com/Pycord-Development/pycord`<br>
`pip3 install twilio`<br>
`pip3 install sqlalchemy`<br>

## Running the bot
```
python3 run_bot.py
```

## Built with
- Twilio API
- Pycord
- SQLAlchemy

## Commands list
```
/hello - returns a "hello"
/register - DMs the user, tells them to enter their number
/notify - Sends a SMS message to a specified user
/tellme - Sends messages in specified channel to user
```

## Extra functions
```
Sends message from SMS to discord channel via webhooks and Zapier (large delay)
(Bot does not automatically create webhooks)
/notify can take an optional delay in seconds
```
