from pyrogram import Client, Filters

app = Client("silencert")


@app.on_message(Filters.group)
def delete_join_or_leave_message(client, message):
    if message.new_chat_members is not None or message.left_chat_member is not None:
        client.delete_messages(message.chat.id, [message.message_id])


app.start()
app.idle()
