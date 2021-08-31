def calc():
    a = input_val('Enter any number: ')
    b = input_val('Enter second integer: ')
    print(a + b)


def input_val(prompt_text):
    #  number only
    x = 0
    while True:  # วนไปเรื่อย ๆ จนกว่าจะสามารถแปลง x เป็นตัวเลขได้
        try:
            x = float(input(prompt_text))
            break
        except ValueError:
            print('Please enter valid number not string')
            continue

    return x


if __name__ == '__main__':
    calc()
