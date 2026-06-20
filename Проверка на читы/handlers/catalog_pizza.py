from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboard.inline import inline_catalog
from state.state import Categori
from aiogram.fsm.context import FSMContext

r = Router()

@r.message(Command('pizza'))
async def catalog_pizza(message : Message):
    await message.answer('Выберите Пиццу:', reply_markup=inline_catalog())
    
@r.callback_query(Categori.selection, F.data.in_(['Пеперони', 'Маргарита', 'Четыре Сыра', 'Сытные и Мясные', 'Цыпленок Барбекю', 'Экзотика и Вегетарианская', 'Овощная (Вегги)']))
async def selection_inline(call : CallbackQuery, state : FSMContext):
    selection = call.data
    await call.message.answer(f'Вашь выбор: {selection}\n\nПока эта команда в бета')