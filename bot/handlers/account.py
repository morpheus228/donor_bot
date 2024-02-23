from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from utils.message_template import MessageTemplate

router = Router()


class States(StatesGroup):
    amount = State()


@router.message()
async def start(message: Message, state: FSMContext):
    await message.answer("...")
   
