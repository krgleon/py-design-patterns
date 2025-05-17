# Flyweight class: shared object
class Character:
    def __init__(self, symbol: str):
        self.symbol = symbol  # Intrinsic state (shared)

    def display(self, position: int):
        # position is the extrinsic state (unique per usage)
        print(f"{self.symbol} at position {position}")

class CharacterFactory:
    def __init__(self):
        self._characters = {}  # Cache of already-created characters

    def get_character(self, symbol: str) -> Character:
        # Return shared instance if exists, otherwise create and store it
        if symbol not in self._characters:
            self._characters[symbol] = Character(symbol)
        return self._characters[symbol]

factory = CharacterFactory()

document = "AABABACAB" * 100_000
for index, char in enumerate(document):
    letter = factory.get_character(char)
    letter.display(index)
