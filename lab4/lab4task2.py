import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f1:
        lines = [line1 for line1 in csv.DictReader(f1)]
    with open(OUTPUT_FILENAME, 'w') as f2:
        json.dump(lines, f2, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
