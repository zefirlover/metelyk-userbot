from pyrogram import Client, types
import os

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

chat_id = -1001725834609
reaction = "🤡"
app = Client("my_account", api_id, api_hash)

async def main():
    async with app:
        # get_chat_history(chat_id, 10) get last 10 messages
        async for messages in app.get_chat_history(chat_id, 15):
            print(messages.reactions)
            if messages.reactions == None or messages.reactions == [types.Reaction(count=int,emoji=reaction)] or messages.reactions != [types.Reaction(count=int,chosen_order=0,emoji=reaction)]:
                await app.send_reaction(chat_id, messages.id, reaction)

app.run(main())
