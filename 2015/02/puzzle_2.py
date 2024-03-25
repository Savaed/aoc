from pathlib import Path


def compute_ribbon_lenght(dimension: str) -> int:
    lenght, width, height = dimension.split("x")
    lenght = int(lenght)
    width = int(width)
    height = int(height)

    shortest_sides = sorted((lenght, width, height))[:2]
    ribbon = 2 * shortest_sides[0] + 2 * shortest_sides[1]
    bow = lenght * width * height
    return ribbon + bow


assert compute_ribbon_lenght("2x3x4") == 34
assert compute_ribbon_lenght("1x1x10") == 14

input_path = Path(__file__).parent / "input.txt"
total_ribbon = sum([compute_ribbon_lenght(dim) for dim in input_path.read_text().splitlines()])
print(total_ribbon)
