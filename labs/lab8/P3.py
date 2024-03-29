class Pet:

    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f'I\'m {self.name}')

    def move(self):
        print('moving ...')



class Cat(Pet):

    def __init__(self, name, owner, color):
        super().__init__(name)
        self.owner = owner
        self.color = color

    def show_info(self):
        super().show_info()
        print(f'and is {self.color}')
        print(f'belonging to {self.owner}')

    def move(self):
        print('Cat likes to walk more than run')


    def __del__(self):
        print(f'Oh no! ma boi {self.name}')


class Dog(Pet):

    def __init__(self, name, owner, color):
        super().__init__(name)
        self.owner = owner
        self.color = color

    def show_info(self):
        super().show_info()
        print(f'and is {self.color}')
        print(f'belonging to {self.owner}')

    def move(self):
        print('Dog likes to run more than walk')

    def eat_cat(self, cat: Cat):
        print(f'Dog {self.name} eats cat {cat.name}')
        del cat


if __name__ == '__main__':
    pet1 = Pet('Thongdaeng')
    pet1.show_info()
    pet1.move()
    cat1 = Cat('Thongdee', 'Manee', 'white')
    cat1.show_info()
    cat1.move()
    dog1 = Dog('Thongdum', 'Mana', 'black')
    dog1.show_info()
    dog1.move()
    dog1.eat_cat(cat1)
    print(cat1 == None)
    print(cat1)
