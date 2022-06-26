from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
  
updater = Updater("5346512296:AAG2sqZCUea0WcfAiqaUgCCftZCLhrFYZ4g",
                  use_context=True)

def get_random_advice():
    from random import choice
    advice_list = ["1. Choose a shower over a bath\nPerhaps those who like to soak in the bath for a long time will be upset. But on average, taking a shower uses less water than taking a regular bath.",
" Cut down on shower time\nThose who stand in the shower for a long time hoping to wake up in the morning do not even think about saving water. Try changing your habit. Drink, for example, before a shower a cup of coffee to wake up your body. And remember: the less time you spent in conditions of abundant moisture and steam, the easier your skin will feel.",
" Run the dishwasher only when fully loaded\nThis does not mean that you need to fill the dishwasher with a chock-full - so the plates and cups will not be rinsed well. But you can not turn on the car half empty. According to the operating instructions, in this case, the equipment fails faster, and a lot of excess water is consumed.",
" Run only a full washing machine\nAs in the above paragraph, you should not start washing in an incompletely loaded washing machine. If you can’t fill it with pre-prepared things, then throw in it home textiles that often need washing: curtains, kitchen towels, napkins, tablecloths and more.",
" Water houseplants with reclaimed tub wastewater\nThis will significantly reduce water consumption, especially if there is plenty of green decor in your home. In addition, some plants need daily watering.",
" Install Waste Recycling Systems\nEco gadgets are becoming more and more popular in the world. With them, saving water in the house is much easier. To do this, you need to install special structures for collecting and filtering wastewater - you can order them or make them yourself.",
" Repair the leak\nFrom a faulty faucet, up to 7,000 liters of water can drip in a year! A leaking toilet cistern can lose up to 16,000 liters per year. So, poorly functioning plumbing not only hits the nerves and pockets, but also has a bad effect on the global ecology.",
" Turn off the faucet while brushing your teeth or washing dishes\nHave you noticed how much water flows out of an open faucet while you brush your teeth or rub your plate to a shine? Definitely a lot. Train yourself to turn off the faucet if you are not currently using water. In this regard, it is good to have single-lever mixers that are easy to turn off and on with one movement.",
" Install Low Flow Shower Heads\nModern bath fixtures have special functions and settings that control water consumption, which helps to save water consumption well. But the popularity of such watering cans has influenced the growth of their fakes, so before buying, carefully read the product and read reviews about it. Another option, more budgetary, is to purchase a smaller diameter shower head.",
" Throw a full plastic water bottle in the toilet bowl\nThis simple but proven method will reduce the amount of water needed to fill the tank after each flush. It seems to be a trifle, but the real savings."] 
    return choice(advice_list)
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot. Please write\
        /help to see the commands available.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /donate - To get donate URL
    /advice - To get advice
    /site - my site URL""")
  
  
def advice_url(update: Update, context: CallbackContext):
    update.message.reply_text(get_random_advice())
  
  
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/")
  
  
def site_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Site URL => \
        https://defendthewater.tk/")
  
  
def donate_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Donate URL => None")
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('advice', advice_url))
updater.dispatcher.add_handler(CommandHandler('donate', donate_url))
updater.dispatcher.add_handler(CommandHandler('site', site_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()