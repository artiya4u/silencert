# SilencerT - A bot to automatic delete trivial messages on Telegram group.

##Features
- Remove trivial unwanted auto messages on Telegram group e.g. joining, leaving or title change.
- Usage: add an account name [@SilencerGramBOT](https://t.me/SilencerGramBOT) to your group and make it be a group admin or run bot yourself as the "getting started" steps below.

### Messages to be remove
- `USER` left the group
- `USER` joined the group
- `USER` joined the group by invite link
- Message that contain another group invite link e.g. "LET'S JOIN ANOTHER GROUP -> https://t.me/joinchat/ANOTHER_GROUP"

## Requirements

- Python 3.4 or higher.
- pyrogram - Telegram MTProto API Client Library for Python

## Getting Started

```bash
pip install -r requirements.txt
python3 bot.py
```
Log in your group admin account with the prompt (only do this once).
