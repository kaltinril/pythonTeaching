# Classes, Part 1

In this lesson you will learn about `classes`.
A `class` is simply a way to group related `variables` and `functions` together into a single object.
You use classes in python all the time without realizing it.  `.upper()` is a function that is part of the string class.

A class is similar to an Equipment Spec.  It defines the structure and behavior.  Then you can create an instance of it to use it.

In this lesson we will create a class to for our pets.

The basic structure of a class is:

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
1. What classes are
1. How to create a basic class
1. How to create class variables
1. How to use classes, their variables, and call their methods

## Assignment:
1. Create 2 files.  
   - classes_part1.py
   - pet.py
1. **classes_part1.py** will ask the user to enter information about their pets.
   - Create a list of pets (at least 4)
   - One where you only pass in the first 3 arguments.
   - One where you pass in all the arguments.
   - One where you put the last_fed date in the past by 1 day.
   - One where you put the last_fed date in the past by 10 days.
   - After creating the pets, run a loop over the list and perform the below checks:
     - Print out if the pets are fed or not.  If they are not fed, feed them.
     - If it has been more than 3 days since the pet was fed, the pet has died.  Set the deathdate.
1. Inside **pet.py** create a class called Pet.
1. The class will have the following variables (The [R] is required):
   - [R] **name**
   - [R] **category** (Restrict to [mammal, reptile, etc])
   - [R] **type** (Restrict to [dog, cat, fish, as many as you want])
   - **birthdate** (string format 'mm/dd/yyyy') [**Default:** None]
   - **colors** (array of color names the pet has) [**Default:** None]
   - **has_tail** (True/False) [**Default:** False]
   - **has_wings** (True/False) [**Default:** False]
   - **num_of_legs** (most have 2 or 4, but octopuses spiders and some insects have more) [**Default:** 4]
   - **last_fed** (date of the last time the pet was fed)  [**Default:** None]
1. Create a class constructor function that takes the above variables as input to set the class variables.
   - Make sure only the first 3 are required, and the others are set to default if not provided.
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
### How to create a class called "State" in file state.py
```python
from datetime import datetime, timedelta

class State:
    def __init__(self, name, capital, population = None, gmt_offset = -9):
        self.name = name
        self.capital = capital
        self.population = population
        self.gmt_offset = gmt_offset
    
    def display(self):
        print('The capital of ' + name + ' is ' + capital)
    
    def get_local_time(self, time):
        return datetime.today() + timedelta(hours=gmt_offset)
    
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
