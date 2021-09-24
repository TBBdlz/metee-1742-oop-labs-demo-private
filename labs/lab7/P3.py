import math as m


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return m.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * m.pi * self.radius

    def display_info(self):
        print(f'The circle with radius {self.radius:.2f} has the area as {self.area():.2f}')
        print(f'and the perimeter as {self.perimeter():.2f}')


if __name__ == '__main__':
    while True:
        try:
            r = float(input('Enter a radius:'))
        except ValueError:
            print('Please input valid floating-point number')
        else:
            break
    circle = Circle(r)
    circle.display_info()
