from js import document

from pyodide.ffi.wrappers import add_event_listener
from js import localStorage
from pathlib import PureWindowsPath
import play_pause
from pyscript import Element
import json

async def upload_file_and_show(e):
    global event
    # Firefox on Linux return a "name" such as "c:\fake\filename.txt". We
    # only want the "filename.txt" so "PureWindowsPath" is used (because
    # Pyode use, by default if using Path, POSIX paths).
    filename = PureWindowsPath(Element("file-upload").element.value).name

    file_list = e.target.files
    first_item = file_list.item(0)

    my_bytes: bytes = await get_bytes_from_file(first_item)

    try:
        lines = my_bytes.decode("utf-8").rstrip().split("\n")
    except UnicodeError as exc:
        Element("status").write(exc)
        return

    localStorage.setItem("filename", filename)
    localStorage.setItem("lines", json.dumps(lines))
    localStorage.setItem("next_word", 0)

    await play_pause.start_play(event)

async def get_bytes_from_file(file):
    array_buf = await file.arrayBuffer()

    return array_buf.to_bytes()


add_event_listener(document.getElementById("file-upload"), "change", upload_file_and_show)
