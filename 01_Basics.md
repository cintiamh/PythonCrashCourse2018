# Part I - Basics

1. [Getting Started](#getting_started)
2. [Variables and simple data types](#variables_and_simple_data_types)
3. [Introducing lists](#introducing_lists)
4. [Working with lists](#working_with_lists)
5. [If statements](#if_statements)
6. [Dictionaries](#dictionaries)
7. [User input and while loops](#user_input_and_while_loops)
8. [Functions](#functions)
9. [Classes](#classes)

## Getting Started

```python
print("Hello world!")
```

Start Python console:
```
$ python
or
$ python3
```

You can exit with CTRL+D or enter `exit()`.

[hello_world.py](basics/hello_world.py)

Run file:
```
$ python3 hello_world.py
```

## Variables and simple data types

### Variables

```python
message = "Hello Python world!"
print(message)
```

### Strings

* Series of characters.

```python
"This is a string."
'This is also a string.'
```

[name.py](basics/name.py)

```python
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
```

#### Combining or concatenating strings

```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
```

#### Adding whitespace to strings with tabs or newlines

* `\t` - tab
* `\n` - newline

#### Stripping whitespace

Temporarily remove whitespace at the right end of a string:
```python
favorite_language = 'python '
# strips from right side
favorite_language.rstrip()
# strips from left side
favorite_language.lstrip()
# strips from both sides
favorite_language.strip()
```

### Numbers

#### Floats

Float is any number with a decimal point.

#### Avoid type errors with the str() function

```python
age = 23
# str() here is used to convert a number to string before combining it.
# without str() it will fire an error
message = "Happy " + str(age) + "rd Birthday!"
print(message)
```

#### Integers in Python 2

Integer division in Python 2 is treated different.
```python
>>> 3 / 2
1
>>> 3.0 / 2
1.5
```

### Comments

Comment is done with `#`.

### The Zen of Python

```
# Prints out a list of principles
>>> import this
```

## Introducing lists

[bicycles.py](basics/bicycles.py)

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

### Accessing elements in a list

Lists are ordered collections.

Access by index:
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
```

Get the last element:
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
```

### Modifying elements in a list

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
```

### Appending elements to the end of a list

```python
motorcycles.append('ducati')
```

### Inserting elements into a list

```python
motorcycles.insert(0, 'ducati')
```

### Removing an item using the del statement

```python
del motorcycles[0]
```

### Removing an item using the pop() method

The `pop()` method removes the last item in a list, and it lets you work with that item after removing it.

```python
popped_motorcycle = motorcycles.pop()
```

### Popping items from any position in a list

```python
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
```

### Removing an item by value

`remove()` deletes only the first occurrence of the specified value.

```python
motorcycles.remove('yamaha')
```

### Organizing a list

#### Sorting a list permanently with the sort() method

[cars.py](basics/cars.py)

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
```

Reversed sort:
```python
cars.sort(reverse=True)
print(cars)
```

#### Sorting a list temporarily with the sorted() function

This doesn't change cars order
```python
print(sorted(cars))
```

#### Printing a list in reverse order

Just reverse the original list:
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
```

#### Finding the length of a list

```python
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4
```

You can access the last element using `-1`

## Working with lists

### Looping through an entire list

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

### Avoid indentation errors

Python uses indentation to determine when one line of code is connected to the line above it.

### Making numerical lists

#### Using the range() function

numbers.py
```python
for value in range(1, 5):
    print(value) // prints 1 to 4
```

#### Using range() to make a list of Numbers

even_numbers.py
```python
even_numbers = list(range(2, 11, 2))
print(even_numbers)
```

squares.py
```python
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)
```

#### Simple statistics with a list of numbers

```python
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```

#### List comprehensions

```python
squares = [value**2 for value in range(1,11)]
```

### Working with part of a list

slice => a specific group of items in a list.

#### Slicing a list

[players.py](./basics/players.py)
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```

If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list.

```python
print(players[:4])
```

A similar syntax works if you want a slice that includes the end of a list.

```python
print(players[2:])
print(players[-3:]) # 3 last elements
```

#### Copying a list

You can make a slice that includes all elements from the original.
[foods.py](./basics/foods.py)
```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
```

If don't use the slice, and just assign the original list to a new one, it will just be pointing to it. Changes in one list will reflect on the other.

### Tuples

Tuple is a immutable list.
Define a tuple using `()` instead of `[]` (list)

[dimensions.py](./basics/dimensions.py)

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
```

Python raises an error when we try to change a tuple's value.

#### Looping through

```python
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
```

You can't modify a tuple, but you can assign a new value to a variable that holds a tuple.

### Styling your code

*Python Enhancement Proposal (PEP)* - current: PEP8

https://python.org/dev/peps/pep-0008/

#### Indentation

* 4 spaces

Mixing tabs and spaces can cause problems.

#### Line length

* code <= 80 chars
* comments <= 72 chars

#### Blank lines

* use blank lines to organize your files

## If statements

### A simple example

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

### Checking for inequality (and)

```python
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
```

### Checking multiple conditions (or)

```python
age_0 >= 21 and age_1 <= 22
age_0 > 9 or age_1 > 22
```

### Checking whether a value is in a list

```python
'mushrooms' in requested_toppings
user not in banned_users
```

### Boolean expressions

```python
game_active = True
can_edit = False
```

### if-else statements

```python
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10")
```

Refactoring:
```python 
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
```

#### Checking that a list is not empty

```python
requested_toppings = []

if requested_toppings:
  for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
  print("\nFinished making your pizza.")
else:
  print("Are you sure you want a plain pizza?")
```

#### Using multiple lists

```python 
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                        'pepperoni', 'pinaple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding: " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza")
```

## Dictionaries

### A simple dictionary

A dictionary is a collection of key-value pairs.

```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
```

### Adding new key-value pairs

Dictionaries are dynamic structures.

```python 
alien_0['x_position'] = 0
alien_0['y_position'] = 25
```

### Removing key-value pairs

```python 
del alien_0['points']
```

### A dictionary of similar objects

Multiple lines:
```python 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")
```

### Looping through a dictionary

#### Looping through all key-value pairs

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
```

`.items()` returns a list of key value pairs

#### Looping through all the keys in a dictionary

`.keys()` returns a list of all keys

```python
for name in favorite_languages.keys():
    print(name.title())
```

Looping through keys is the default behavior.
Same result:
```python
for name in favorite_languages:
    print(name.title())
```

Check if a key is not in the list:
```python 
if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")
```

#### Looping through a dictionary's keys in order

```python
for name in sorted(favorite_languages):
    print(name.title() + ", thank you for taking the poll.")
```

#### Looping through all values in a dictionary

`.values()` returns a list of values without any keys.

```python 
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
```

`set()` removes duplicates from list.
```python 
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
```

### Nesting

#### A list of dictionaries

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

Dynamically generating aliens:
```python
# Make an empty list of storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens 
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
```

#### A list in a dictionary

[pizza.py](./basics/pizza.py)
```python 
# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")    

for topping in pizza['toppings']:
    print("\t" + topping)
```

#### A dictionary in a dictionary

[many_users.py](./basics/many_users.py)
```python 
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstain',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
```

## User input and while loops

### How the input() function works

`input()` - pauses and waits for user input.

[parrot.py](./basics/parrot.py)
```python 
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

#### Using `int()` to accept numerical input

Python interprets input as a string.

[rollercoaster.py](./basics/rollercoaster.py)
```python 
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

#### The modulo operator (%)

* divides one number by another and returns the remainder.

#### Accepting input in Python 2.7

`raw_input()` => returns a string
`input()` => tries to run as Python code

### Introducing while loops

`while` loop runs as long as a certain condition is true.

#### The while loop in action

[counting.py](./basics/counting.py)
```python 
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

#### Letting the user choose when to quit

[parrot.py](./basics/parrot.py)
```python 
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
```

#### Using a flag

[parrot.py](./basics/parrot.py)
```python 
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
```

#### Using a break to exit a loop

[cities.py](./basics/cities.py)
```python 
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
```

#### Using continue in a loop

[counting.py](./basics/counting.py)
```python 
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

### Using a while loop with lists and dictionaries

[confirmed_users.py](./basics/confirmed_users.py)
```python 
# Start with users that need to be verified
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed usersself.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed_users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

[pets.py](./basics/pets.py)
```python 
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

[mountain_poll.py](./basics/mountain_poll.py)
```python 
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat's your name?")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (y/n) ")
    if repeat == 'n':
        polling_active = False

# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
```

## Functions

greeter.py
```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
    
greet_user()
```

### Passing information to a function

```python 
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
    
greet_user('cintia')
```

#### Positional arguments

pets.py
```python 
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
```

#### Keyword arguments

Using keywords the order doesn't matter:
```python 
describe_pet(pet_name='penny', animal_type='dog')
```

#### Default values

Prefer to leave arguments without default values in the beginning. Because positioning still applies.

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
```

### Return values

#### Returning a simple value

```python 
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

#### Making an argument optional

You can use default values to make an argument optional:

```python 
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else: 
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

#### Returning a dictionary

person.py
```python 
def build_person(first_name, last_name, age=''):
    person = { 'first': first_name, 'last': last_name }
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

#### Using a function with a while loop

```python 
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else: 
        full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
```

#### Passing a list

##### Preventing a function from modifying a list

```python
function_name(list_name[:])
```

The slice notation `[:]` makes a copy of the list to send to the function.

You should pass the original list to functions unless you have a specific reason to pass a copy.

#### Passing an arbitrary number of arguments

pizza.py
```python 
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

`*toppings` make an empty tuple called `toppings` and pack whatever values in receives into this tuple.

#### Using arbitrary keyword arguments

user_profile.py
```python 
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)
```

`**user_info` create an empty dictionary called `user_info` and pack whatever name-value pairs it receives into this dictionary.

### Storing your functions in modules

You can store your functions in a separated file called a *module* and then *importing* that module into your main program.

#### Importing an entire module

pizza.py
```python 
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
```

making_pizzas.py
```python
import pizza 

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

And run:
```
$ python3 basics/making_pizzas.py 
```

#### Importing specific functions

```python 
from module_name import function_0, function_1, function_2
```

With this syntax you don't need to use the dot notation.

#### Using as to give a function an alias

```python 
from module_name import function_name as fn
```

#### Using as to give a module an alias

```python
import module_name as mn
```

#### Importing all functions in a module

```python
from module_name import *
```

`*` tells Python to copy every function from the module. You can call each function by name without using the dot notation.

The best approach is to import the function or functions you want, or import the entire module and use dot notation.

### Styling functions

* Descriptive names, lowercase letters, underscores.
* Every function should have a comment.
* If you specify a default value for a parameter, no spaces on either side of the equal sign.
* PEP 8: https://www.python.org/dev/peps/pep-0008/
* Line length: 79
* All `import` statements should be written at the top.

## Classes

### Creating and using a class

dog.py
```python 
class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
```

* `Dog`: Capitalized names for class 
* `__init__()`: Special method that runs automatically whenever we create a new instance of `Dog`.
* `self`: this parameter is required and it must come first. Every method call associated with a class automatically pass the `self` argument.

#### Creating classes in Python 2.7

```python
class Dog(object): # you need to pass in object
  --snip--
```

#### Making an instance from a class

Accessing attributes
```python 
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
```

Calling methods:
```python 
my_dog.sit()
my_dog.roll_over()
```

### Working with classes and instances

car.py
```python 
class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
```

#### Setting a default value for an attribute

Every attribute in a class needs an initial value. You can define the initial value in the body of the `__init__()` method.

#### Modifying attribute values

* modifying an attribute's value directly:
  * `my_new_car.odometer_reading = 23`
* modifying an attribute's value through a method
* Incrementing an attribute's value through a method

car.py
```python 
class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
```

### Inheritance

#### The `__init__()` method for a child class

car.py
```python 
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
```

* The parent class must appear before the child class in the file.
* The name of the parent class must be included in parentheses in the definition of the child class.
* The `super()` function helps making connections between the parent and child class.

* You can override any methods from the parent class on the child class.

```python 
class Car():
  # ...

class Battery():
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```

### Importing Classes
