from pathlib import Path


def compute_paper_amount(dimensions: str) -> int:
    length, width, height = dimensions.split("x")
    length = int(length)
    width = int(width)
    height = int(height)

    sides = (2 * length * width, 2 * width * height, 2 * length * height)
    return sum(sides) + (min(sides) // 2)


assert compute_paper_amount("2x3x4") == 58
assert compute_paper_amount("1x1x10") == 43

input_path = Path(__file__).parent / "input.txt"
paper_amount = sum([compute_paper_amount(dim) for dim in input_path.read_text().splitlines()])
print(paper_amount)
