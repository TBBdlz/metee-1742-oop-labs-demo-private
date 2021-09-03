def read_user_file() -> None:
    file_name = input('Enter a filename:')
    with open(file_name, 'r') as fr:
        print(fr.read())


if __name__ == '__main__':
    read_user_file()
