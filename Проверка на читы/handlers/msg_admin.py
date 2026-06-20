from aiogram import Router, F,  Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboard.inline import inline_answer
from state.state import Admin

r = Router()

ADMIN_ID = 5865529339

async def send_admin_msg(bot : Bot, user_id : int, prise : int, note : str, dough : str, toppings : str, message : Message, state : FSMContext):

    width = 26

    heandle = 'HOT CIRCLE ADMIN'.center(width)
    title = 'Новый ЗАКАЗ'.center(width)
    line = '-' * width

    total_line = f'{"Итог:":<18}{prise:>8}'

    user_id_msg = f'{'ID:':<18}<b>{user_id:>8}</b>'
    note_line = f'Примечание: {note}'

    text = (
        f'<code>'
        f'{heandle}\n'
        f'{line}\n'
        f'{title}\n'
        f'{line}\n\n'
        f'{dough.center(width)}\n'
        f'{toppings.center(width)}\n\n'
        f'{note_line}\n\n'
        f'{line}\n'
        f'{total_line}\n\n'
        f'{user_id_msg}'
        f'</code>'
    )
    await bot.send_message(chat_id=ADMIN_ID, text=text, parse_mode='HTML')
    await bot.send_message(chat_id=ADMIN_ID, text=f'Скопировать ID: <code>{user_id}</code>\n\nВведите ID:', parse_mode='HTML')
@r.message(F.chat.id == ADMIN_ID, F.text.isdigit())
async def user_id_msg(message : Message, bot : Bot, state : FSMContext):
    user_id = message.text

    await state.update_data(save_id=user_id)
    await bot.send_message(chat_id=user_id, text='Подтвердите:', reply_markup=inline_answer())
    await state.set_state(Admin.confirmation)

@r.callback_query(Admin.confirmation, F.data.in_(['Да', 'Нет']))
async def confirmation_msg(call : CallbackQuery, state : FSMContext, bot : Bot):
    confirmation = call.data
    user_data = await state.get_data()
    save_id = user_data.get('save_id')
    if confirmation == 'Нет':
        await bot.send_message(chat_id=int(save_id), text='Вашь заказ отменён')
        await bot.send_message(chat_id=ADMIN_ID, text=f'Вы отменили заказ {save_id}')
    else:
        await bot.send_message(chat_id=int(save_id), text='! Вашь заказ готов !')
        await bot.send_message(chat_id=ADMIN_ID, text='Вы подтвердили заказ')


