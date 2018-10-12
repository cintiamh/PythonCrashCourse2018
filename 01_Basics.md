# Part I - Basics

1. [Getting Started](#getting_started)
2. [Variables and simple data types](#variables_and_simple_data_types)
3. [Introducing lists](#introducing_lists)

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
