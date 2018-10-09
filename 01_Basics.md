# Part I - Basics

1. [Getting Started](#getting_started)
2. [Variables and simple data types](#variables_and_simple_data_types)

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
