# Telegram Recent Actions' Restoring

Deleted messages restoring from supergroup in Telegram (from Recent Actions menu).

You have **only 48 hours after deleting** and you should be admin (or owner) of group.

- Update `.env`:
  - Get your `API_ID` and `API_HASH` according to [this instruction](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id)
  - Group ID could be found by [@RawDataBot](https://t.me/RawDataBot) (just add to group)
  - Add `NEW_GROUP_ID` if you want to forward deleted media to a new group (thanks [@JunaidBabu](https://github.com/JunaidBabu))
- Run script — all media will be downloaded to `media` directory, all messages will be saved in `dump.json`
