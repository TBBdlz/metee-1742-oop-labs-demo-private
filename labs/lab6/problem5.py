def count_word_in_file(fname) -> None:
    with open(fname, 'r') as fr:
        data = fr.read()
        for char in data:
            if char == '.' or char == ',' or char == '\n':
                data = data.replace(char, ' ')
        word_list = data.split()

    print(word_list)
    print(f'There are {len(word_list)} in file {fname}')


if __name__ == '__main__':
    FILE_NAME = 'lorem.txt'
    count_word_in_file(FILE_NAME)
