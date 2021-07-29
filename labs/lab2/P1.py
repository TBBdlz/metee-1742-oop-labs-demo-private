def celsius_to_fahrenheit(c: float) -> float:
    temp_fah = (9 / 5) * c + 32
    return temp_fah


def main() -> None:
    try:
        temp_input = float(input('Enter a temperature in Celsius: '))
        temp_fah = celsius_to_fahrenheit(temp_input)
        print(f'{temp_input:.2f} in Celsius is {temp_fah:.2f} Fahrenheit')
    except ValueError:
        print('Please enter a valid floating point for the temperature.')
        main()


if __name__ == '__main__':
    main()
