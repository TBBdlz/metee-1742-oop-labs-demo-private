"""
Sum of all odd number
author: Metee Yingyongwatthanakit
date: 5 August 2021
"""


def compute_sum_positive_odd_numbers() -> None:
    data_list = [int(x) for x in input('Enter numbers in the list: ').split()]
    data_odd_num = list(filter(lambda t: t % 2 == 1 and t > 0, data_list))
    print(sum(data_odd_num))


if __name__ == '__main__':
    compute_sum_positive_odd_numbers()
