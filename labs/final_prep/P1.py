"""
    There are problem created for understaning OOP
    1. Objects and Classes
    2. Abstraction
    3. Encapsulation
    4. Inheritance
    5. Polymorphism
"""


class User:

    _num_user = 0

    def __init__(self, user_name, email, age):
        self.user_name = user_name
        self.email = email
        self._age = age
        self._id = User._num_user
        User._num_user += 1
