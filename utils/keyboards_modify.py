from vkbottle import Keyboard, KeyboardButtonColor, Text
from vkbottle.tools.dev.keyboard.button import KeyboardButton
from vkbottle.tools.dev.keyboard.action import Text

async def insert_buttons(keyboard : Keyboard, buttons=[str]):
    keyboardButtons = await buttons_builder([KeyboardButton.from_typed(Text(text), 
                                                KeyboardButtonColor.PRIMARY) for text in buttons])
    if keyboardButtons[0]: keyboard.buttons.extend(keyboardButtons.__reversed__())
    keyboard.buttons.reverse()
    return keyboard

async def buttons_builder(buttons : list[KeyboardButton], buttons_in_row=2):
    builder = [[]]
    for i, button in enumerate(buttons, start=1):
        if i % buttons_in_row == 0:
            builder[-1].append(button)
            if i != len(buttons): builder.append([])
        else:
            builder[-1].append(button)
    return builder
