# Classes, Part 2

In this lesson you will learn about `Operator overloading`.

## Helpful links

https://www.geeksforgeeks.org/operator-overloading-in-python/

## Getting started and Tips

Try doing just the addition method first.  Don't create the entire Point2d class first.

If you get stuck, you can use the classes_part2.py from answer to "Test" your code.  It runs all tests and prints out True if it passes the test.

NOTE: The point2d.py in answer is over-engineered and overly complex, you don't have to do what I did.

## What is Operator Overloading?

Lets say you have your pet class from classes_part1.  You want to add in a `mate` method so you can breed your cats and sell the litter.

You could create a method called mate on the pet class, and then you say p1.mate(p2), and that would probably be the better way to do this.

However, Lets say you wanted to use math like the + operator to indicate this.
```python
# create a two pets, and then mate them
female = Pet('tabatha', 'mammal', 'cat')
male = Pet('Dane', 'mammal', 'cat')
child = female + male
```

So with the above example we are re-purposing the + operator.  We are `overloading` it.  It no longer means mathmatical addiiton like 1 + 2, nor does it mean concatenation like 'john ' + 'Doe'.

In this above situation a new Pet instance would be created if the parent category and sub-category are the same, both are alive, and are of opposite sex.

## More details about Operator Overloading

Python like C++ and other language allows us to do this by using "magic" or "predefined" method names.

|Operatror|Magic Method|Note|
|---|---|---|
|Constructor|`__init__`(self, [params]])|Called when we create a class instance|
|+|`__add__`(self, other)|We define what happens when a user does p3 = p1 + p2|
|-|`__sub__`(self, other)|We define what happens when a user does p3 = p1 - p2|
|*|`__mul__`(self, other)|We define what happens when a user does p3 = p1 * 10|
|/|`__truediv__`(self, other)|We define what happens when a user does p3 = p1 /10|
|==|`__eq__`(self, other)|We define what happens and how to compare p1 and p2|
|!=|`__ne__`(self, other)|We define what happens and how to compare p1 and p2|
|str|`__str__`(self, other)|This is so we can change what we want to be printed out about our class|

# Why do we need to do this, what happens if we don't?

If you were to create a class and try to do mathmatical operations on it, you would get errors.

```python
a = Point(10, 100)
b = Point(20, 200)
c = a + b
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
c = a * 10
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'Point' and 'int'
```

For the == and !=, it wouldn't error, but it wouldn't be comparing the VALUES of a.x and b.x, instead it would be checking if the two objects were the same object.

```python
a = Point(10, 100)
b = Point(20, 200)
a == b
False
c = Point(20, 200)
b == c
False
b.x == c.x
True
b.y == c.y
True
d = b # Set D as a "refrence" to b, so they are the same object with 2 alias'
b == d # Now it works, because they are actually the same object.  Not what we want
True
```

We would like the Point class to compare the CONTENTS of the x and y variables, not if the 2 classes are the same



## Items Learned:
1. More class creation learning
1. What operator overloading is

---

## Part 2 Assignment Overview

We will create a class to store the X and Y positions of a object like a Vector or a Point.

We will use this class in part3 to create a bullet class, and learn about `inheritance` and `polymorphism`

## Assignment Files

 - point2d.py
 - classes_part2.py


## Assignment Pieces (point2d.py)

1. Inside **point2d.py** create a class called Point2d.
1. The class will have the following instance variables.

    |Variable|Required|Default|Info|
    |---|---|---|---|
    |**x**|Yes|   |The X coordinate|
    |**y**|Yes|   |The Y coordinate|
1. Create a class constructor using the `__init__` method that accepts 2 values (x and y), then stores them in self.x and self.y.
1. Create an operator overload for **addition** + using the method name `__add__`.  Notice it is similar to `__init__`.
   - Should have self and another variable name for the passed in point object.
   - Suggest using o for other, or p for point.  My example names the parameter **other** for learning/teaching purposes.
   - Example below is inflated and could be simplified to 2 lines.
    ```python
    # example for first on
    # Expected use:  p3 = p1 + p2
    def __add__(self, other):
       newx = self.x + other.x # add the X values of the two points and store that
       newy = self.y + other.y # add the Y values of the two points and store that
       newpoint = Point2d(newx, newy) # Create a new point witrh those newx and newy values
       return newpoint # Return the new point
    ```
1. Create an operator overload for **subtraction** - using the method name `__sub__`.
1. Create an operator overload for **multiplication** * using the method name `__mul__`.
   - Note, for this one, the other object is just a number, not a point.
   - Meaning to create newx and newy would be like this
    ```python
    newx = self.x * other
    newy = self.y * other
    ```
   - Figure out the rest by yourself
1. Create an operator overload for **division** / using the method name `__truediv__`.
1. Create an operator overload for **equals** == using the method name `__eq__`.
1. Create an operator overload for **not equals** != using the method name `__ne__`.


## Assignment Pieces (classes_part2.py)

This will be a class that has you play around with learning how to use the overloaded operators.

Recommend doing this part last

1. Import the Point2d class from the point2d file
1. Create [2] `Point2d` instances of the Point2d class.
   - p1     Values: 10, 100
   - p2     Values: 50, 10
1. Create a third `Point2d` instance that adds those 2 points together, using the + symbol.
   - Add them:  p3 = p1 + p2
   - Print result:  print(p3)
   - **Result:**    60, 110
1. Create a forth `Point2d` instance that subtracts p1 and p2, and print it out
   - **Result:** -40, 90
1. Create a fifth `Point2d` instance that divides p1 by 10 and prints it out
   - **Result:** 1.0, 10.0
1. Create a sixth `Point2d` instance that multiplies p1 by 10 and prints it out
   - **Result:** 100, 1000
1. Create a seventh `Point2d` instance that uses the `if` statement and checks if p1 and p2 are equal, and print out 'equal' if they are, or 'not equal' if they arn't.
1. Play around with the Point2d class, making sure you understand the overloading.


## Requirements:
1. Must use the mathmatical operators in classes_part2.py.  So p3 = p1 + p2 or if p1 == p2:
1. Must get the expected results supplied when using the values supplied
