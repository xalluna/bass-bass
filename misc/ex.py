from typing import Callable

class sortable():
    song: Callable[..., str]
    priority: int
    def __init__(self, song: str, prio: int) -> None:
        self.song = song
        self.priority = prio

song_map: dict[str, sortable] = {
    "Unknown": sortable(lambda x: 'bobby_hill.mp3', 10),
    "Brandon": sortable(lambda x: 'barcelona.mp3' if 'Deanna' in x else 'a.mp3', 1),
    "Deanna": sortable(lambda x: 'crazy_frog.mp3', 2),
    "Robin": sortable(lambda x: 'the_batman.mp3', 4),
    "Log": sortable(lambda x: 'qs.mp3', 4),
    "Pao" : sortable(lambda x: ('boom_boom_pao.mp3', 'careless_whisper.mp3', 'barbie_girl.mp3')[len(x) - 1 if len(x) < 3 else 2], 0),
}

def main():
    foo = ['Brandon', 'Pao', 'Unknown', 'Deanna']

    bar = [song_map[name] for name in foo]
    bar = sorted(bar, key=lambda x: x.priority, reverse=False)

    fizz = bar[0]
    buzz = fizz.song(foo) if callable(fizz.song) else fizz.song
    print(buzz)
#end mainu

if __name__ == '__main__':
    main()