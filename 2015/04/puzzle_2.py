import itertools
from hashlib import md5
from pathlib import Path


def find_hash(input: str) -> int:
    for i in itertools.count():
        x = input + str(i)
        h = md5(x.encode(), usedforsecurity=False)

        if h.hexdigest().startswith("000000"):
            print(h.hexdigest())
            return i


input_path = Path(__file__).parent / "input.txt"
x = find_hash(input_path.read_text().strip())
print(x)
