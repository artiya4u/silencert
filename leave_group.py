from pyrogram import Client

# Bot will leave all of non admin right group.
app = Client("silencert")
app.start()
dialogs = app.iter_dialogs()
me = app.get_me()
for d in dialogs:
    try:
        member = app.get_chat_member(d.chat.id, me.id)
        if member.status != "administrator":
            print("LEAVE", d.chat.title)
            app.leave_chat(d.chat.id)
        else:
            print('STAY', d.chat.title)
    except Exception as e:
        print('ERROR', d.chat.title)
app.stop()
