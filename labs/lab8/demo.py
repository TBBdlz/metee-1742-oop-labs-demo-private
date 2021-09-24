class Cat:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    def __str__(self):  # return string -> print(object)
        # name : {name}, age : {age}
        return f'name : {self.get_name()}, age : {self.get_age()}'

    def meow(self):
        print('Meow give me food!')


class A(Cat):

    def __init__(self, name, age, cat_id):
        super().__init__(name, age)
        self.__id = cat_id

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def __str__(self):
        return f'name : {self.get_name()}, age : {self.get_age()}, id : {self.get_id()}'

    def meow(self):
        super().meow()
        print('Give me money too')


if __name__ == '__main__':
    cat = Cat('Rainy', 2)
    xcat = A('Xcat', 99, 1234223)
    print(cat)
    print(xcat)
    print('---')
    cat.meow()
    print('---')
    xcat.meow()
