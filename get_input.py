import requests
import json
from pathlib import Path
import argparse

CONFIG_PATH = Path(__file__).parent / "settings.json"


def main() -> int:
    cfg = json.loads(CONFIG_PATH.read_text())

    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", type=int, default=cfg["year"])
    parser.add_argument("-d", "--day", type=int, default=cfg["day"])
    args = parser.parse_args()

    url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"
    response = requests.get(url, cookies=cfg["cookies"])
    output: Path = (
        Path(__file__).parent / str(args.year) / f"{args.day:02}" / "input.txt"
    )
    output.touch()
    output.write_text(response.text)
    return 0


if __name__ == "__main__":
    main()
