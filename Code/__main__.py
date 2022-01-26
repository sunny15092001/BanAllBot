import logging
from . import bot
from pyrogram import Client, idle
from pyrogram import filters
from Code.helpers.Decorators import authorized_users_only
@bot.on_message(filters.command("banall") & filters.group)
@authorized_users_only
def NewChat(bot,message):
    logging.info("new chat {}".format(message.chat.id))
    logging.info("getting memebers from {}".format(message.chat.id))
    a= bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            bot.kick_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            bot.send_message("kicked {} from {}".format(i.user.id,message.chat.id))
            logging.info("kicked {} from {}".format(i.user.id,message.chat.id))
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id,message.chat.id))
            
    logging.info("process completed")

bot.run()
idle() 
