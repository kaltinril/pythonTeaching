# Random Numbers

To give our programs and games some variety, we can use a random number generator.

Python provides all this for us automatically.

## Purpose:

Learn how to generate random numbers.

## References:
- Free online Editor and IDE: https://repl.it/languages/python3
- Free online help about Python:  https://www.w3schools.com/python/
- These lessons: https://github.com/kaltinril/pythonTeaching/tree/master/assignments/4thgrade

## Random Whole Numbers

The first type of numbers we will generate are `Integers`.  These are another way to say whole numbers.  They are the numbers from -infinity to positive infinity.

Some examples would be -273, 9, 0, 1000000.

To generate a random integer, you need to first include the `random` code library.  Then call the `random.randint()` function

```python
import random

dice = random.randint(1, 6)

print("You rolled a " + str(dice))
```

**Output:**
> You rolled a 3

## Random Decimal Numbers

This is a little more complicated.  First we need to convert the number to a whole number by multiplying it by a power of 10.

### Example with inches: (Random between 0.00 and 12.00)

1. Pick a minimum and maximum value (0 and 12 for our example)
1. Multiply each by 100 first.
1. Get the random value between those new numbers.
1. Convert the result to a decimal with the `float` command.
1. Divide by 100 to get the range 0.00-12.00.

```python
import random

min = 0
max = 12
inches = random.randrange(min * 100, max * 100)
inches = float(inches) / 100
print("You are 4 foot " + str(inches) + " tall!")
```

**Output:**
> You are 4 foot 4.7 inches tall!

##

