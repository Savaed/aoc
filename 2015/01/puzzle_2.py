from pathlib import Path


def get_first_basement_position(instruction: str) -> int | None:
    up = 0
    down = 0

    for position, direction in enumerate(instruction, 1):
        if direction == "(":
            up += 1
        else:
            down += 1

        if up - down < 0:
            return position

    return None


assert get_first_basement_position(")") == 1
assert get_first_basement_position("()())") == 5

input_path = Path(__file__).parent / "input.txt"
instruction = input_path.read_text()
basement_position = get_first_basement_position(instruction)
print(basement_position)
