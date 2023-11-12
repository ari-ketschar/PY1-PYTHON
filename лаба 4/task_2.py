import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as input_:
        reader = csv.DictReader(input_, delimiter=',', quotechar='\n')
        data = [item for item in reader]

    with open(OUTPUT_FILENAME, "w") as output_:
        json.dump(data, output_, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
