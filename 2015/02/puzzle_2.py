from pathlib import Path


def compute_ribbon_lenght(dimension: str) -> int:
    l, w, h = dimension.split("x")
    l = int(l)
    w = int(w)
    h = int(h)

    shortest_sides = sorted((l, w, h))[:2]
    ribbon = 2 * shortest_sides[0] + 2 * shortest_sides[1]
    bow = l * w * h
    return ribbon + bow


assert compute_ribbon_lenght("2x3x4") == 34
assert compute_ribbon_lenght("1x1x10") == 14

input_path = Path(__file__).parent / "input.txt"
total_ribbon = sum(
    [compute_ribbon_lenght(dim) for dim in input_path.read_text().splitlines()]
)
print(total_ribbon)
