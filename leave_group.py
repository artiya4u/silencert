from pyrogram import Client

min_member_count = 200
# Bot will leave all of non admin right group.
app = Client("silencert_remove_self")
app.start()
dialogs = app.iter_dialogs()
me = app.get_me()
for d in dialogs:
    try:
        member = app.get_chat_member(d.chat.id, me.id)
        if d.chat.is_scam:
            print("LEAVE - SCAM", d.chat.title)
            app.leave_chat(d.chat.id)
        elif d.chat.members_count < min_member_count:
            print("LEAVE - NOT ENOUGH USERS", d.chat.title)
            app.leave_chat(d.chat.id)
        elif member.status != "administrator":
            print("LEAVE - NOT ADMIN", d.chat.title)
            app.leave_chat(d.chat.id)
        else:
            print('STAY', d.chat.title)
    except Exception as e:
        print('ERROR', d.chat.title)
app.stop()
