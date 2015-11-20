Title: Dynamically Building a Class
Date: 2015-07-18 21:49
Tags: python, how-to
Summary: A silly method for dynamically building a Python class at runtime

I recently ran into a situation where a class I was writing was getting a bit hard to manage. The source file was getting so long and I got sick of scrolling back and forth through it to get to the functions I needed. Surely there must be a way to remedy this inconvenient situation!

Packages in Python can help make managing lots of different classes and functionality easier. But I want to split my class' methods out of the same file. Can it be done? Of course it can.

## Setup

Note that this works in both Python 2 and 3. My original class looks like the following.

```
class MyClass:
    def __init__(self):
        self.one = '1'
        self.two = '2'
    def hello(self):
        print('hello')
    def one_func(self):
        print(self.one)
    def two_func(self):
        print(self.two)
```

Stupid, I know. Pretend it is significantly larger. We'll get to a more practical application later.

We want to have the functions broken out into separate files. We will leave the `__init__` function alone because moving that would be silly.

Create a directory with the name of your choice. I will use `funcs`. Then make a file for each of the functions. For ease of remembering which is which I named the files the same as the functions.

```
myclass.py - Our class
funcs/
|__ __init__.py
|__ hello.py
|__ one_func.py
|__ two_func.py
```

Notice the `__init__.py`? That isn't for our class' `__init__` function; it lets Python know that the directory contains a package. Now for the contents of each file.

```
# __init__.py
from .hello import hello
from .one_func import one_func
from .two_func import two_func
```

This sets everything up so we can `from funcs import *` in our `myclass.py` file. The files for each of our functions are just a copy of the function's code in the original file. So for example:

```
# hello.py
def hello(self):
    print('hello')
```

Now that all of our functions are split out into their own files we can finalize our class.

```
from funcs import *

class MyClass:
    def __init__(self):
        self.one = '1'
        self.two = '2'

g = dict(globals())
for e in g:
    if callable(g[e]) and e != 'MyClass':
        setattr(MyClass, e, g[e])
```

This will cycle through all of the callable objects in the global space and add them as attributes of our class. However, notice that we have to specifically ignore our class as we search for our functions to add. If we imported other functions we would have to ignore them as well, or we could do the imports after our functions are added to the class.

```
from funcs import *
from os.path import join

class MyClass:
    def __init__(self):
        self.one = '1'
        self.two = '2'

g = dict(globals())
ignore = ['MyClass', 'join']
for e in g:
    if callable(g[e]) and e not in ignore:
        setattr(MyClass, e, g[e])
```

## Practical Application

Why would you ever want to do this? Say you have a class that may require constant maintenance. Maybe you are adding in new functions or getting rid of deprecated ones. This could help you manage that.

Say your program requires some sort of command interpreter. Python makes this easy with the `cmd` module. Commands for your custom interpreter follow a certain format, being that the function names all start with `do_`. This makes it easier to pick out the right functions to add to our class.

```
# mycmd.py
import cmd
from funcs import *

class MyCmdInterpreter(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

g = dict(globals())
for e in g:
    if callable(g[e]) and e.startswith('do_'):
        setattr(MyCmdInterpreter, e, g[e])

if __name__ == '__main__':
    MyCmdInterpreter().cmdloop()
```

The file structure:

```
mycmd.py
funcs/
|__ __init__.py
|__ do_hello.py
|__ do_something.py
```

```
# __init__.py
from .do_hello import do_hello
from .do_something import do_something
```

```
# do_hello.py
def do_hello(self):
    print('hello!')
```

```
# do_something.py
def do_something(self, line):
    print('doing something with the line')
    print(line)
```

Now when you run `mycmd.py` you will have a command interpreter that knows your two commands: hello and something! This is just one application of a basic but useful idea.
