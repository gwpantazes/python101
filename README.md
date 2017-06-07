# Python 101
Welcome to Python 101, a guided lesson going from absolute beginner to making a simple data crunching program in Python.

We will be learning the basics of Python 3. This lesson will take about 2 hours. We'll cover absolute basics up through file reading. By the end, you’ll be a pro in the fundamentals of Python!

This lesson can be found on Github at <https://github.com/gwpantazes/python101>.

# Table of Contents
- [Overview](#overview)
- [Installing Python](#installing-python)
- [The Command Line](#the-command-line)
- [The Python Interpreter](#the-python-interpreter)
- [Programming Fundamentals](#programming-fundamentals)
  - [Data Types](#data-types)
  - [Expressions](#expressions)
  - [Variables](#variables)
  - [Conditionals](#conditionals)
  - [Loops](#loops)
- [Programming with Python](#programming-with-python)
    - [Reading a CSV File](#reading-a-csv-file)
- [Let's Make Something](#lets-make-something)
- [Where to go from here?](#where-to-go-from-here)
- [Resources, Useful Links, and Sources](#resources-useful-links-and-sources)

# Overview
We'll be learning Python starting from the basics.

0. Please download the lesson materials from the [Python101 Github Repository](https://github.com/gwpantazes/python101).
    - Click on the green "Clone or Download button" to the right side, [or just use this link to download directly](https://github.com/gwpantazes/python101/archive/master.zip)
    - Unpack the zip where you'd like to work. I suggest your `$HOME` directory (we'll get to that soon).
1. First, we'll be learning how to get Python running.
2. Second, we'll learn the fundamentals of the Command Line and the Python Interpreter.
3. Third, we'll get into the basics of programming, general concepts that can be applied to any programming language, and how to work the with Python programming language specifically.
4. Finally, we'll write a program to load and run computations on data.

By the end of the lesson, you should have a firm grasp on how Pyhon can be used to run computations

## Big Picture: Why does Python matter?
As a general programming tool, Python is a simple and useful general scripting language which can accomplish most anything you'd ever like to program.

Python's website says it best:
> Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed. [\[source\]](https://www.python.org/doc/essays/blurb/)

As a bioinformatics tool, Pyhon already has a widge range of free math, scientific libraries for analysis and data processing. These libraries should allow you to:
- Load and work with your own large data files
- Compute complex math
- Process and analyze RNA Sequencing data
- Run machine learning algorithms on your data

See the [Where to go from here?](#where-to-go-from-here) for some inspiration.

### Why should I use Python vs a spreadsheet application like Excel?
Let's address a common question: Why should I use Pyhon? Why wouldn't I just use Excel?

***The answer***: Don't stop using Excel! Pyhon is just a tool. We can use both for their strong points.

Python is a tool that can help solve problems of scale, automation and utility, and other pain points that might come along with large or complex datasets.

> A spreadsheet program will be better for entering new data and exploring existing data, using a mouse as a primary tool to explore and understand the data. Extending this exploration with simple transformations of small data is common.
>
> Python is great for a wide variety of data analysis. If the size of data is repeatably impacting your work, if your questions are getting too complex for a spreadsheet program to reasonable handle, or if there are alot of utility activities being done to handle the data, then Python becomes a useful tool.
> [\[excel vs python\]](https://www.quora.com/When-should-I-use-excel-instead-of-python-for-data-analysis-and-vice-versa)

# Installing Python
1. Go to <https://www.python.org/>
2. Navigate to Downloads: <https://www.python.org/downloads/>
3. Download the latest version of Python 3.
  - Python 3 is also often referred to as Python 3.x, because there are many minor release versions. Python 2.x is an earlier version that is very popular but is being phased out over time. There are a few [key differences and breaking changes](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html) between Python 2 and Python 3.
  - Python 2 is still commonly supported for legacy applications and libraries. Even so, at this point [it's best to start with Python 3](http://www.asmeurer.com/blog/posts/moving-away-from-python-2/), since [almost all libraries support Python 3](http://py3readiness.org/).
4. Run the downloaded Python installer and go through the installation process for your OS.
    - Make sure that if the installer offers to add Python to your `PATH`, you agree. Otherwise, we will have to add the Python installation directory to the `PATH` it manually.
        - What's the `PATH`? The `PATH` environment variable is a list of locations your shell will check when you try to run a command in the command line. See [The Command Line](#the-command-line).

[Using Python3 with Windows, and Installation Instructions](https://docs.python.org/3/using/windows.html)
[Using Python3 with Unix, and Installation Instructions](https://docs.python.org/3/using/unix.html)

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

## Print
The `print()` statement will be your best friend while programming. Just like `echo` in bash, it prints output to the screen for you to see.

Want to debug why your programming isn't working? Go ahead and `print()` the value you're confused by.

***Try it:***
```python
>>> print("Hello world!")
Hello world!
```
Good job! You just wrote a Python interpreted

## Comments (Ignoring code)
If you want to write something into Python and have the intepreter ignore it, put a `#` hash symbol and anything following will not be run. This works both in the intepreter and in scripts.

***Try it:***
```python
>>> # This is a code comment, it won't be run!
>>> # print("This won't print.")
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


## Expressions
Here are some expressions:
```
>>> 1       # A single numeric constant is an expression with the return type of integer
1
>>> 1.0 + 1     # Returns a float
2.0
>>> "This string is an expression, albeit a simple one"
```

## Variables
## Conditionals
## Loops
## Data Structures
In order to compose

### Lists / Array
> A list or sequence is an abstract data type that represents a countable number of ordered values, where the same value may occur more than once. [\[source\]](https://en.wikipedia.org/wiki/List_(abstract_data_type))

Arrays are ordered lists of similar/like elements. In Python, we approximate arrays with Lists.

, while in Python, the built-in List data type is ***mutable***. ***Immutable* means (unchangeable object) is an object whose state cannot be modified after it is created

For example:
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
```

We can access elements of a list by numeric index.


# Programming with Python
A highly recommended overview of how Python works can be found at [Learn Python in Y Minutes](https://learnxinyminutes.com/docs/python3/).

## Python Data Structures
- Lists
- Tuples
- Dictionaries


### Lists
Lists, as described before, are ordered sequences of values.

Python lists can hold anything, even other lists.

***Try it:***
```python
>>> z = ["apple", 42, 3.07, ["nested", "list"], None]
>>> z
['apple', 42, 3.07, ['nested', 'list'], None]
>>> z[-1]       # Note that a return type of None doesn't return anything and thus doesn't print anything
>>> z[-2]           # Access the nested list, which is itself just one element within z
['nested', 'list']
```

### Tuples
Tuples are just like lists, but they are ***immutable*** meaning they are unchangeable after they are created.

A classic example of a tuple is a cartesian point `(x,y)`.
***Try it:***
```python
>>> point = (3,4)   # Tuples denoted by parentheses (although parens are optional)
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
https://pyformat.info/

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

## Reading a CSV File
Comma-Seqarated Value (CSV) files are a common way to store spreadsheet data in a simple text format. Each new line of the file is a spreadsheet row, and columns are *delimited* by commas.

Python offers a standard library for us to consume csv files called `csv`. We can look at each row of a csv file, one at a time, using a csv reader.

[Python CSV Library Documentation](https://docs.python.org/3.6/library/csv.html)

```python
>>> import csv
>>> with open("data/biopsy.csv") as csvfile:
...     reader = csv.reader(csvfile)
...     for row in reader:
...             print(row)
...
['', 'ID', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'class']
['1', '1000025', '5', '1', '1', '1', '2', '1', '3', '1', '1', 'benign']
['2', '1002945', '5', '4', '4', '5', '7', '10', '3', '2', '1', 'benign']
['3', '1015425', '3', '1', '1', '1', '2', '2', '3', '1', '1', 'benign']
... # Output truncated
```

# Let's Make Something
Now that we know how to do lots of cool things, let's use our new skills to program something neat. Let's make a program which reads data from a CSV file and computes values from it.

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
