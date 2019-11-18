# Elizabeth Fuller
# 11/18/19
# is-a, has-a

# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name


# Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name


# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        # run the __init__ method of a parent class reliably
        self.__init__(name)
        super().__init__(name)
        # Employee has-a salary
        self.salary = salary


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a Fish
class Salmon(Fish):
    pass


# Halibut is-a fish
class Halibut(Fish):
    pass


# Rover is-a Dog
rover = Dog("Rover")

# Satan is-a Cat
satan = Cat("Satan")

# Mary is-a Person
mary = Person("Mary")

# Mary's pet is satan
mary.pet = satan

# Frank is-a Employee, salary is 120000
frank = Employee("Frank", 120000)

# Frank's pet is rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
