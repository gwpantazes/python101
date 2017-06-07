# Python 101
Welcome to Python 101, a guided lesson going from absolute beginner to making a simple data crunching program in Python.

We will be learning the basics of Python 3. This lesson will take about 2 hours. We'll cover absolute basics up through CSV file reading. By the end, you’ll be a pro in the fundamentals of Python!

This lesson and its materials can be found on Github at <https://github.com/gwpantazes/python101>.

# Table of Contents
- [Overview](#overview)
- [Setup and Materials](#setup-and-materials)
    - [Installing Python](#installing-python)
- [The Command Line](#the-command-line)
- [The Python Interpreter](#the-python-interpreter)
- [Programming Fundamentals](#programming-fundamentals)
  - [Data Types](#data-types)
  - [Expressions](#expressions)
  - [Variables](#variables)
  - [Conditionals](#conditionals)
  - [Loops](#loops)
  - [Data Structures](#data-structures)
- [Programming with Python](#programming-with-python)
    - [Reading a CSV File](#reading-a-csv-file)
- [Ready to Make Something](#ready-to-make-something)
- [Where to go from here?](#where-to-go-from-here)
- [Resources, Useful Links, and Sources](#resources-useful-links-and-sources)

# Overview
We'll be learning Python starting from the basics.

1. First, we'll be learning how to get Python running.
2. Second, we'll learn the fundamentals of the Command Line and the Python Interpreter.
3. Third, we'll get into the basics of programming and how to program with Python.
4. Finally, we'll write a program to load and run computations on data.

By the end of the lesson, you should feel comfortable running computations on data with Python.

## Big Picture: Why does Python matter?
As a general programming tool, Python is a simple and useful general scripting language which can accomplish most anything you'd ever like to program. The language is like a programming swiss-army knife; it's utility is useful in many diverse situations, and it's great for small programming tasks.

Python's website says it best:
> Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed. [\[source\]](https://www.python.org/doc/essays/blurb/)

As a bioinformatics tool, Python already has a widge range of free math, scientific libraries for analysis and data processing. These libraries should allow you to:
- Load and work with your own large data files
- Compute complex math or run data analysis
- Process and analyze RNA Sequencing data
- Run machine learning algorithms on your data

See the [Where to go from here?](#where-to-go-from-here) for some inspiration.

### Why should I use Python vs a spreadsheet application like Excel?
Let's address a common question: Why should I use Python? Why wouldn't I just use Excel?

***The answer***: Don't stop using Excel! Python is just a tool. We can use both for their strong points.

Python is a tool that can help solve problems of scale, automation and utility, and other pain points that might come along with large or complex datasets.

> A spreadsheet program will be better for entering new data and exploring existing data, using a mouse as a primary tool to explore and understand the data. Extending this exploration with simple transformations of small data is common.
>
> Python is great for a wide variety of data analysis. If the size of data is repeatably impacting your work, if your questions are getting too complex for a spreadsheet program to reasonable handle, or if there are alot of utility activities being done to handle the data, then Python becomes a useful tool.
> [\[excel vs python\]](https://www.quora.com/When-should-I-use-excel-instead-of-python-for-data-analysis-and-vice-versa)

# Setup and Materials
Please download the lesson materials from the [Python101 Github Repository](https://github.com/gwpantazes/python101).
- Click on the green "Clone or Download button" to the right side, [or just use this link to download directly](https://github.com/gwpantazes/python101/archive/master.zip)
    - Unpack the zip where you'd like to work. I suggest your `$HOME` directory (we'll get to that soon).
- Please follow along with README.md, which is also visible from the main project page.

We'll be using a text editor to create files at some point. Some recommendations:
- ***Recommended Text Editor:*** The [Atom text editor](https://atom.io/) is a nice cross-platform text editor for Windows and Mac.
    - Windows users, you should also consider getting [Notepad++](https://notepad-plus-plus.org/) which is an awesome replacement for the existing Windows stock text editor.
    - Mac users, you should consider getting [TextWrangler](https://itunes.apple.com/us/app/textwrangler/id404010395?mt=12) which is an awesome text editor.
        - Mac users should **not** use the TextEdit application, as it saves in rich text which is not a good thing for programming.
- ***Not recommended for beginners:*** Advanced options are `nano`, `emacs`, and `vi` that you can run in the command line.
- There's also the option to use the Python `idle3` shell and its built-in text editor. It works fine, but it's not the best thing you could choose. If you don't want to download any new software or use a command line text editor, this is a fine option.

# Installing Python
1. Go to <https://www.python.org/>
2. Navigate to Downloads: <https://www.python.org/downloads/>
3. Download the latest version of Python 3.
  - Python 3 is also often referred to as Python 3.x, because there are many minor release versions. Python 2.x is an earlier version that is very popular but is being phased out over time. There are a few [key differences and breaking changes](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html) between Python 2 and Python 3.
  - Python 2 is still commonly supported for legacy applications and libraries. Even so, at this point it's best to [use Python 3 when starting new projects which don't rely on legacy code](http://www.asmeurer.com/blog/posts/moving-away-from-python-2/), since [almost all libraries support Python 3](http://py3readiness.org/).
4. Run the downloaded Python installer and go through the installation process for your OS.
    - Make sure that if the installer offers to add Python to your `PATH`, you agree. Otherwise, we will have to add the Python installation directory to the `PATH` manually which will be a pain for a beginner.
        - What's the `PATH`? The `PATH` environment variable is a list of locations your shell will check when you try to run a command in the command line. See [The Command Line](#the-command-line).

In case of trouble, here are additional Installation Instructions:
- [Using Python3 with Windows, and Installation Instructions](https://docs.python.org/3/using/windows.html)
- [Using Python3 with Unix, and Installation Instructions](https://docs.python.org/3/using/unix.html)

# The Command Line
The command line is the window for a programmer to access the heart of a computer.

Typical everyday applications using the mouse and on screen buttons are examples of a GUI (Graphical User Interface).

Instead of a GUI, the Command Line is a CLI (Command Line Interface). We'll be typing commands and hitting the Enter/Return key to send commands to the shell.

Let's open up your command line application:
| Mac | Windows |
| --- | ------- |
| *Terminal* | *PowerShell* if available, otherwise *Command Prompt* |

***Try it:*** Type in the following command into the command line
```shell
echo 'Programming is really cool, wow!'
```
Hit the Enter/Return key on the keyboard to send the command to the shell. You should observe the text being output right back at you.

```shell
george@testers-MacBook-Pro:~$ echo 'Programming is really cool, wow!'
Programming is really cool, wow!
```

Good job! You just ran a shell command very similar to how we'll be running Python scripts.

> **Note**:  We used single quotes, which prevent variable expansion, to let us type the exclamation mark `!` which has special meaning in the shell. Typically we'd want to use double quotes to let us do variable expansion like `echo "${USER}"`.

## Common Commands
Here are some absolutely essential CLI commands we'll be using.
- `echo`: Print/output to the command line
    - ***Try it:***
        ```shell
        george@testers-MacBook-Pro:~$ echo "User: $USER"
        User: george
        george@testers-MacBook-Pro:~$ echo "Home Directory: $HOME"
        Home Directory: /Users/george
        george@testers-MacBook-Pro:~$ echo "PATH variable: $PATH"
        PATH variable: /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/george/Library/Android/sdk/build-tools:/Users/george/Library/Android/sdk/platform-tools:/Users/george/Library/Android/sdk/tools:/usr/local/share/npm/bin/:/Users/george/.rvm/bin:/Library/Frameworks/Python.framework/Versions/3.6/bin
        ```
    - If you haven't unpacked the Python101 materials zip yet, I suggest you extract it in the `$HOME` directory so it looks like: `<Your $HOME Directory Here>/python101`
- `pwd`: "Print Working Directory"
    - Output the current working directory of the shell (where you currently are)
    - ***Try it:***
        ```shell
        george@testers-MacBook-Pro:~$ pwd
        /Users/george
        george@testers-MacBook-Pro:~$ cd python101/
        george@testers-MacBook-Pro:~/python101$ pwd
        /Users/george/python101
        ```
    - Your current working directory will be printed in every one of your command prompts, making `pwd` redundant.
        - Within the prompt, you can find your current directory in between the `:` colon and the `$` dollar sign.
        - The `~` tilde character in your prompt is exactly equivalent to `$HOME`.
        - For example, in this prompt we can see we are in `python101` within the `$HOME` directory: `george@testers-MacBook-Pro:~/python101$`
- `ls`: "List Segments" or more colloquially, just "list"
    - Show contents of a directory. With no arguments, `ls` will output the current working directory's contents.
    - ***Try it:***
        ```shell
        george@testers-MacBook-Pro:~/python101$ ls
        LICENSE    README.md  code/      data/      sandbox/
        george@testers-MacBook-Pro:~/python101$ ls sandbox/
        PEP20.txt     dir1/         dir2/         learnxiny.py  lorem.txt
        ```
- `cd`: "Change Directory"
    - Change the working directory by providing a relative or absolute path.
        - A *relative path* is based off of the current working directory, while an *absolute path* is based off the entire file system from the root of your computer. An example for `subdir1`:
            - Absolute Path: `/Users/george/python101/sandbox/dir1/subdir1`
            - Relative Path: With a working directory of `/Users/george/python101/`, a relative path to `subdir1` would be `sandbox/dir1/subdir1/`

                > **Note:** A trailing slash `/` means an item is definitely a directory, not a file (files cannot have a trailing slash). The trailing slash is optional.

            - In order to go upwards in the directory structure, `..` (two periods) means "*parent directory*".

    - ***Try it:***
        ```shell
        george@testers-MacBook-Pro:~/python101$ cd sandbox
        george@testers-MacBook-Pro:~/python101/sandbox$ ls
        PEP20.txt     dir1/         dir2/         learnxiny.py  lorem.txt
        george@testers-MacBook-Pro:~/python101/sandbox$ ls dir1
        subdir1/ subdir2/
        george@testers-MacBook-Pro:~/python101/sandbox$ cd dir1/subdir1
        george@testers-MacBook-Pro:~/python101/sandbox/dir1/subdir1$ cd ..
        george@testers-MacBook-Pro:~/python101/sandbox/dir1$ cd ../..
        george@testers-MacBook-Pro:~/python101$
        ```
    - Given no argument, `cd` will return to the `$HOME` directory.
    ***Try it:***
        ```shell
        george@testers-MacBook-Pro:~/python101$ cd
        george@testers-MacBook-Pro:~$
        ```
- `cat`: Short for "Concatenate"
    - View contents of a file, create single or multiple files, concatenate files, and redirect output in terminal or files
    - In practice, used for output to the screen, such as printing a whole file. `echo` doesn't print the contents of files, so instead we use `cat` for file output.
    - ***Try it:***
        ```shell
        george@testers-MacBook-Pro:~/python101/sandbox$ ls
        PEP20.txt     dir1/         dir2/         learnxiny.py  lorem.txt
        george@testers-MacBook-Pro:~/python101/sandbox$ cat PEP20.txt
        The Zen of Python

        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!
        ```

    - `head` and `tail` commands print out files just like cat, but only output the first few lines or the last few lines respectively.

- `man`: "Manual"
    - Show manual documentation for the command given as an argument.
    - ***To exit:*** Once in the manual, press `q` to exit the manual.
    - ***Try it:***
        ```shell
        george@testers-MacBook-Pro:~$ man echo
        ECHO(1)                   BSD General Commands Manual                  ECHO(1)

        NAME
             echo -- write arguments to the standard output

        SYNOPSIS
             echo [-n] [string ...]

        DESCRIPTION
             The echo utility writes any specified operands, separated by single blank (` ') char-
             acters and followed by a newline (`\n') character, to the standard output.
         ...
        ```
    - Sometimes there's no man page. The command may have it's own `-h` or `--help` flag. Or you may have to Google for the documentation.

- Extra credit for the curious:
    - `env`: Display all environment variables
    - `compgen`: Can display available commands.
        - This is an example of a command without a `man` page, so look up the documentation for this on Google!
    - Searching Google for the answer is an essential tool.

# The Python Interpreter
Let's start using Python! Python can either interpret new commands one the fly or run scripts you've already written.
  - Writing commands on the fly in the interpreter is great for experimentation and prototyping new ideas.
  - Running pre-written scripts is much faster and easier to run the same script again and again. You don't have to type in the same thing twice!

Let's start with writing some commands on the fly with the Python Intepreter, which from now on we'll just call "the interpreter". After, let's write and run some scripts from Python script files.

## Starting the Interpreter
Starting the interpreter in your command line shell depends on which OS (operating system) you are using (Unix vs Windows).

> **Note:** Mac OS computers are Unix compliant. Windows 10 64-bit machines are just beginning to support Unix compliance in developer mode without relying on emulation. And of course, any flavor of Linux OS is *Unix-like* (practically 100% Unix compliant).

We'll start the interpreter in the shell, which depends on which operating system you're on.

In your command line, enter based on your Operating System:

| Unix      | Windows |
|-----------|---------|
| `python3` | `py -3` |

> **NOTE:** Unix names Python3 differently than Python2 in order to differentiate the versions. On its own, Python2 would simply be named `python` in the command line.
>
> Windows does something a little funnier: when you isntall Python 3 first, and Python2 second, Python3 installed the `py` helper script

When the Python interpreter boots up, it should output some starting information for you. See the following Unix and Windows examples for what to expect.

***Unix (Mac Terminal, `BASH` Shell)***
```shell
george@testers-MacBook-Pro:~/python101$ python
Python 2.7.12 (default, Aug  5 2016, 10:48:32)
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
george@testers-MacBook-Pro:~/python101$ python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
***Windows (Command Prompt)***
```shell
Windows PowerShell
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

PS C:\Users\George> py
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
PS C:\Users\George> # Notice that it defaulted to python 2 if you have both installed. Oops! Let's do Python 3 instead.
PS C:\Users\George> py -3
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

***How do I exit the interpreter?***
If you're in the interpreter and you want to get out, use the Python `quit()` function and hit enter.
```shell
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
george@testers-MacBook-Pro:~/python101$
```
Alternatively, you can close the entire shell application window. Since it might be impractical to close the whole shell, it's better practice to just close the interpreter running *inside* the shell.

## IDLE Python Shell
By running `idle3` in the command line, a hybrid GUI/CLI Python shell application will start called *IDLE*. This *IDLE* shell is largely the same as writing commands to the python interpreter in the command line, but has a few convenient things.

It's your choice to use the command line or *IDLE* when running the interpreter. You can also take advantage of IDLE's text editor to write simple scripts. Be careful to save your scripts properly though, when working in IDLE.

## Print
The `print()` statement will be your best friend while programming. Just like `echo` in bash, it prints output to the screen for you to see.

Want to debug why your programming isn't working? Go ahead and `print()` the value you're confused by.

***Try it:***
```python
>>> print("Hello world!")
Hello world!
```
Good job! You just wrote a Python interpreted command, composed of the print function and a string constant. The print command returned nothing, but output the string to the screen.

Lots of good things are happening! Let's continue!

## Comments (Ignoring code)
If you want to write something into Python and have the intepreter ignore it, put a `#` hash symbol and anything following will not be run. This works both in the intepreter and in scripts.

***Try it:***
```python
>>> # This is a code comment, it won't be run!
... # print("This won't print.")
...
>>>
```

It's very useful and highly recommended to leave comments for yourself as you are coding script files! Writing comments for what you plan to do in "plain language" (not code) is extremely helpful to structure your code; this abstraction is called *Pseudocode*. Write commented pseudocode to plan your program, and leave "plain language" documentation for the long term.

Also, leaving helpful reminders explaining why you are doing something can save you time when you read through your code in a few months!

```python
""" Multiline strings can be written
    using three "s, and are often used
    as documentation.
"""
```

This lesson will make use of comments to explain what code is doing.

## The Interpreter as a Calculator
Let's try a few different things we can do with the Interpreter, which can easily act as a calculator.

***Try it:***
```python
>>> 1 + 1       # Simple addition
2
>>> 8 - 1       # Simple subtraction
7
>>> 5 - 14      # Negative numbers are no problem
-9
>>> 10 * 2      # Simple multiplication
20
>>> 35 / 5      # Simple division. Notice the result is a floating point number, not a whole integer. Normal division always returns a float.
7.0
>>> 22 / 7      # Let's divide something a bit more complicated
3.142857142857143
>>> 8/0         # Oops. Dividing by zero throws an error.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 9 * .2      # Multiply by a float, get a float.
1.8
>>> 1 * 1.0     # Really, I wasn't kidding.
1.0
>>> 5 + 3 * 6       # PEMDAS Order of operations means multiplication comes first
23
>>> (5 + 3) * 6     # But Parentheses enforce precedence, just like in PEMDAS
48
>>> 5 // 3      # Integer division truncates to whole digits, discarding the remainder
1
>>> 5.0 // 3.0  # Works for floats too
1.0
>>> -5 // 3     # Works for negatives too. Increased
-2
>>> 7 % 3       # The Modulus operator only returns the remainder
1
```
Python can do fancier math expressions as well, such as powers, logs, square roots, etc. Most complex functions require importing standard or new libraries, since Python only has a few key functions built in.

***Try it:***
```python
>>> 2**3      # Exponents are built-in and don't need a library
8
>>> import math     # Import the math standard library that comes with Python
>>> math.sqrt(100)  # Square Root is found in the math library
10.0
>>> math.log(9)     # Log defaults to base e
2.1972245773362196
>>> math.log(9, 3)  # By looking in the docs, we find out we can change the base easily by adding another parameter
2.0
>>> piVariable = math.pi    # Store the result in a variable
>>> print(piVariable * 3 + 5 / 2)   # Expressions can be used as arguments
```

## Running Python Scripts
Let's run Python code from scripts.

1. `quit()` the interpreter to return to the command line.
2. Using your respective python command ()`python3` or `py -3`, whichever you used to start the interpreter), let's call a script file.
3. Now lets run some scripts found in the `code` directory of the downloaded Python 101 materials.

```shell
george@testers-MacBook-Pro:~/python101$ python3 code/00_hello_world.py
Hello World!
george@testers-MacBook-Pro:~/python101$ python3 code/01_greetings.py
Hello! What is your name? George
Hello George
george@testers-MacBook-Pro:~/python101$ python3 code/02_questions.py
What is your name? George
What is your age? 25
George is 25 years old.
```

Awesome! We are now running python scripts like pros.

# Programming Fundamentals
Let's cover a few general programming concepts. These are fundamental building blocks that allow us to build any program.

- Data Types
- Expressions
- Variables
- Conditionals
- Loops

## Data Types
Python has a few built-in primitive data types you can use out of the box. These types fall into categories of numeric types, sequences, sets, and mappings.
- `boolean`
    - A boolean is a `True` or `False` value. These are extremely important for computers to decide what to do. Some examples of booleans:
        - The primitive values `True` and `False`. Note the capitalization.
        - Comparison operators produce booleans
            - `3 > 1` returns `True` because 3 is greater than 1.
            - `7 >= 11` returns `False` because 7 is not greater than or equal to 11.
                - But `7 <= 11` returns `True` because 7 is less than or equal to 11.
            - `1 == 0` returns `False` because 3 is not equivalent to 1.
                - But check this out: both `1 == 1` and `1 == 1.0` return `True` because the numeric value of 1 is equivalent.
            - `1 != 0` returns `True` because 1 is not equivalent to zero.
        - The `not` keyword inverts a boolean:
            - `not True` returns `False`
            - `not False` returns `True`
            - `not 1 == 0` returns `True` (works with expressions)
- `string` values are sequences of characters. Some examples:
    - `"apple"`
    - `'m'`
    - `"Toccata" + 'and' + "Fugue" + 'in D Minor'`
- Numeric Types
    - `int` type numbers are whole integers. In Python3 these can be as long as you like.
        - If you convert to an int, the fractional part of the number gets be truncated away
        - ***Try it:*** Convert to an int
            ```python
            >>> int("5")    # Strings can be converted no problem
            5
            >>> int(7.8)    # Floats get truncated
            7
            >>> int(-4)      # You can redundantly cast an int to an int, since -4 is still an int regardless of negative
            -4
            >>> int('a')    # But anything that is not a number will throw a value error
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            ValueError: invalid literal for int() with base 10: 'a'
            ```
    - `float` type numbers have decimal parts and can grow very large or very small due to being based on scientific notation (uses exponents to achieve )
        - `0.0`, `1.0`, `-1.0` are all floats even if they are equivalent to their respective whole ints
- The `list` type looks like a sequence surrounded by `[]` square brackets. Examples of lists:
    - `[1,2,3,4]`
        - The same list built with the `range` keyword: `range(1, 5)`
    - Lists can be composed of any objects: `["string", int("8"), 3.1415926535, ["inner", "list"]]`
    - Strings are ***not*** lists by themselves: `"Strings are a sequence of characters and behave a lot like a list sometimes, but are not a list."`
    - We'll cover lists in more detail in a few sections. See [Lists / Arrays](#lists-arrays)
- The `dictionary` is composed of ***unordered*** key-value pairs. Values are accessed via their key. Anything can be a value, and anything can be a key.
    - The key is used with the `[]` square bracket access operator, and can ***get*** or ***set*** the value.
    - ***Try it:***
        ```python
        >>> dict = {}       # We can initialize an empty dictionary
        >>> dict["anything here?"]  # But checking for something that isn't there will throw a KeyError
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        KeyError: 'anything here?'
        >>> # Let's add it in so we can find it
        ... dict["anything here?"] = "Yep! Something is here!"
        >>> dict["anything here?"] # We've found it!
        'Yep! Something is here!'
        >>> dict = {'jack': 4098, 'jill': 1043} # Overwrite the whole dictionary
        >>> dict["anything here?"]  # Nope, not anymore...
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        KeyError: 'anything here?'
        >>> dict['jack']    # But we can find Jack
        4098
        >>> 'jill' in dict  # And check whether Jill is present
        True
        >>> del dict['jill']    # Delete Jill
        >>> 'jill' in dict  # And she can no longer be found
        False
        ```
    - A `set` is an unordered collection with no duplicate elements. In practice it behaves
        - ***Try it:***
            ```python
            >>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
            >>> print(basket)   # duplicates have been removed
            {'orange', 'banana', 'pear', 'apple'}
            >>> 'orange' in basket  # check membership
            True
            >>> 'crabgrass' in basket
            False
            ```
- There are other types of objects, but they are beyond the scope of this lesson.


## Expressions
Expressions are just composites of everything we learned so far. Expressions are single values, functions, or any group of values, operators, and functions that represent a complete thought and give one return value.

This is an important idea because often, instead of just putting one item in a `print()`, for example, we can put expressions computing whatever we like as the argument.
```python
>>> import math
>>> print("Twenty" + 'two' + "7" * 3, math.log(3), "And 2 formatted {}s to cap it off".format(type(str(1))))
Twentytwo777 1.0986122886681098 And 2 formatted <class 'str'>s to cap it off
```

Here are some examples of expressions:
```python
>>> 1       # A single numeric constant is an expression with the return type of integer
1
>>> 1.0 + 1     # Returns a float
2.0
>>> "This string is an expression, albeit a simple one consisting of only a single primitive value"
'This string is an expression, albeit a simple one consisting of only a single primitive value'
>>> type(print("print() is a function which returns nothing."))
print() is a function which returns nothing.
<class 'NoneType'>
```

## Variables
We can store the return value of any expression into a variable.

***Try it:***
```python
>>> x = 7   # Store something using '=' equals operator
>>> x       # Access something
7
```

You can name a variable whatever you like as long as it follows these rules:
1. Variables names must start with a letter or an underscore, such as:
    - `_underscore`
    - `underscore_`
2. The remainder of your variable name may consist of letters, numbers and underscores.
    - `password1`
    - `n00b`
    - `un_der_scores`
3. Names are case sensitive.
    - `case_sensitive`, `CASE_SENSITIVE`, and `Case_Sensitive` are each a different variable.

> Variable naming rules [\[source\]](https://thehelloworldprogram.com/python/python-variable-assignment-statements-rules-conventions-naming/) tutorial

```python
>>> Guido       # Accessing a variable that has not been made throws an error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Guido' is not defined
>>> Guido = ""
>>> Guido = False
>>> Guido = 1
>>> 0 = Guido               # Wrong way, variable always on the left side
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> '' = Guido              # You can't assign values to strings
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> False = Guido           # Nor can you override reserved words
  File "<stdin>", line 1
SyntaxError: can't assign to keyword
>>> Guido           # But the value of the variable is maintained
1
```

## Conditionals
`if`, `elif`, and `else` statements control the flow of a program using boolean conditions.
- They are evaluated sequentially from the top down. If a boolean condition is evaluated as `True`, the block under that `if`/`elif` will run.
- If an `if` or `elif` conditional expression is found to be true `True` and the code in that block runs, no following conditions will be tested.
- If no `if` or `elif` are `True`, then the `else` block code will run.
- `else` always comes last and doesn't take an expression, since if the code reaches that position the else block is guaranteed to run.
- `elif` and `else` are both optional.

***Try it:***
```python
>>> x = 42
>>> if x < 0:       # 42 isn't less than zero...
...     x = 0       # So anything in here doesn't run
...     print('Negative changed to zero')
... elif x == 0:    # 42 isn't zero...
...     print('Zero')
... elif x == 1:    # 42 isn't 1...
...     print('Single')
... else:           # By reaching the else block, it will run!
...     print('More')   # And we print "More"!
...
More
>>> # Let's do another if statement with a different value
>>> x = 0
>>> if x < 0:       # 0 isn't less than zero...
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:    # 0 matches! Success
...     print('Zero')   # Run this code block!!!
... elif x == 1:    # We don't even bother checking if x is 1
...     print('Single')     # So of course this doesn't run
...                     # We don't need an else block!
Zero
>>> if True:                # Simplest possible if
...     print("Victory")
...
Victory
```

## Loops

While loops test a boolean condition and run whatever is inside the loop block if the condition is true.
***Try it:***
```python
>> # Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1             # One-line assignment with commas
>>> while b < 10:
...     print(b)
...     a, b = b, a + b     # One-line assignment with commas again
...
1
1
2
3
5
8
```

For loops iterate over finite sequences of things, and can also conveniently declare a loop block variable.

***Try it:***
```python
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:     # in keyword lets us extract a single value at a time
...     print(w, len(w))    # len() is a built-in function which returns the length of a sequence (string, list, etc)
...
cat 3
window 6
defenestrate 12
>>> # And now let's loop over a range. This is a very typical for loop idiom.
... range(0,10)
range(0, 10)
>>> for i in range(0,10):
...     print("Loop", i)
...
Loop 0
Loop 1
Loop 2
Loop 3
Loop 4
Loop 5
Loop 6
Loop 7
Loop 8
Loop 9
```

## Data Structures
In order to compose cool programs and complex objects, we'll need to cover useful data structures. The main data structure we'll focus on is the `list` data type.

### Lists / Arrays
> A list or sequence is an abstract data type that represents a countable number of ordered values, where the same value may occur more than once. [\[source\]](https://en.wikipedia.org/wiki/List_(abstract_data_type))

We've already discussed lists, so what about Arrays?
Arrays are ordered lists of similar/like elements. In Python, we typically treat lists and arrays like they are the same thing (though it's more correct to always call it a list, *especially* if there are different types of elements or it is being dynamically resized).

***Try it:***
```python
>>> a = [1,2,3,4,5,6,7,8]   # Make our list
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a[0]    # Python uses zero based indices. Index 0 is the "first" element.
1
>>> a[7]    # Because of the zero base, the final index = size of list - 1
8
>>> a[8]    # If we try to access the element at [size of list], we get an out of range error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> a[-1]   # But we can count from the end using negative indices
8
>>> a[-2]   # And the second to last
7
>>> a[-0]   # Negative zero is just zero. No surprises here...
1
```

We can access elements of a list by numeric index. We can also iterate over lists very easily:

***Try it:***
```python
>>> a = [1,2,3,4,5,6,7,8]
>>> for num in a:      # in keyword lets us extract a single value from the list at a time
...     print(num)
...
1
2
3
4
5
6
7
8

```


# Programming with Python
Now that we've learned the basics, let's get to doing thingsA highly recommended overview of how Python works can be found at [Learn Python in Y Minutes](https://learnxinyminutes.com/docs/python3/).

## Data Structures
Time to go a bit more in depth on these Python data structures.

### Lists
Lists, as described before, are ordered sequences of values.

Python lists can hold anything, even other lists. Lists can add, remove, and change elements.

***Try it:***
```python
>>> z = ["apple", 42, 3.07, ["nested", "list"], None]
>>> z
['apple', 42, 3.07, ['nested', 'list'], None]
>>> z[-1]       # Note that a return type of None doesn't return anything and thus doesn't print anything
>>> z[-2]           # Access the nested list, which is itself just one element within z
['nested', 'list']
>>> z[2] = 999      # Let's change the 3rd element
>>> z.append("NEW") # Add a new element to the end
>>> del z[0]        # And delete the first element
>>> z           # The list has been changed!
[42, 999, ['nested', 'list'], None, 'NEW']
```

### Tuples
Tuples are just like lists, but they are ***immutable*** meaning they are unchangeable after they are created. Lists remain ***mutable*** after creation, meaning we can add, remove, or change elements. Because tuples are ***immutable***, we cannot make any of these modifications to an existing tuple. What we can do is compose a new one on the fly, though...

A classic example of a tuple is a cartesian point `(x,y)`.
***Try it:***
```python
>>> point = (3,4)   # Tuples stylistically denoted by parentheses (although parentheses are actually optional)
>>> point[0]        # Accessing element
3
>>> point[2]        # Same types of range mistakes can be made, same as lists
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> point[0], point[1]
(3, 4)
>>> point[0], point[1], 7.45, "apple"   # Form tuples on the fly by using commas
(3, 4, 7.45, "apple")
```

#### List Manipulation (Slicing)
Python has built in list slicing, adding a `:` colon operator in the existing list access `[]` square bracket operator.

```python
a[start:end] # get a list of the items from start through end-1
a[start:]    # get a list of the items from start through the rest of the array
a[:end]      # get a list of the items from the beginning through end-1
a[:]         # a copy of the whole array
```
There is also the step value (default step is `1`), which can be appended and used with any of the above slices:
```python
a[start:end:step] # start through end - 1, by step
```
The key point to remember is that the `:end` value represents the first value that is not in the selected slice. So, the difference beween `end` and `start` is the number of elements selected (if step is 1, the default).

If `start` or `end` are a negative number, it means it counts from the end of the array instead of the beginning. So:
```python
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
```

***Try it:***
```python
>>> a = [1,2,3,4,5,6,7,8]   # Make our list
>>> a[1:4]                  # Select the 2nd element through the 3rd. Inclusive start, exclusive end.
[2, 3, 4]
>>> a[::-1]                 # Reverse the list by choosing the whole array, with a step of -1
[8, 7, 6, 5, 4, 3, 2, 1]
>>> a[:-1]              # Common mistake: What if we tried to reverse an array like this? Doesn't work... This selects from the array beginning to 1 from the end
[1, 2, 3, 4, 5, 6, 7]
>>> a[4:1]              # So what if we want a slice that is also reversed? This doesn't work...
[]
>>> a[1:4:-1]           # What about specifying a -1 step? Nope...
[]
>>> a[4:1:-1]           # Now we've got it! Set the -1 step, and start high to end low in order to match the step.
[5, 4, 3]
```
List slicing and manipulation is a powerful feature of Python which we can take advantage of when processing data columns.

> Explanation and examples of list slicing came from [this amazing StackOverflow answer on Python list slicing](https://stackoverflow.com/a/509295/2291928)

## String formatting
String formatting is pretty nice in Python. [See this Python string format tutorial for a tour.](https://pyformat.info/)

The `.format()` method is called directly on a string, with its arguments *interpolated* into the format string. That sounds scary, but really it just means that items are inserted straight into the string where you want them, at the `{}` format string

Let's quickly play around with it.

***Try it:***
```python
>>> x = 7
>>> y = 2.5
>>> fruit = "apple"
>>> # The default format string behavior inserts by ordered position
... "This is a formatted string. x: {}, y: {}, My favorite food: {}".format(x, y, fruit)    # Format will return a new string with the values interpolated
'This is a formatted string. x: 7, y: 2.5, My favorite food: apple'
>>> "{a}, {fav}, {b}".format(a=x, b=y, fav=fruit)   # We can use named format specifiers
'7, apple, 2.5'
>>> "{1}, {0}, {fav}".format(x, y, fav=fruit)   # We can use position indices as well
'2.5, 7, apple'
>>> "{2}, {1}, {fav}".format(x, y, fav=fruit)   # Don't forget that positional indices are zero based
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
```

## Reading from a file
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
```python
>>> with open("data/biopsy.csv") as datafile:
...     datafile.read()
...
'"","ID","V1","V2","V3","V4","V5","V6","V7","V8","V9","class"\n"1","1000025",5,1,1,1,2,1,3,1,1,"benign"\n"2","1002945",5,4,4,5,7,10,3,2,1,"benign"\n
... # Output truncated
```

Reading the file like that. Let's just do one line at a time.
```python
>>> with open("data/biopsy.csv") as datafile:
...     for i in range(4):
...             datafile.readline()
...
'"","ID","V1","V2","V3","V4","V5","V6","V7","V8","V9","class"\n'
'"1","1000025",5,1,1,1,2,1,3,1,1,"benign"\n'
'"2","1002945",5,4,4,5,7,10,3,2,1,"benign"\n'
'"3","1015425",3,1,1,1,2,2,3,1,1,"benign"\n'
```
Notice that the newline character `\n` is kept in each line. Python detects that character as the end of a line, but leaves it for you to strip off yourself.

If we wanted to parse through this kind of output, we can use Python functions `split`, `strip`, and convert any values we need to the proper types.

Let's just work with a single row's data to make it simple for ourselves. We will plug the logic into a script after we tinker.
```python
>>> # Let's work with the header row. Let's convert this messy string into a nice array.
... row = '"","ID","V1","V2","V3","V4","V5","V6","V7","V8","V9","class"\n'
>>> row.strip()         # strip removes whitespace from the beginning and end by default, although you can specify other characters
'"","ID","V1","V2","V3","V4","V5","V6","V7","V8","V9","class"'
>>> row                 # strip doesn't modify the existing string in place
'"","ID","V1","V2","V3","V4","V5","V6","V7","V8","V9","class"\n'
>>> # Most string operations return a new string, and don't modify the current string
... row = row.strip()   # So let's make sure to store the result
>>> row                 # Now the strip result is actually stored
'"","ID","V1","V2","V3","V4","V5","V6","V7","V8","V9","class"'
>>> rowArray = a.split(',') # Split delimits an array from a string. We're splitting on the comma character
>>> rowArray            # We now have an array of strings
['""', '"ID"', '"V1"', '"V2"', '"V3"', '"V4"', '"V5"', '"V6"', '"V7"', '"V8"', '"V9"', '"class"']
>>> for col in rowArray:        # col is a local variable for just this for loop, a copy.
...     col = col.strip("\"")   # When we modify col, nothing happens to the original
...
>>> rowArray                    # Nothing changed. So how do we modify our array?
['""', '"ID"', '"V1"', '"V2"', '"V3"', '"V4"', '"V5"', '"V6"', '"V7"', '"V8"', '"V9"', '"class"']
>>> for i in range(0, len(b)):
...     b[i] = b[i].strip("\"")
...
>>> b       # Now the header row looks ready to work with
['', 'ID', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'class']
```

Now that we've cleaned up the header row, let's look at a data row:

```python
>>> row = '"1","1000025",5,1,1,1,2,1,3,1,1,"benign"\n'  # Our sample data row
>>> row = row.strip().split(',')    # Let's strip and split the array in one line
>>> row                             # We still need to clean up those extra quotes
['"1"', '"1000025"', '5', '1', '1', '1', '2', '1', '3', '1', '1', '"benign"']
>>> for i in range(0, len(row)):    # So iterate through row indices
...     row[i] = row[i].strip("\"") # to strip quotes and store the result in place
...
>>> row
['1', '1000025', '5', '1', '1', '1', '2', '1', '3', '1', '1', 'benign']
>>> for item in row:            # Let's check out our data
...     print(item, type(item))
...
1 <class 'str'>
1000025 <class 'str'>
5 <class 'str'>
1 <class 'str'>
1 <class 'str'>
1 <class 'str'>
2 <class 'str'>
1 <class 'str'>
3 <class 'str'>
1 <class 'str'>
1 <class 'str'>
benign <class 'str'>
>>> for i in range(0, len(row)):
...     row[i] = row[i].strip("\"")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'list' object has no attribute 'strip'
>>> row
['"1"', '"1000025"', '5', '1', '1', '1', '2', '1', '3', '1', '1', '"benign"']
>>> for i in range(0, len(row)):
...     row[i] = row[i].strip("\"")
... row
  File "<stdin>", line 3
    row
      ^
SyntaxError: invalid syntax
>>> for i in range(0, len(row)):
...     row[i] = row[i].strip("\"")
...
>>> row
['1', '1000025', '5', '1', '1', '1', '2', '1', '3', '1', '1', 'benign']
>>> int(row[-1])    # If you try to convert things that aren't numbers to numbers, you'll get an error!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'benign'
>>> try:    # Luckily we can catch and deal with stuff like this
...     value = int(row[-1])    # Try to store the result
... except ValueError:  # If we encounter a ValueError
...     print("ERROR. Not cool. Not cool at all.")  # Do whatever you like here instead, such as printing an message
...
ERROR. Not cool. Not cool at all.
>>>
```

As you can see, it takes a bit of work to clean up data from a csv file "by hand".

Maybe we can make this into a Python script so we don't have to run this in the interpreter?

```python
data = []
with open("data/biopsy.csv") as datafile:
    for row in datafile:
        rowArray = row.strip().split(',')
        for i in range(0, len(rowArray)):
            if(rowArray[i])
            rowArray[i] = rowArray[i].strip('"')
        # Now we have a single row cleaned and ready
        data.append(rowArray)
print(data)
```
This should be a good start...
See `code/10_readfile.py` for a working script solution for reading a file and parsing through values.

## Reading a CSV File
Comma-Seqarated Value (CSV) files are a common way to store spreadsheet data in a simple text format. Each new line of the file is a spreadsheet row, and columns are *delimited* by commas.

Python offers a standard library for us to consume csv files called `csv`. We can look at each row of a csv file, one at a time, using a csv reader. This is just a convenience class on top of the file reader we used before.

[Python CSV Library Documentation](https://docs.python.org/3.6/library/csv.html)

***Try it:***
```python
>>> import csv                              # Use the CSV standard library
>>> with open("data/biopsy.csv") as csvfile:# Lets open the csv file safely by using a with block, relatively from the root of the lesson
...     reader = csv.reader(csvfile)        # Read from the csvfile
...     for row in reader:                  # Iterate through each row
...             print(row)
...
['', 'ID', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'class']
['1', '1000025', '5', '1', '1', '1', '2', '1', '3', '1', '1', 'benign']
['2', '1002945', '5', '4', '4', '5', '7', '10', '3', '2', '1', 'benign']
['3', '1015425', '3', '1', '1', '1', '2', '2', '3', '1', '1', 'benign']
... # Output truncated
```

See `code/11_read_csv.py` for a working script solution for reading through a csv file and parsing its values.

# Ready to Make Something
Now that we know how to do lots of cool things in Python, let's use our new skills to program something neat. Let's make a program which reads data from a CSV file and computes values from it.

Refer to `code/20_average_biopsy_bugged.py` for the beginnings of something cool. But wait! This program has a bug! Oh no! We'll have to track it down and fix it.
Solution can be found in `code/21_average_biopsy.py`.

# Where to Go From Here?
Python has extensive libraries for Scientific Analysis and Computation.
- [NumPy](http://www.numpy.org/)
    - NumPy is the fundamental package for scientific computing with Python.
    - Useful things:
        - N-dimensional array object (matrix)
        - useful linear algebra, Fourier transform, and random number capabilities
- [SciPy](https://www.scipy.org/)
    - Python-based ecosystem of open-source software for mathematics, science, and engineering.
    - Includes NumPy!
- RNA Sequencing Analysis: [READemption](https://github.com/konrad/READemption): a pipeline for the computational evaluation of RNA-Seq data
    - Disclaimer: I'm not familiar with this tool, and there are other tools which can be run straight from the shell which you can feed data prepared with Python.
- [Keras](https://keras.io/): Deep Learning library for Theano and TensorFlow
- [PyGame](www.pygame.org): Python game engine.
    - Useful for more than just games, PyGame can be used to visualize simulations.
- [PyPi](https://pypi.python.org/pypi): The Python Package Index
    - The Python Package Index is a repository of software for the Python programming language. Find a package you'd like to use in your program!

Some Python distributions with all the goodies:
- [Anaconda](https://www.continuum.io/downloads) data science platform
    - Includes NumPy, SciPy, and more
- [Python(x,y)](http://python-xy.github.io/): A Scientific Python Distribution

# Resources, Useful Links, and Sources
- [Main Python Documentation](https://docs.python.org/3/)
- [Python Tutorials](https://www.learnpython.org/)
- [Learn Python the Hard Way](https://learnpythonthehardway.org/book/ex1.html): Good tutorial to thoroughly learn Python from the beginning.
- [Learn Python in Y Minutes](https://learnxinyminutes.com/docs/python/): 10 Minute Overview of Python
- [Hitchhikder's Python Style Guide](http://python-guide-pt-br.readthedocs.io/en/latest/writing/style/)
- [Popular Python Packages](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/)
- [Python Tutorial for Science from NYU](http://www.physics.nyu.edu/pine/pymanual/html/pymanMaster.html)
- [Python Crash Course for Scientists](http://nbviewer.jupyter.org/gist/anonymous/5924718)
- [Sample Datasets](https://vincentarelbundock.github.io/Rdatasets/datasets.html)
- [Python String Formatting](https://pyformat.info/)
