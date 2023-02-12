from typing import Callable
from multiprocessing import Event, Process
import time

class Sortable():
    song: Process
    condition: Callable[..., bool]
    priority: int

    def __init__(self, song: str, prio: int) -> None:
        self.song = song
        self.priority = prio


song_map: dict[str, Sortable] = {
    "Unknown": Sortable(lambda x: 'bobby_hill.mp3', 10),
    "Brandon": Sortable(lambda x: 'barcelona.mp3' if 'Deanna' in x else 'a.mp3', 1),
    "Deanna": Sortable(lambda x: 'crazy_frog.mp3', 2),
    "Robin": Sortable(lambda x: 'the_batman.mp3', 4),
    "Log": Sortable(lambda x: 'qs.mp3', 4),
    "Pao" : Sortable(lambda x: ('boom_boom_pao.mp3', 'careless_whisper.mp3', 'barbie_girl.mp3')[len(x) - 1 if len(x) < 3 else 2], 0),
}

def worker(e):
    for i in range(100):
        print(1)
        time.sleep(4)


def main():
    e = Event()
    e.set()

    fin = Process(target=worker, args=(e, ))
    fin.start()
#end main


if __name__ == '__main__':
    main()