# Printing, Variables, and Input
All lessons are in the Python Programming Language.

## Purpose:
This lesson will explain variables, let them make their first program, and get text input from users. 

## References:
- Free online Editor and IDE: https://repl.it/languages/python3
- Free online help about Python:  https://www.w3schools.com/python/

## Your first program:
The first program in many languages is often called the "Hello World" program.  It's the amount of code needed to get a basic program up and running and print out the phrase "Hello World".  
```python
print("Hello World")
```

Believe it or not, this is a complete working program in Python.  It prints out the words "Hello World" to the screen.

## Variables:
A variable (pronounced **very-a-bowl**), is a way to store information in programming.  

When you download and play a game, it usually asks you things like:
- Name your character
- Pick the color of your hair
- Pick the color of your eyes
- and so on...

This information is stored in a variable.  This is so that we can later use this information in our program.

In python, to save information into a variable we need 3 parts.
1. Name of the variable (Where to put the data)
1. Special command that lets python know you want to save data: The equals sign =
1. The data you want to store
   - **Example:** Lets create 3 variables, one to store your name, one to store your favorite color, and one to store your age.
        ```python
        first_name = "Jeremy"
        age = 38
        favorite_color = "Hot Pink"
        ```

Notice how `letters` and `words` require a **quote** mark surrounding them.  These are called Strings.

Notice also that `numbers` _do not_ require a **quote**.

## Format to store information:
```python
variable_name = "Text to store"
variable_name2 = 123456
```

## Getting input from the user:
There is a built-in command to get text and number input from the user.  The function is called input.  All lowercase.  Once we get that data from the user, we need to store it somewhere so we can use it in the program.
```python
name = input("What is your name? ")
```

`name` is the variable we will store the response from the user in.

`Input` will first print our message to the user, and then it will wait for the user to type a message, and press enter.  Whatever they typed will be stored in name.