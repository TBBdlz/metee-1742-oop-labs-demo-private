class Car:

    def __init__(self, name: str, max_speed: int):
        self.name = name
        self.max_speed = max_speed

    def drive(self):  # Must override in Tank class
        print(f'{self.name} moving at top speed {self.max_speed} mph.')


class Tank(Car):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def drive(self):
        super().drive()
        print('Please move away from this thing.')


if __name__ == '__main__':
    car1 = Car('Honda City', 80)
    car1.drive()
    print('---------------')
    tank1 = Tank('M1A1', 60)
    tank1.drive()
