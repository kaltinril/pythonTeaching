# If, else
All lessons are in the Python Programming Language.

## Purpose:
A program that starts at the top, and goes to the bottom will always run the same way.  We need a way to do certain actions one way when a user gives us an answer, and another way when the user gives us a different answer.

For instance, if you make a game, you want the program to do different things depending on which direction the player goes (Which button they press).  To do that you need to check which button they pressed, and then do something.

## References:
- Free online Editor and IDE: https://repl.it/languages/python3
- Free online help about Python:  https://www.w3schools.com/python/
- These lessons: https://github.com/kaltinril/pythonTeaching/tree/master/assignments/4thgrade

## Flow control Explained (If, Else)
How do we control the flow?  Well, we use a command called `IF`.  The if statement can be thought of like a normal conversation or sentence.
- "If it's raining outside, bring your umbrella."

In the above sentence, you would only bring your umbrella if it is raining.  This is why we need the flow control statement `IF` .

## If: (Structure)
This is the format, or structure, of the `IF` statement.

```python
if CONDITION:
    some_code
    print("message")
    more_code
```

`CONDITION` is any value or math equation that can be `TRUE` or `FALSE`.

## If: (Example: compare variable and number)
```python
if age == 10:
    print("You're old enough for 5th grade!")
```

The == means "is the left side the same value as the right side"

The == is what's called an `operator`.

## If: (Example: Is it raining?)

```python
if raining == True:
    print('Bring your umbrella!')
```

## If: (Example: compare variable and string)
Lets have a small program that asks the user to pick red or blue.  
- If they pick blue, it will say 'That's wonderful!'
- If it's red, it will say 'I like red too!'

```python
color = input("Pick red or blue: ")

if color == "red":
    print("I like red too!")

if color == "blue":
    That's wonderful!
```

## If: (A few other basic operators):

|operator|name|purpose|
|--------|----|-------|
|==|Equal|Check if two values are the same|
|!=|Not Equal|Check if two values are different|
|<|Less than|Check if the left value is less than the right value|
|>|Greater than|Check if the left value is greater than the right value|


## If: (Else)

Using the same example from before, lets add to it with the `else` condition.
- "If it's raining outside, bring your umbrella, otherwise just bring a coat."

We see that if it is not raining, we are expected to bring at least a coat.

### If...Else, in code

```python
if raining == True:
    print('Bring your umbrella!')
else:
    print('Bring your coat!')
```

Notice that the `else` also requires the `colon` : character.

## If...Elif...else...

There is yet one more situation.

Perhaps you have three or more possible outcomes.  For instance, what if it was snowing?
- "If it's raining outside, bring your umbrella, However if it's snowing bring snow gear, otherwise just bring a coat."

So this is saying three things now:
1. If it's raining, bring an umbrella
1. If it is snowing, bring snowgear
1. If its neither, just bring a coat.

### If...Elif...else... (Example)
Here is how we would do that in an example:

```python
if raining == True:
    print('Bring your umbrella!')
elif snowing == True:
    print('Bring your snow gear!')
else:
    print('Bring your coat!')
```

This will make sure we wear the appropriate attire for each situation.