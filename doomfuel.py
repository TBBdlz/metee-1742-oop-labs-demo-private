import numpy as np


def transform(a):
    res = []
    for row in a:
        if sum(row) == 0:
            res.append(row)
        else:
            n = sum(row)
            p_row = [row[i] / n for i in range(len(row))]
            res.append(p_row)

    return res


def calc_prob_iterative(i, a: np.array, ROUND=10000):
    choose: np.array = np.array(a[i])
    for _ in range(ROUND):
        choose = choose.matmul(a)
    return choose


arr = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

if __name__ == '__main__':
    p_arr = transform(arr)
    com_arr = np.array(p_arr)
    pi = calc_prob_iterative(0, p_arr)
    print(com_arr)
    print(pi)
