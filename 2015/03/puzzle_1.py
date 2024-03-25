from pathlib import Path
from typing import TypeAlias


Coordination: TypeAlias = tuple[int, int]


def move(coordination: Coordination, direction: str) -> Coordination:
    x, y = coordination

    match direction:
        case "^":
            return x, y + 1
        case ">":
            return x + 1, y
        case "v":
            return x, y - 1
        case _:
            return x - 1, y


def deliver_presents(moves: str) -> int:
    coord = (0, 0)
    coords: set[Coordination] = {coord}
    for m in moves:
        coord = move(coord, m)
        coords.add(coord)

    return len(coords)


assert deliver_presents(">") == 2
assert deliver_presents("^>v<") == 4
assert deliver_presents("^v^v^v^v^v") == 2

input_path = Path(__file__).parent / "input.txt"
h = deliver_presents(input_path.read_text())
print(h)
