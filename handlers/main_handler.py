from vkbottle.bot import Message, BotLabeler
from vkbottle import CtxStorage

from keyboards import kb_main, kb_start
from utils import insert_buttons, json_search
from config import Config

ctx_storage = CtxStorage()
main_labeler = BotLabeler()
main_labeler.vbml_ignore_case = True

start_text = "начать"
@main_labeler.message(text=[start_text, "к началу"])
async def start_handler(message: Message):
    ctx_storage.set("last", start_text)
    new_kb = await insert_buttons(kb_main(), Config.INFO.keys())
    await message.answer("Выберите раздел", keyboard=new_kb.get_json())

@main_labeler.message(text=["назад"])
async def back_handler(message: Message):
    if CtxStorage().get("last") in [start_text] + list(Config.INFO.keys()): return await start_handler(message)
    info = json_search(Config.INFO,  CtxStorage().get("last"))
    if info:
        to = json_search(Config.INFO, info[0][-2] if len(info[0]) >= 2 else info[0][-1])[1]
        ctx_storage.set("last", info[0][-2] if len(info[0]) >= 2 else start_text)
        new_kb = await insert_buttons(kb_main(), to["buttons"].keys())
        await message.answer(to["text"], keyboard=new_kb.get_json(), attachment=to.get("image", ""))
    else: await error_handler(message)

@main_labeler.message(text=Config.INFO.keys())
async def main_handler(message: Message):
    ctx_storage.set("last", message.text)
    new_kb = await insert_buttons(kb_main(), Config.INFO[message.text]["buttons"].keys())
    await message.answer(Config.INFO[message.text]["text"], keyboard=new_kb.get_json())
    
@main_labeler.message(text=Config.ADDITIONAL_BUTTONS)
async def additional_handler(message: Message):
    info = json_search(Config.INFO, message.text)
    if info:
        data = info[1]
        ctx_storage.set("last", message.text)
        new_kb = await insert_buttons(kb_main(), data["buttons"].keys())
        await message.answer(data["text"], keyboard=new_kb.get_json(), attachment=data.get("image", ""))
    else: await error_handler(message)

@main_labeler.message()
async def error_handler(message: Message):
    await message.answer("Такой информации еще нет, но скоро она появится", keyboard=kb_main().get_json())