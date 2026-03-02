import random 
class Encryptor:
    def __init__(self, number):
        self.__number = number

    def __str__(self):
        return str(self.__encrypt())

    def __encrypt(self):
        operations = ['+', '-', '*', '/']
        operation = random.choice(operations)
        if operation == '+':
            return self.__number + random.randint(1, 10)
        elif operation == '-':
            return self.__number - random.randint(1, 10)
        elif operation == '*':
            return self.__number * random.randint(1, 10)
        elif operation == '/':
            return self.__number / random.randint(1, 10)
