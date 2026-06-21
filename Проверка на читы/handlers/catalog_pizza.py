from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboard.inline import inline_catalog
from state.state import Categori
from aiogram.fsm.context import FSMContext
from keyboard.inline import inline_answer
from handlers.msg_admin import send_admin_msg

r = Router()

PIZZA_PRISE = {
    'Пеперони' : 160,
    'Маргарита' : 160,
    'Четыре Сыра' : 160,
    'Сытные и Мясные' : 160,
    'Цыпленок Барбекю' : 160,
    'Экзотика и Вегетарианская' : 160,
    'Овощная (Вегги)' : 160
}

@r.message(Command('pizza'))
async def catalog_pizza(message : Message, state : FSMContext):
    await message.answer('Выберите Пиццу:', reply_markup=inline_catalog())
    await state.set_state(Categori.selection)
    
@r.callback_query(Categori.selection, F.data.in_(['Пеперони', 'Маргарита', 'Четыре Сыра', 'Сытные и Мясные', 'Цыпленок Барбекю', 'Экзотика и Вегетарианская', 'Овощная (Вегги)']))
async def selection_inline(call : CallbackQuery, state : FSMContext):
    await call.answer()
    selection = call.data
    await state.update_data(save_selection=selection)
    await call.message.answer(f'Вашь выбор: {selection}\n\nНачять готовку?', reply_markup=inline_answer())
    await state.set_state(Categori.confirmation)

@r.callback_query(Categori.confirmation, F.data.in_(['Да', 'Нет']))
async def confirmation_msg(call : CallbackQuery, state : FSMContext):
    await call.answer()
    confirmation = call.data
    if confirmation == 'Да':
        await call.message.answer('Хорошо\n\nЕстли примечание к заказу (если нету то пиши "нет")')
        await state.set_state(Categori.note)

    else:
        await call.message.answer('Хорошо начните занаво\nКоманда: <code>/pizza</code>')
        await state.clear()

@r.message(Categori.note)
async def note_msg(message : Message, state : FSMContext):
    note = message.text
    await state.update_data(save_note=note)
    await message.answer(f'Ваше примечание:\n{note}')

    data = await state.get_data()
    selection = data.get('save_selection')

    width = 26

    heandle = f'HOT CIRCLE'.center(width)
    title = f'ЧЕК'.center(width)
    line = '-' * width

    note_message = f'Примечание: {note}'
    
    footer = '! Спасибо за покупку !'.center(width)

    prise_pizza = PIZZA_PRISE.get(selection, 0)


    text = (
        f'<code>'
        f'{heandle}\n'
        f'{line}\n'
        f'{title}\n'
        f'{line}\n\n'
        f'{selection:<18}{prise_pizza:>8}\n\n'
        f'{note_message}\n\n'
        f'{line}\n'
        f'{footer}'
        f'</code>'
    )
    result = prise_pizza
    user_id = message.from_user.id
    await message.answer(text=text, parse_mode='HTML')
    await send_admin_msg(
            bot=message.bot,
            user_id=user_id, 
            dough=selection,
            prise=result,
            toppings='Добавок: Нету',
            message=message,
            state=state,
            note=note
            )
    await state.clear()

