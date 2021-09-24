class Vehicle:

    def __init__(self, name, speed, mileage):
        self.name = name
        self.__speed = speed
        self.mileage = mileage

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed


class Car(Vehicle):

    def __init__(self, name, speed, mileage, num_doors):
        super().__init__(name, speed, mileage)
        self.num_doors = num_doors

    def __str__(self):
        return f'Name: {self.name} speed: {self.get_speed()} ' \
               f'mileage: {self.mileage} num doors: {self.num_doors}'


class Bus(Vehicle):

    def __init__(self, name, speed, mileage, capacity):
        super().__init__(name, speed, mileage)
        self.capacity = capacity

    def __str__(self):
        return f'Name: {self.name} speed: {self.get_speed()} ' \
               f'mileage: {self.mileage} capacity: {self.capacity}'


if __name__ == '__main__':
    car = Car('Toyota Vios', 90, 150_000, 4)
    bus = Bus('School Volvo', 12, 200_000, 100)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)
