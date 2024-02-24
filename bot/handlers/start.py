from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command

from repositories import Repository
from utils.message_template import MessageTemplate

router = Router()


class States(StatesGroup):
    ask = State()


@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await state.clear()
    text, reply_markup = MessageTemplate.from_json('start/start').render()
    await message.answer(text, reply_markup=reply_markup)


@router.message(Command('ask'))
async def ask(message: Message, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('start/ask').render()
    await message.answer(text, reply_markup=reply_markup)   
    await state.set_state(States.ask)


@router.message(States.ask)
async def ask(message: Message, state: FSMContext, repository: Repository):
    answer = await repository.gpt.make_request(message.text)

    if answer is None:
        await message.answer("К сожалению у меня нет ответа на данный вопрос. Попробуй задать другой вопрос.")   
    else:
        await message.answer(answer)