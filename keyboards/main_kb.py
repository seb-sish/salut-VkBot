from vkbottle import Keyboard, KeyboardButtonColor, Text

kb_start = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Начать"), color=KeyboardButtonColor.POSITIVE)
    .get_json()
)

def kb_main():
    return (Keyboard(one_time=True, inline=False)
            .add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE)
            .add(Text("К началу"), color=KeyboardButtonColor.POSITIVE))

