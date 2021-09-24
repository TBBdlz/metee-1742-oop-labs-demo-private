class Numbers:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def display_factors(cls, number):
        if number % 2 == 0:  # even number case
            factor = number // 2
            return f'Factors of {number} is {factor} and {factor}'
        else:  # odd number case
            upper_factor = number // 2 + 1
            lower_factor = number // 2
            return f'Factors of {number} is {upper_factor} and {lower_factor}'

    @classmethod
    def is_valid_divisor(cls, divisor):
        if divisor != 0:
            return f'{divisor} is a valid divisor'
        else:
            return f'{divisor} is not a valid divisor'


if __name__ == '__main__':
    xp = 2
    yp = 3
    print(f'{xp} + {yp} is {Numbers(xp, yp).add()}')
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(7))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))
