class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_width(self, new_width):
        self.__width = new_width

    def get_width(self):
        return self.__width

    def set_height(self, new_height):
        self.__height = new_height

    def get_height(self):
        return self.__height

    def __str__(self):
        return f'This rectangle has width as {self.get_width()} height as {self.get_height()}'


if __name__ == '__main__':
    rect1 = Rectangle(3, 4)
    print(rect1)
    print(f'Width is {rect1.get_width()}')
    print(f'Height is {rect1.get_height()}')