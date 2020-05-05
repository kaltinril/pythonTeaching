# Classes, Part 1

In this lesson you will learn about `classes`.

## What is a class?

A `class` is simply a way to group related `variables` and `functions` together into a single object.  
The purpose is to combine all behavior into a single self contained file.  With it's own variables and functions.

You use classes in python all the time without realizing it.  `.upper()` is a function that is part of the string class.

A class is similar to an Equipment Spec.  It defines the structure and behavior.  Then you can create an instance of it to use it.

**The basic structure of a class is:**

```python
class name_of_class:
    # This is the constructor, this method is called when you create an instance of the class
    def __init__(self, class_argument1):
        self.class_variable = class_argument1
    
    def this_is_a_function(self):
        return 'some value'
    
    def another_class_function(self, argument1):
        return argument1 + 2
```

## Items Learned:
1. What classes are all about
1. How to create a basic class
1. How to create class variables
1. How to use classes, their variables, and call their functions

---

## Part 1 Assignment Overview

In this lesson we will create a class to for our pets.  The purpose of this class 
is to keep track of our pets to and make sure we are feeding them on time.

To do this, we will need the ability to create unique instances of the pet class, 
one for each pet we want to track.

We will enter things like the pets name, birthdate, category, and sub-category.

We will create functions to allow us to calculate their age, if they need to be fed, or if they died.


## Assignment Overview

Create a program that lets a user enter in their pets as described above and in detail below.

The program will have all the functionality built into the `pet` class inside the `pet.py` file.  You will create a `main` 
program `classes_part1.py` to get user input and create instances of the `pet` class.


## Assignment Files
1. Create 2 files.  
   - classes_part1.py
   - pet.py

## Assignment Pieces (classes_part1.py)

1. This file will ask the user to enter information about their pets.
   - Create a list variable of pets (at least 4).
      - The first instance, only pass in the first 3 arguments to the pet class constructor.
      - The second instance, pass in all the arguments.
      - The third instance, pass in last_fed date as yesterday's date.
      - The fourth instance, pass in last_fed date as 10 days ago.
   - After creating the pets, run a loop over the list and perform the below function calls and checks:
     - Print out if the pets are fed or not.
        - Meaning call `p.is_fed()` to see if the pet has been fed.
     - If the pet has not been fed:
        - If it has been _**less**_ than 3 days, feed the pet: `p.feed(datetime.now)`
        - If it has been _**more**_ than 3 days since the pet was fed, the pet has died.  Set the deathdate.


## Assignment Pieces (pet.py)

1. Inside **pet.py** create a class called Pet.
1. The class will have the following variables, None is a real value like "null".

    |Variable|Required|Default|Info|
    |---|---|---|---|
    |**name**|Yes|   |The name of your pet|
    |**category**|Yes|   |Restrict to [mammal, reptile, etc]|
    |**subcategory**|Yes|   |Restrict to [dog, cat, fish, as many as you want]|
    |**birthdate**|No|None|string format 'mm/dd/yyyy' |
    |**colors**|No|None|array of color names the pet has |
    |**has_tail**|No|False|(True/False)|
    |**has_wings**|No|False|(True/False)|
    |**num_of_legs**|No|4|most have 2 or 4, but octopuses spiders and some insects have more|
    |**last_fed**|No|None|date of the last time the pet was fed|

1. Create a class constructor function that takes the above variables as input to set the class variables.
   - Make sure only the first 3 arguments are required, and the others are set to default if not provided.
1. Create a class function in pet called `age`.  This should calculate the age of the pet based on the birthday.
1. Create a class function in pet called `is_fed`.  This should return True if the pet has been fed today, otherwise return false.
1. Create a class function in pet called `feed`.  This function has 1 argument, the date the pet was fed.  It should update the last_fed date.  No return value.
1. Create another variable that is set to None by default and the user can not provide this during creation.
   - **deathdate** (string format 'mm/dd/yyyy') [**Default:** None]
1. Create a class function in pet called `died`.  This should accept the date the pet died, and update the `deathdate`

## Requirements:
1. Must create a real class for pet in pet.py
1. Must have a constructor that requires the first 3 variables.  Others are optional and should be set to their defaults.
1. Must have all the functions created with their required arguments and return variables.

---

## Lessons on Classes:

In these example files we create a class called State.  This class is designed
to store 

### How to create a class called "State" in file state.py
```python
from datetime import datetime, timedelta, timezone

class State:
    def __init__(self, name, capital, population = None, gmt_offset = -9):
        self.name = name
        self.capital = capital
        self.population = population
        self.gmt_offset = gmt_offset
    
    def display(self):
        print('The capital of ' + self.name + ' is ' + self.capital)
    
    def get_local_time(self):
        return datetime.now(timezone.utc) + timedelta(hours=self.gmt_offset)
    
    def record_births(self, total_births):
        self.population += total_births
    
    def record_deaths(self, total_deaths):
        self.population += total_deaths
        
        # Can't have a negative population
        if self.population < 0:
            self.population = 0
```

### How to create an instance of the class from another file
```python
import state
s = state.State('Alaska', 'Juneau', 700000)
```

### How to access functions in a class
```python
import state
s = state.State('Alaska', 'Juneau', 700000)

s.record_births(150)
s.record_deaths(10)

s.display()
print(s.get_local_time())
```
