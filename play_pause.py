current_status = "play"
Element("play_pause").element.style.display = "none"

def toggle_play_pause():
    global current_status

    if current_status == "play":
        current_status = "pause"
    else:
        current_status = "play"

    Element("play_pause").write(current_status.capitalize())
