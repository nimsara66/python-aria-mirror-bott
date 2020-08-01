from pyrogram import Client

API_KEY = int(input("1581404"))
API_HASH = input("f38e4e8eed29ebb53053e65d4d68fb96")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
