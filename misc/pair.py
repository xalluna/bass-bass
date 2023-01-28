

from typing import Callable


class Pair():

    pairings: list[list[str]]
    simple_mappings: dict[str , str]
    complex_mappings: dict[list[str] , str]


    def __init__(self) -> None:
        pass

    def add_simple_pair(self, key: str, value) -> None:
        pass

    def add_complex_pair(self, key: list[str], value) -> None:
        pass

    def add_rule(self, rule: Callable[..., bool]) -> None:
        pass