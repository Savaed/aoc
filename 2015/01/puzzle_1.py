from collections import Counter
from pathlib import Path


def which_floor(instruction: str) -> int:
    directions = Counter(instruction)
    floor = directions["("] - directions[")"]
    return floor


assert which_floor("((()))") == 0
assert which_floor("((())") == 1
assert which_floor("))(") == -1

input_path = Path(__file__).parent / "input.txt"
instruction = input_path.read_text()
floor = which_floor(instruction)
print(floor)
