import telegram.ext

Token = "7197209767:AAHPU0AaV6hfBdH2wWx5kIXazwTSSae7j0Q"

updater = telegram.ext.updater("7197209767:AAHPU0AaV6hfBdH2wWx5kIXazwTSSae7j0Q", use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text("Hello Welcome to CricInfoBot!")\
    
def help(update, context):
    update.message.reply_text(
        """
    
    /start -> Welcome to the channel
    /help -> This Particular Message
    /content -> About Various Colleges Across India                                                    
                              """
    )    
    
def content(update, context):
     update.message.reply_text(" We Have Various information about colleges")

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('content', content))

updater.start_polling()
updater.idle()