from aiogram.fsm.state import State, StatesGroup

class Buy(StatesGroup):
    dough = State()
    toppings = State()
    note = State()
    confirmation = State()
 

class Admin(StatesGroup):
    confirmation = State()
    user_id = State()

class Msg(StatesGroup):
    msg = State()
    confirmation = State()

class Categori(StatesGroup):
    selection = State()