from bot import bot

async def start_game(message):
    await bot.send_message(message.from_user.id,f'Привет{message.from_user.first_name}\n'
                                                f'На столе лежит 150 конфет.За один ход можно забрать не более чем 28 конфет.'
                                                f' Все конфеты оппонента достаются сделавшему последний ход.')

async  def player_take(message):
    await bot.send_message(message.from_user.id, f'Возмите конфет не больше 28: ')

async def table_info(message, name1, take, total_count, name2):
    await bot.send_message(message.from_user.id, f'{name1} Взял {take}котнфет \n '
                                                 f'на столе осталось {total_count} конфет'
                                                 f' Ход {name2}')


async def win(message, name, take, total_count):
    await bot.send_message(message.from_user.id, f'{name} Взял {take}котнфет \n'
                                                 f'на столе осталось {total_count} конфет'
                                                 f'{name} Победил!')

async def wrong_take(message):
    await bot.sens_message(message.from_user.id,f'Вы взяли слишком много конфет, попробуйдетке снова!')