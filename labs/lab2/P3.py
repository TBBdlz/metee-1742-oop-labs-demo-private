data_list = [1, 2, 3, 4, 5]


def add_number_to_list() -> None:
    global data_list
    print(f'Before adding an integer, the list is {data_list}')
    append_num = int(input('Enter a number to add a list: '))
    data_list.append(append_num)
    print(f'After adding an integer {append_num}, the list is {data_list}')


def replace_number_in_list() -> None:
    global data_list
    data_copy = data_list.copy()
    print(f'Finding a number to replace in the list {data_copy}')
    find_num = int(input('Enter a number to find: '))
    index = data_copy.index(find_num)
    replace_num = int(input('Enter a new number to replace: '))
    data_copy[index] = replace_num
    print(f'After replacing {find_num} with {replace_num}, the new list is {data_copy}')


def remove_number_in_list() -> None:
    global data_list
    print(f'Finding a number to replace in the list {data_list}')
    remove_num = int(input('Enter a number to remove: '))
    data_list.remove(remove_num)
    print(f'After removing 7, the list is {data_list}')


if __name__ == '__main__':
    add_number_to_list()
    replace_number_in_list()
    remove_number_in_list()
