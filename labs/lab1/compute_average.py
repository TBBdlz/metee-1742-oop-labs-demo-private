import random


def compute_avg() -> None:
    """
    [summary] get numbers from users and print average to consoles
    """
    number_list = []
    while True:
        number = float(input('Enter positive number:'))
        if number <= 0:
            break
        number_list.append(number)
    try:
        average = sum(number_list) / len(number_list)
        print('Numbers are', number_list)
        print(f'The average number of the list is {average:.2f}')
    except ArithmeticError as e:
        print(e)


def compute_avg_list(n: int) -> None:
    """
    [summary] ask users to input <n> numbers and compute average
              then print to the console

    Args:
        n (int): [number in the list]
    """
    numbers_str = input(f'Enter {n} positive numbers:')
    print('You entered', numbers_str)
    number_list_str = numbers_str.split()
    print('Numbers are', number_list_str)
    number_list = [int(i) for i in number_list_str]
    average = sum(number_list) / len(number_list)
    print(f'The average number of the list is {average:.2f}')


def test_compute_avg_list() -> None:
    """
    [summary] random integer and run compute_avg_list(n) function
    """
    min_number: int = 1
    max_number: int = 10
    n = random.randint(min_number, max_number)
    compute_avg_list(n)


if __name__ == '__main__':
    test_compute_avg_list()
    compute_avg()
