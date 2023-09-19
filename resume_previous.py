import asyncio

from js import localStorage
from pyscript import Element

def continue_previous():
    global current_status

    if previous_filename := localStorage.getItem("filename"):
        Element("play_pause").write(f"Resume {previous_filename}")
        Element("play_pause").element.style.display = "block"
        current_status = "resume"
    else:
        Element("play_pause").element.style.display = "none"

continue_previous()