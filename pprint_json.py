import json
import sys


def load_data(filename):
    with open(filename) as init_file:
        return json.load(init_file)


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    try:
        init_json_file = sys.argv[1]
        init_json_data = load_data(init_json_file)
        pretty_print_json(init_json_data)
    except IndexError:
       print("You need enter a filename with json data.")