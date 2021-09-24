class Teacher:

    def __init__(self, name: str, addr: str, research: str, *course):
        self.name = name
        self.addr = addr
        self.research = research
        self.course = course

    def __str__(self):
        return f'name:{self.name}, address:{self.addr}' \
               f', research:{self.research}, courses:{self.course}'


if __name__ == '__main__':
    manee = Teacher('manee', 'Rm. 4203', 'Artificial Inteligence', 'EN842004', 'EN813701')
    print(manee)
