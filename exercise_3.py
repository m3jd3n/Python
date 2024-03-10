class Animal:
    def __init__(self, age, name):
        print('Animal!')
        self.age = age
        self.name = name
    def increase_age(self, by_how_much = 1):
        self.age += by_how_much
        print(f'{self.name} age increased to {self.age}')

class Mammal(Animal):
   def __init__(self, age = None, name = None):
       Animal.__init__(self, age, name)
       print('Mammal!')

   def introduce_yourself(self):
       print(f'I am {self.name} and I am {self.age} years old')

class Cat(Mammal):
    def __init__(self, age, name, master):
        Mammal.__init__(self, age, name)
        self.master = master
        print('Cat!')

    def purr(self):
        print('Purr!')

    def introduce_yourself(self):
        super().introduce_yourself()
        print(f"My master's name is {self.master}")

class Dog(Cat):
    def __init__(self, age, name, master, fav_toy = None):
        Mammal.__init__(self, age, name)
        self.master = master
        self.fav_toy = fav_toy
        print('Dog!')

    def favourite_toy(self):
        print(f"My favourite toy is {self.fav_toy}")

    def introduce_yourself(self):
        super().introduce_yourself()
        print(f"My favourite toy is {self.fav_toy}")

kot = Cat(12,"Rademenes", master = "Artur")
kot.introduce_yourself()
kot.purr()
kot.increase_age(2)

pies = Dog(name = "Reksio", age = 8, master = "Artur")
pies.introduce_yourself()
pies = Dog(name = "Reksio", age = 8, master = "Artur", fav_toy="Pluszowy kot")
pies.introduce_yourself()
pies.increase_age(4)