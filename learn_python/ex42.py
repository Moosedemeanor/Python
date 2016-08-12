#!/usr/bin/env python2.7
"""
is-a - use when you talk about objects and classes being related to each other by a 
		class relationship
has-a - use when you talk about objects and classes that are related only because they 
		reference each other.
"""

## Animal is-a object
class Animal(object):
		
		def __init__(self, name):
				self.name = name
				print self.name, "is an animal"

## Dog is-a Animal
class Dog(Animal):
		
		def __init__(self, name):
				## Dog has-a name
				self.name = name
				print self.name, "is a dog."

## Cat is-a Animal
class Cat(Animal):

		def __init__(self, name):
				## Cat has a name
				self.name = name
				print self.name, "is a cat."
				
## Person is-a object
class Person(object):

		def __init__(self, name):
				## Person has-a name
				self.name = name
				
				## Person has-a pet
				self.pet = None
				print self.name, "is a person."

## Employee is-a Person
class Employee(Person):

		def __init__(self, name, salary):
				## Employee has-a name
				super(Employee, self).__init__(name)
				## Employee has-a salary
				self.salary = salary
				print self.name, "is an employee with a salary of $", self.salary
				
## Fish is-a object
class Fish(object):
		pass
## Salmon is-a Fish
class Salmon(Fish):
		pass
## Halibut is-a Fish
class Halibut(Fish):
		pass
		
## rover is-a Dog
rover = Dog("Rover")
## satan is-a Cat
satan = Cat("Satan")
## mary is-a Person
mary = Person("Mary")
## mary has-a pet named satan
mary.pet = satan
## frank is-a employee with a salary of $120,000
frank = Employee("Frank", 120000)
## frank has-a pet named rover
frank.pet = rover
## flipper is-a Fish
flipper = Fish()
## crouse is-a Salmon
crouse = Salmon()
## harry is-a Halibut
harry = Halibut()
