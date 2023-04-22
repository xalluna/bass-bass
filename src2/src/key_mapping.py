import pygame.mixer as mixer

def quit() -> tuple[bool, bool]:
    return (False, False)

def stop_song() -> tuple[bool, bool]:
    mixer.music.stop()
    return (True, True)

def pause_song() -> tuple[bool, bool]:
    mixer.music.pause()
    return (True, False)

def resume_song() -> tuple[bool, bool]:
    mixer.music.unpause()
    return (True, True)

key_map = {
    's': stop_song,
    'q': quit,
    'p': pause_song,
    ' ': resume_song,
}