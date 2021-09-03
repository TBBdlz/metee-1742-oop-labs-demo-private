import json


def read_json_data(fname: str) -> None:
    with open(fname, 'r') as read_file:
        hobbies = json.load(read_file)

    print(f'{hobbies["name"]} has hobbies as ' + ", ".join(hobbies["hobbies"]))


if __name__ == '__main__':
    read_json_data('hobbies.json')
