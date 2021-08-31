def squared_sum() -> None:
    n = int(input('Enter an integer: '))
    data_list = list(range(1, n + 1))
    sum_squared = sum(list(map(lambda t: t * t, data_list)))
    print('The sum of the square of', data_list, 'is', sum_squared)


if __name__ == '__main__':
    squared_sum()
