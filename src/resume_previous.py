import asyncio
import json

from js import localStorage
from pyscript import Element

def continue_previous():
    global current_status

    if previous_filename := localStorage.getItem("filename"):
        number_of_words = len(json.loads(localStorage.getItem("lines")))
        next_word = int(localStorage.getItem("next_word"))
        Element("play_pause").write(f"Resume {previous_filename} ({next_word + 1}/{number_of_words})")
        Element("play_pause").element.style.display = "block"
        current_status = "resume"
        Element("introduction").write("Select a file or click on \"Resume\" button")
    else:
        Element("play_pause").element.style.display = "none"

continue_previous()