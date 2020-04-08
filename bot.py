from pyrogram import Client, Filters

app = Client("silencert")


@app.on_message(Filters.group)
def delete_unwanted_message(client, message):
    unwanted_messages = [
        message.new_chat_members,
        message.left_chat_member,
        message.new_chat_title,
    ]
    for unwanted in unwanted_messages:
        if unwanted is not None:
            client.delete_messages(message.chat.id, [message.message_id])

    if message.text is not None and message.text.find("https://t.me/joinchat/") > -1:
        client.delete_messages(message.chat.id, [message.message_id])


app.start()
app.idle()
