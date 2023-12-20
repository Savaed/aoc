from pathlib import Path


def get_code_1(input: str) -> int:
    code = ""
    for x in input:
        if x.isdigit():
            code += x
            break

    for x in input[::-1]:
        if x.isdigit():
            code += x
            break

    return int(code)


assert get_code_1("1abc2") == 12
assert get_code_1("pqr3stu8vwx") == 38
assert get_code_1("a1b2c3d4e5f") == 15
assert get_code_1("treb7uchet") == 77


input = Path.cwd() / "input.txt"
codes = [get_code_1(line) for line in input.read_text().splitlines()]
code = sum(codes)
print(code)
