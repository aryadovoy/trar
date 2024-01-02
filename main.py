import json
import logging
import os

from telethon import TelegramClient

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
OLD_GROUP_ID = os.getenv("OLD_GROUP_ID")
NEW_GROUP_ID = os.getenv("NEW_GROUP_ID")

messages = []

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

client = TelegramClient("session_name", API_ID, API_HASH)
client.start()


async def main() -> None:
    logging.info("Restoring was started!")
    async for event in client.iter_admin_log(int(OLD_GROUP_ID)):
        if event.deleted_message:
            if event.old.media:
                # Forwarding to a group and reply to it with the data and file id
                if NEW_GROUP_ID:
                    logging.info(
                        f"Forwarding media {event.old.id} to new group"
                    )
                    new_msg = await client.send_message(
                        NEW_GROUP_ID, event.old
                    )
                    await client.send_message(
                        NEW_GROUP_ID,
                        reply_to=new_msg,
                        message=f"media/{str(event.old.date)[:-6]}_{event.old.id}",
                    )

                # NOTE comment out the following to skip local download
                logging.info(f"Downloading media {event.old.id}")
                await client.download_media(
                    event.old.media,
                    f"media/{str(event.old.date)[:-6]}_{event.old.id}",
                )

            if event.old.message:
                logging.info(f"Saving message {event.old.id}")
                messages.append(
                    {
                        "id": event.old.id,
                        "date": str(event.old.date),
                        "message": str(event.old.message),
                    }
                )
    with open("dump.json", "a", encoding="utf-8") as json_file:
        json.dump(messages, json_file, ensure_ascii=False)
    logging.info("All messages were downloaded!")


with client:
    client.loop.run_until_complete(main())
