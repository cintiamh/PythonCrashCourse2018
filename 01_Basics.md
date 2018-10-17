# Part I - Basics

1. [Getting Started](#getting_started)
2. [Variables and simple data types](#variables_and_simple_data_types)
3. [Introducing lists](#introducing_lists)
4. [Working with lists](#working_with_lists)

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
