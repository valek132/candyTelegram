from aiogram import Dispatcher
import commands

def rigistred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_game, commands=['START'])
    dp.register_message_handler(commands.player_turn)