def calc_diff(num1: int, num2: int) -> float:
    return (num2 - num1) / num1 * 100


def main() -> None:
    num_infected_yesterday = int()
    num_infected_today = int()
    while True:  # number of infected cases yesterday
        try:
            num_infected_yesterday: int = int(input('Enter the number of new infected Covid-19 cases for yesterday: '))
            if num_infected_yesterday < 0:
                raise TypeError
            break
        except ValueError:
            print('Please enter a Valid Integer')
            print('Stay healthy!')
            continue
        except TypeError:
            print('You can only enter a non-negative integer')
            print('Stay healthy!')
            continue
    while True:  # number of infected cases today
        try:
            num_infected_today: int = int(input('Enter the number of new infected Covid-19 cases for today: '))
            if num_infected_today < 0:
                raise TypeError
            break
        except ValueError:
            print('Please enter a Valid Integer')
            print('Stay healthy!')
            continue
        except TypeError:
            print('You can only enter a non-negative integer')
            print('Stay healthy!')
            continue
    difference = calc_diff(num_infected_yesterday, num_infected_today)
    print(f'The difference of the number of new infected cases is {difference:.2f}%')


if __name__ == '__main__':
    main()
