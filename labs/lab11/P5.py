import sys

USAGE_TEXT = f'Usage:python {__file__} <operator> <operand1> <operand2>'
INVALID_WARNING = 'Operands are invalid. They are not numbers.'


def main() -> None:
    global USAGE_TEXT, INVALID_WARNING
    try:
        operator = sys.argv[1]
        if operator.lower() == 'q':
            print('Program quits...')
            exit()
        first_operand: float = float(sys.argv[2])
        second_operand: float = float(sys.argv[3])
        if operator not in {'+', '-', 'x', '/'}:
            raise ValueError
        if operator != 'x':
            result: float = eval(
                f'{first_operand} {operator} {second_operand}')
        else:
            result: float = eval(
                f'{first_operand} * {second_operand}')
        print(f'{first_operand} {operator} {second_operand} is {result}')
    except IndexError:
        print(USAGE_TEXT)
    except ValueError:
        print(INVALID_WARNING)
    except ZeroDivisionError:
        print(f'{first_operand} cannot be divided by {second_operand}')


if __name__ == '__main__':
    main()
