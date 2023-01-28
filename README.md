# Restoring deleted messages from supergroup in Telegram (Recent Actions)

You have only 48 hours after deleting and you should be admin (or owner) of group.

- Update `.env`:
  - Get your `API_ID` and `API_HASH` according to [this instruction](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id)
  - Channel ID could be found by [@RawDataBot](https://t.me/RawDataBot) (just add to group)
- Run script — all media will be downloaded to `media` directory, all messages will be saved in `dump.json`
