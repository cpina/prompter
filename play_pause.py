from js import localStorage
from pyscript import Element
import asyncio
import json

current_status = "playing"

event = asyncio.Event()

def toggle_play_pause():
    global current_status

    if current_status == "playing":
        current_status = "paused"
        event.clear()
    elif current_status == "paused":
        current_status = "playing"
        asyncio.ensure_future(start_play(event))
    elif current_status == "resume":
        current_status = "playing"
        # file_upload didn't call it, so we do it from here
        asyncio.ensure_future(start_play(event))

    if current_status == "paused":
        if int(localStorage.getItem("next_word")) == 0:
            button_action = "start"
        else:
            button_action = "resume"
    elif current_status == "playing":
        button_action = "pause"

    Element("play_pause").write(button_action.capitalize())


async def start_play(event):
    event.set()
    Element("play_pause").element.style.display = "block"

    initial = localStorage.getItem("next_word")
    if initial is None:
        initial = 0
    else:
        initial = int(initial)

    lines = json.loads(localStorage.getItem("lines"))
    for i, word in enumerate(lines[initial:]):
        word = word.rstrip()
        current_index_in_file = initial + i

        Element("progress").write(f"Word {current_index_in_file + 1} of {len(lines)}")
        Element("word").write(word)
        localStorage.setItem("next_word", current_index_in_file + 1)
        await asyncio.sleep(wait_seconds_for(word))

        if not event.is_set():
            break

    if event.is_set():
        # It finished because all the lines have been prompted, not
        # because the user clicked on Pause
        Element("progress").write(f"Finished! Done {len(lines)} words")
        Element("play_pause").element.style.display = "none"
        Element("word").write("")

        localStorage.removeItem("filename")
        localStorage.removeItem("lines")
        localStorage.removeItem("next_word")

        Element("introduction").write("Select a file to start the prompter...")


def wait_seconds_for(word):
    return len(word) * 0.22 + 1.5
