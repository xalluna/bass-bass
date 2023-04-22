from face_recognition import compare_faces, face_encodings, face_locations
from pickle import loads
from typing import Any
from song_mappings import song_map


class ImageProcessor:
    """Class for processing images and identifying people. Remebers people from previously processed images."""

    name_history: list[list[str]]
    """Running history of people identified from each image process operation."""
    current_names: list[str]
    """The most recent list of names processed."""
    previous_names : list[str]
    """The second most recent list of names processed."""
    people_seen: set[str]
    """All people previously seen over this object instance's lifespan."""
    people_seen_before: set[str]
    """All people previously seen over this object instance's lifespan proir to the most recent image."""
    data: Any
    """Encoding data for faces from the data set. This data must be precompiled."""

    def __init__(self) -> None:
        self.people_seen = set()
        self.people_seen_before = set()

        self.name_history = list()
        self.current_names = list()
        self.previous_names = list()

        encodings_from_file = "data-model/encodings.pickle"
        self.data = loads(open(encodings_from_file, "rb").read())
    #end init

    def process_image(self, frame) -> None:
        """Processes a frame to identify people and adds the people to the internal name history."""

        boxes = face_locations(frame)
        encodings = face_encodings(frame, boxes)

        names_to_add = self.process_encodings(encodings)
        self.update_names(names_to_add)
    #end image_processing

    def process_encodings(self, encodings) -> list[str]:
        """Processes encodings.
        
        Returns a `list[str]` of names identified."""

        names_to_return = []

        for encoding in encodings:
            matches = compare_faces(self.data["encodings"], encoding)

            name = "Unknown"

            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                for i in matchedIdxs:
                    name = self.data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                name = max(counts, key=counts.get)

            names_to_return.append(name)

        return names_to_return
    #end process_encodings

    def update_names(self, names_to_add: list[str]):
        """Adds names to history and updates people seen."""

        self.people_seen_before = self.people_seen.copy()
        self.people_seen.update(names_to_add)

        self.previous_names = self.current_names
        self.current_names = names_to_add
        self.name_history.insert(0, names_to_add)
    #end update_names

    def get_history(self) -> list[list[str]]:
        """Gets the entire name history."""
        return self.name_history.copy()
    #end get_history

    def choose_song(self) -> tuple[bool, str]:
        """Returns the next song that should be played."""

        song_matches = [song_map[name] for name in self.current_names]

        if(len(song_matches) < 1):
            return (False, '')
        
        song_to_return = song_matches[0]
        
        return (True, f'songs/{song_to_return}.mp3')
    #end choose_song
