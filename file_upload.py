from js import document, window, Uint8Array

from pyodide.ffi.wrappers import add_event_listener
import asyncio

def wait_seconds_for(word):
    return len(word) * 0.22 + 1.5

async def upload_file_and_show(e):
    file_list = e.target.files

    first_item = file_list.item(0)

    my_bytes: bytes = await get_bytes_from_file(first_item)

    lines = my_bytes.decode("utf-8").rstrip().split("\n")

    Element("play_pause").element.style.display = "block"

    for i, word in enumerate(lines):
        word = word.rstrip()
        Element("progress").write(f"Word {i+1} of {len(lines)}")
        Element("word").write(word)
        await asyncio.sleep(wait_seconds_for(word))

        while current_status == "pause":
            # TODO: change this :-)
            await asyncio.sleep(0.5)

    Element("progress").write(f"Finished! Done {len(lines)}")
    Element("play_pause").element.style.display = "none"

async def get_bytes_from_file(file):
    array_buf = await file.arrayBuffer()

    return array_buf.to_bytes()


add_event_listener(document.getElementById("file-upload"), "change", upload_file_and_show)
