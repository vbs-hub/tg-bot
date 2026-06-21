import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from state.state import Buy
from keyboard.inline import inline_dough, inline_topping, inline_confirmation
from handlers.msg_admin import send_admin_msg

r = Router()

DOUGH_PRISE = {
    'Тонкое' : 100,
    'Классическое' : 150,
    'Римское' : 150,
    'Цельнозерновое' : 200
}

TOPPINGS_PRISE = {
    'Сыр' : 60,
    'Перец' : 60,
    'Шампиньоны' : 60,
    'Баклажан': 60,
    'Ананас' : 60,
    'Томаты': 60,
    'Халапеньо' : 60

}

@r.message(Command('buy'))
async def buy_pizza(message : Message, state : FSMContext):
    await message.answer('Давай начнём делать тебе пицу\n\nКакуе тесть возьмёшь?', reply_markup=inline_dough())
    await state.set_state(Buy.dough)

@r.callback_query(Buy.dough, F.data.in_(['Тонкое', 'Классическое', 'Римское', 'Цельнозерновое']))
async def dough(call : CallbackQuery, state : FSMContext):
    await call.answer()
    data = call.data
    await state.update_data(save_dough=data)
    await call.message.answer(f'Тесто: {data}\n\nВыберите добавку:', reply_markup=inline_topping())
    await state.set_state(Buy.toppings)

@r.callback_query(Buy.toppings, F.data.in_(['Сыр', 'Перец', 'Шампиньоны', 'Баклажан', 'Ананас', 'Томаты', 'Халапеньо']))
async def toppings(call : CallbackQuery, state : FSMContext):
    await call.answer()
    data = call.data
    await state.update_data(save_toppings=data)
    await call.message.answer(f'Добавка: {data}\n\nПримечание к заказу (без примечанай пропишите "нет")')
    await state.set_state(Buy.note)

@r.message(Buy.note)
async def note_message(message : Message, state : FSMContext):
    note_msg = message.text
    if note_msg.lower() == 'нет':
        await message.answer(f'Примечание к готовке:\nНету\n\nНачять готовку:', reply_markup=inline_confirmation())
        note_msg = 'Нету'
        await state.update_data(save_note=note_msg)
    else:
        await message.answer(f'Примечание к готовке:\n{note_msg}\n\nНачять готовку:', reply_markup=inline_confirmation())
        await state.update_data(save_note=note_msg)
    await state.set_state(Buy.confirmation)

@r.callback_query(Buy.confirmation, F.data.in_(['Да', 'Нет']))
async def confirmation(call : CallbackQuery, state : FSMContext):
    await call.answer()
    calldata = call.data
    if calldata == 'Да':
        await call.message.answer('Мы начнём готовку')
        data = await state.get_data()
        save_dough = data.get('save_dough')
        save_toppings = data.get('save_toppings')
        save_note = data.get('save_note')

        prise_dough = DOUGH_PRISE.get(save_dough, 0)
        prise_toppings = TOPPINGS_PRISE.get(save_toppings, 0)

        result = prise_dough + prise_toppings

        width = 26 

        header = 'HOT CIRCLE'.center(width)
        title = 'ЧЕК'.center(width)
        footer = '! Спасибо за покупку !'.center(width)
        line = '-' * width


        dough_line = f'{save_dough:<18}{prise_dough:>8}'
        toppings_line = f'{save_toppings:<18}{prise_toppings:>8}'
        total_line = f'{"Итог:":<18}{result:>8}'
        note_line = f'Примечание: {save_note}'

        text = (
            f'<code>'
            f'{header}\n'
            f'{line}\n'
            f'{title}\n'
            f'{line}\n\n'
            f'{dough_line}\n'
            f'{toppings_line}\n\n'
            f'{note_line}\n\n'
            f'{line}\n'
            f'{total_line}\n'
            f'{footer}'
            f'</code>'
        )

        user_id = call.from_user.id
        await call.message.answer(text=text, parse_mode='HTML')
        await send_admin_msg(
            bot=call.bot,
            user_id=user_id, 
            dough=save_dough,
            prise=result,
            toppings=save_toppings,
            message=call.message,
            state=state,
            note=save_note
            )
        await state.clear()
    else:
        await call.message.answer(f'Вашь ответ: {calldata}. Начните занаво пропишите: <code>/buy</code>', parse_mode='HTML')
        await state.clear()

