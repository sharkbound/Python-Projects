from typing import Any, Dict, Optional, Generator, Tuple


class Interactable:
    def __init__(self, key: Any):
        self.key = key

    def interact(self):
        pass

    def can_interact(self) -> bool:
        return True


class Interactables:
    def __init__(self):
        self.items: Dict[Any, Interactable] = {}

    def get(self, key, default=None) -> Optional[Interactable]:
        return self.items.get(key, default)

    def __setitem__(self, key: Any, value: Interactable):
        self.items[key] = value

    def __iter__(self) -> Generator[Tuple[Any, Interactable], None, None]:
        yield from self.items.items()

    def __contains__(self, key) -> bool:
        return key in self.items

    def __getitem__(self, key) -> Interactable:
        return self.items[key]
