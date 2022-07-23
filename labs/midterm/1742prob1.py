"""
    Prob1 is GPA calculating program take name, gpas as input
    and compare gpa to {my_gpa} in program
    author: Metee Yingyongwatthanakit
    date: 29 October 2021
"""


def main() -> None:
    my_name: str = 'Metee'
    my_id: str = '633040174-2'
    my_gpa: float = 3.92
    # Welcome Text
    print(f'Welcome to program prob1.py by {my_name}, {my_id} who has average GPA as {my_gpa}')

    # Getting user input
    gpa_list: list[float] = []
    username = input('Enter your name:')
    while True:
        try:
            user_gpa = float(input('Enter GPA:'))
            if user_gpa < 0 or user_gpa > 4:  # GPA is out of bound [0, 4]
                print('GPA must be in range [0.0, 4.0]')
                print('Please enter valid GPA')
                break
            gpa_list.append(user_gpa)
        except ValueError:
            print('GPA must be a floating point number')
            print('Please enter valid GPA')
            break

    try:  # there's data in gpa_list
        average_gpa = average(gpa_list)
        print(f'{username} has the average GPA as {average_gpa:.2f}')
        if average_gpa > my_gpa:
            print(f'{username} has the average GPA greater than mine by {(average_gpa - my_gpa):.2f}')
        elif average_gpa < my_gpa:
            print(f'{username} has the average GPA less than mine by {(my_gpa - average_gpa):.2f}')
        else:
            print(f'{username} has the average GPA the same as mine')
    except ZeroDivisionError:  # in case of empty list exit the program
        exit()


def average(datas: list[float]) -> float:
    total: int = 0
    for data in datas:
        total += data
    avg_val: float = total / len(datas)  # datas = [], avg_val = 0 / 0

    return avg_val


if __name__ == '__main__':
    main()
