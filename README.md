# Python 101 (for scientists)
Welcome to Python 101 (for scientists), a guided lesson going from absolute beginner to making a simple data crunching program in Python.

We will be learning the basics of Python 3. This lesson will take about 2 hours. We'll cover absolute basics up through file reading. By the end, you’ll be a pro in the fundamentals of Python!

# Table of Contents
- [Overview](#overview)
    - [Big Picture: Why does Python matter?](#big-picture)
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

# The Command Line
The command line is the window for a programmer to access the heart of a computer.

Typical everyday applications using the mouse and on screen buttons are examples of a GUI (Graphical User Interface).

Instead of a GUI, the Command Line is a CLI (Command Line Interface). We'll be typing commands and hitting the Enter/Return key to send commands to the shell.

***Try it:*** Type in the following command into the command line
```shell
echo "Programming is really cool, wow!"
```
Hit the Enter/Return key on the keyboard to send the command to the shell. You should observe the text being output right back at you.

Good job! You just ran a shell command very similar to how we'll be running Python scripts.

## Common Commands
Here are some absolutely essential CLI commands we'll be using.
- `echo`: Print to the command line
    - Try it:
        ```shell
        george@testers-MBP:~$ echo "Home Directory: $HOME"
        Home Directory: /Users/george
        ```
    - Try another:
        ```shell
        george@testers-MacBook-Pro:~$ echo "PATH variable: $PATH"
        PATH variable: /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/george/Library/Android/sdk/build-tools:/Users/george/Library/Android/sdk/platform-tools:/Users/george/Library/Android/sdk/tools:/usr/local/share/npm/bin/:/Users/george/.rvm/bin:/Library/Frameworks/Python.framework/Versions/3.6/bin
        ```
- `man`: "Manual"
    - Shows manual documentation for the command given as an argument.
    - Try it:
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
        - ***To exit*** Press `q` to exit the manual.
    - Sometimes there's no man page. Check if the program has it's own `-h` or `--help` flag.
### Getting Around
- `pwd`: "Print Working Directory"
    - Outputs where you currently are
    - Try it:
        ```shell
        george@testers-MBP:~/python101/command_line$ pwd
        /Users/george/python101/command_line
        ```
- `ls`: "List Segments" or more colloquially, just "list"
    - Shows contents of the current directory or given directory as argument
    - Try it:
        ```shell
        george@testers-MBP:~/python101/command_line$ ls
        dir1/      dir2/      file1.txt  file2.txt  file3.txt
        ```
- `cd`: "Change Directory"
    - Given no arguments, return to `$HOME`
    - Given an absolute or relative directory, go to that directory
    - Try it:
        ```shell
        george@testers-MBP:~/python101/command_line$ cd dir1
        george@testers-MBP:~/python101/command_line/dir1$ ls
        subdir1/ subdir2/
        ```
    - Let's return to the home directory by providing no argument:
        ```shell
        george@testers-MBP:~/python101/command_line/dir1$ pwd
        /Users/george/python101/command_line/dir1
        george@testers-MBP:~/python101/command_line/dir1$ cd
        george@testers-MBP:~$ pwd
        /Users/george
        george@testers-MBP:~$
        ```

- Extra credit for the curious:
    - `env`: Display all environment variables
    - `compgen`: Can display available commands. See `help`.
    - And of course, Google it if you don't know!

# The Python Interpreter
Let's boot up python! Python can either interpret new commands one the fly or run scripts you've already written.
  - Writing commands on the fly in the interpreter is great for experimentation and prototyping new stuff.
  - Running pre-written scripts is much faster and easier to re-run the same funcionality. You don't have to type in the same thing twice!

Let's start with writing some commands on the fly with the Pyhon Intepreter, which from now on we'll just call "the interpreter".

## Starting the Interpreter
We'll start the interpreter in *the shell*, which depends on which operating system you're on.

In your command line enter `python3` if you're Unix, or `py` if you're Windows.
When the Python interpreter boots up, it should output some starting information for you. See the following Unix and Windows examples for what to expect.

### Unix (Mac Terminal, `BASH` Shell)
```shell
george@testers-MBP:~$ python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
### Windows (Command Prompt)
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




## How do I exit the interpreter?
If you're in the interpreter and you want to get out, use the Python `quit()` function and hit enter.
```Python
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
george@testers-MacBook-Pro:~/python101$
```
Alternatively, you can close the entire terminal window, but that is closing the entire shell, not just the interpreter running *inside* the shell.

## Print
The `print()` statement will be your best friend while programming.
Do you want to show the user some output? `print()` it.
Want to debug why your programming isn't working? Go ahead and `print()` the value

## The Interpreter as a Calculator
Let's try a few different things we can do with the Interpreter, which can easily act as a calculator.

```
>>> 1 + 1
2
>>> 4 - 15
-11
>>> 2 * 4
8
>>> 9 / 3
3.0

>>> (1 + 2.5) * .5
1.75
>>>
```

## Running Python Scripts
Let's run a Hello World script.

# Programming Fundamentals
Let's cover a few general concepts that every programming language has. These fundamental building blocks will allow us to build all possible programs.

- Data Types
- Expressions
- Variables
- Conditionals
- Loops

## Data Types
- Numbers
- Strings
- other types


## Expressions
Here are some expressions:
```
>>> 1
>>> "This string is an expression, albeit a simple one"
```

## Variables
## Conditionals
## Loops
## Data Structures
In order to compose

### Array
Arrays are *immutable*, ordered lists of like elements.

For example:
```python

```

### List
Lists are *mutable*


# Programming with Python
A highly recommended overview of how Python works can be found at [Learn Python in Y Minutes](https://learnxinyminutes.com/docs/python3/).

## Python Data Structures
- Lists
- Dictionaries
- Tuples

### Lists

## List Manipulation (Slicing)



## String formatting
https://pyformat.info/

## Reading from a file
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

## String slicing

## Reading a CSV File
https://docs.python.org/3.6/library/csv.html

# Let's Make Something
Now that we know how to do lots of cool things, let's program something real. Let's make a program which reads data from a CSV file and computes values from it.

# Where to Go From Here?
Python has extensive libraries for Scientific Analysis and Computation.
- [PyPi](https://pypi.python.org/pypi): The Python Package Index
    - The Python Package Index is a repository of software for the Python programming language. Find a package you'd like to use in your program!
- [NumPy](http://www.numpy.org/)
    - NumPy is the fundamental package for scientific computing with Python.
    - Useful things:
        - N-dimensional array object (matrix)
        - useful linear algebra, Fourier transform, and random number capabilities
- [SciPy](https://www.scipy.org/)
    - Python-based ecosystem of open-source software for mathematics, science, and engineering.
    - Includes NumPy!
- [Keras](https://keras.io/): Deep Learning library for Theano and TensorFlow
- RNA Sequencing Analysis
    - [READemption](https://github.com/konrad/READemption): a pipeline for the computational evaluation of RNA-Seq data]
- [PyGame](www.pygame.org): Python game engine.
    - Useful for more than just games, PyGame can be used to visualize simulations.
- [Anaconda](https://www.continuum.io/downloads) data science platform
    - Includes NumPy, SciPy, and more
- [Python(x,y)](http://python-xy.github.io/): A Scientific Python Distribution

# Resources, Useful Links, and Sources
- [Main Python Documentation](https://docs.python.org/3/)
- [Python Tutorials](https://www.learnpython.org/)
- [10 Minute Overview of Python](https://learnxinyminutes.com/docs/python/)
- [Popular Python Packages](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/)
- [Python Tutorial for Science from NYU](http://www.physics.nyu.edu/pine/pymanual/html/pymanMaster.html)
- [Python Crash Course for Scientists](http://nbviewer.jupyter.org/gist/anonymous/5924718)
- [Sample Datasets](https://vincentarelbundock.github.io/Rdatasets/datasets.html)
