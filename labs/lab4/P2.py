def main() -> None:
    operand1 = float(input('Enter first floating point number: '))
    operand2 = float(input('Enter second floating point number: '))
    operator = input('Please enter an operator (+,-,*,/):')
    try:
        result = eval(f'{operand1} {operator} {operand2}')
        print(f'{operand1} {operator} {operand2} = {result}')
    except ZeroDivisionError:
        print('Cannot divide by zero')


if __name__ == '__main__':
    main()
