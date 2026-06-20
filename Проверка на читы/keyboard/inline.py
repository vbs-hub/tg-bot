from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def inline_dough():
    btn_subtle = InlineKeyboardButton(text='Тонкое (Итальянское)', callback_data='Тонкое')
    btn_classic = InlineKeyboardButton(text='Классическоее (Пышное)', callback_data='Классическое')
    btn_roman = InlineKeyboardButton(text='Римское (Хрустящее)', callback_data='Римское')
    btn_fit = InlineKeyboardButton(text='Цельнозерновое (Фитнес)', callback_data='Цельнозерновое')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [btn_subtle],
        [btn_classic],
        [btn_roman],
        [btn_fit]
    ])
    return keyboard

def inline_topping():
    btn_cheese = InlineKeyboardButton(text='Сыр', callback_data='Сыр')
    btn_pepper = InlineKeyboardButton(text='Перец', callback_data='Перец')
    btn_champignons = InlineKeyboardButton(text='Шампиньоны', callback_data='Шампиньоны')
    btn_eggplant = InlineKeyboardButton(text='Баклажан', callback_data='Баклажан')
    btn_pineapple = InlineKeyboardButton(text='Ананас', callback_data='Ананас')
    btn_tomatoes = InlineKeyboardButton(text='Томаты', callback_data='Томаты')
    btn_jalapeno = InlineKeyboardButton(text='Халапеньо', callback_data='Халапеньо')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [btn_pepper],
        [btn_eggplant],
        [btn_champignons],
        [btn_cheese],
        [btn_pineapple],
        [btn_tomatoes],
        [btn_jalapeno]

    ])
    return keyboard

def inline_confirmation():
    btn_yes = InlineKeyboardButton(text='Да', callback_data='Да')
    btn_not = InlineKeyboardButton(text='Нет', callback_data='Нет')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [btn_yes],
        [btn_not]
    ])
    return keyboard

def inline_answer():
    btn_yes = InlineKeyboardButton(text='Да', callback_data='Да')
    btn_not = InlineKeyboardButton(text='Нет', callback_data='Нет')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [btn_yes],
        [btn_not]
    ])
    return keyboard

def inline_catalog():
    btn_pepperoni = InlineKeyboardButton(text='Пеперони', callback_data='Пеперони')
    btn_margarita = InlineKeyboardButton(text='Маргарита', callback_data='Маргарита')
    btn_four_cheese = InlineKeyboardButton(text='Четыре Сыра', callback_data='Четыре Сыра')
    btn_meat = InlineKeyboardButton(text='Сытные и Мясные', callback_data='Сытные и Мясные')
    btn_chicken = InlineKeyboardButton(text='Цыпленок Барбекю', callback_data='Цыпленок Барбекю')
    btn_exotica = InlineKeyboardButton(text='Экзотика и Вегетарианская', callback_data='Экзотика и Вегетарианская')
    btn_vegetables = InlineKeyboardButton(text='Овощная (Вегги)', callback_data='Овощная (Вегги)')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [btn_margarita, btn_chicken],
        [btn_four_cheese, btn_meat],
        [btn_exotica, btn_pepperoni],
        [btn_vegetables]
    ])
    return keyboard