import os
import telebot

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

def start(update, context):
  update.message.reply_text("Hello! Welcome To CricInfoBot!")

def help(update, context):
  update.message.reply_text(""" 
  The following commands are available: 

  /start -> Welcome Message
  /help  -> This Message                            
                                                      """)        

def content(update, context):
  update.message.reply_text("we will inform uh about colleges")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher


disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("help",help))
disp.add_handler(telegram.ext.CommandHandler("content",content))

bot.polling()
