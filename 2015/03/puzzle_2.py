from pathlib import Path
from typing import TypeAlias


Coordinates: TypeAlias = tuple[int, int]


def move(coordinates: Coordinates, direction: str) -> Coordinates:
    x, y = coordinates

    match direction:
        case "^":
            return x, y + 1
        case ">":
            return x + 1, y
        case "v":
            return x, y - 1
        case _:
            return x - 1, y


def deliver_presents(moves: str) -> set[Coordinates]:
    coord = (0, 0)
    coords: set[Coordinates] = {coord}

    for m in moves:
        coord = move(coord, m)
        coords.add(coord)

    return coords


def get_num_houses(moves: str) -> int:
    santa_moves = moves[:-1:2]
    robot_moves = moves[1::2]
    houses = deliver_presents(santa_moves) | deliver_presents(robot_moves)
    return len(houses)


assert get_num_houses("^v") == 3
assert get_num_houses("^>v<") == 3
assert get_num_houses("^v^v^v^v^v") == 11

input_path = Path(__file__).parent / "input.txt"
input = input_path.read_text()
houses = get_num_houses(input)
print(houses)
