import copy

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def __str__(self):
        return f'Name: {self.name}, Address: {self.address}'

john = Person('John', '123, London Road')


jane = copy.deepcopy(john)
jane.name = 'Jane'
jane.address = '124, London Road'

print(john)
print('---')
print(jane)
