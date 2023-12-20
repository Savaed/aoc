from pathlib import Path


DIGITS = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_code(line: str) -> int:
    first_digit = {}
    last_digit = {}

    for digit, code in DIGITS.items():
        fi = line.find(digit)
        if fi > -1:
            first_digit[fi] = code

        li = line.rfind(digit)
        if li > -1:
            last_digit[li] = code

    code = first_digit[min(first_digit)]
    code += last_digit[max(last_digit)]
    return int(code)


assert find_code("two1nine") == 29
assert find_code("eightwothree") == 83
assert find_code("abcone2threexyz") == 13
assert find_code("xtwone3four") == 24
assert find_code("4nineeightseven2") == 42
assert find_code("zoneight234") == 14
assert find_code("7pqrstsixteen") == 76

input = Path.cwd() / "input.txt"
codes = [find_code(line) for line in input.read_text().splitlines()]
code = sum(codes)
print(code)
