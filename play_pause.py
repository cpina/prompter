from js import localStorage
from pyscript import Element
import asyncio
import json

current_status = "play"

def toggle_play_pause():
    global current_status

    if current_status == "play":
        current_status = "pause"
        button_action = "play"
    elif current_status == "pause":
        current_status = "play"
        button_action = "pause"
    elif current_status == "resume":
        current_status = "play"
        button_action = "pause"
        # file_upload didn't call it, so we do it from here
        asyncio.ensure_future(start_play())

    Element("play_pause").write(button_action.capitalize())


async def start_play():
    initial = localStorage.getItem("next_word")
    print("INITIAL:", initial)
    if initial is None:
        initial = 0
    else:
        initial = int(initial)

    lines = json.loads(localStorage.getItem("lines"))
    for i, word in enumerate(lines[initial:]):
        word = word.rstrip()
        current_word = initial + i

        Element("progress").write(f"Word {current_word} of {len(lines)}")
        Element("word").write(word)
        localStorage.setItem("next_word", current_word)
        await asyncio.sleep(wait_seconds_for(word))

        while current_status == "pause":
            # TODO: change this :-)
            await asyncio.sleep(0.5)

    Element("progress").write(f"Finished! Done {len(lines)}")
    Element("play_pause").element.style.display = "none"
    Element("word").write("")

    localStorage.removeItem("filename")
    localStorage.removeItem("lines")
    localStorage.removeItem("next_word")


def wait_seconds_for(word):
    return len(word) * 0.22 + 1.5
