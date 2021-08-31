def robust_calculator() -> None:
    operand1 = get_operand('Please enter the first operand (\'q\' to quit):')
    operand2 = get_operand('Please enter the second operand (\'q\' to quit):')
    operation = input('Enter an operation (\'+\', \'-\', \'*\', \'/\'):')
    format_type = input('Enter output format (float, int):')
    try:
        if operation in "+-*/":
            result = eval(f'{operand1} {operation} {operand2}')
            if format_type == 'int':
                print(f'{operand1} {operation} {operand2} = {round(result)}')
            elif format_type == 'float':
                print(f'{operand1} {operation} {operand2} = {result}')
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except Exception as e:
        print(e)


def get_operand(prompt_text: str):
    operand = ''
    while True:
        try:
            operand = input(prompt_text)
            if operand.lower() == 'q':
                exit()
            if operand.isalpha():
                raise ValueError
            operand = float(operand)
            break
        except ValueError:
            print('Please enter a floating point number')
            continue

    return operand


if __name__ == '__main__':
    robust_calculator()
