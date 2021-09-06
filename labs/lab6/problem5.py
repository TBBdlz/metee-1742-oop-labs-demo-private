def count_word_in_file(fname: str) -> int:
    with open(fname, 'r') as fr:
        data = fr.read()
        for char in data:
            if char in ',.\n':
                data = data.replace(char, ' ')
        word_list = data.split()

    print(word_list)
    print(f'There are {len(word_list)} in file {fname}')
    return len(word_list)


if __name__ == '__main__':
    file_name = 'lorem.txt'
    count_word_in_file(file_name)
