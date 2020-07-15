# Classes, Part 2

In this lesson you will learn about `Inheritance` and `Polymorphism`.

## What is Inheritance?

Just like the word sounds in real life family relationships, inheritance is when something from a parent is passed down to a child.

In programming, this is when variables and methods from a parent class are defined once, but able to be used in a child class.

## What is Polymorphism?

Often it is necessary to loop over a list of items, but its possible each item could be different.  One way to resolve this is by using Inheritance and Polymorphism.

Lets say you are making a **SHUMP** like **1943** or **R-TYPE** or **Galaga**.  Each player might have a different plane/spaceship. Each might shoot different types of bullets depending on the power-up.  

It would be nice if you could loop over all bullets, regardless of the type.

With Polymorphism, this can be done by creating a "Base" or "parent" class called `Bullet`.  Each different type of bullet would be a sub-class.  


Parent: `bullet`

Children:
 - laser
 - missile
 - machinegun

We could have `laser` and `missile` and `machinegun` all being sub-classes inheriting from the base (or parent) `bullet` class.  
This allows us to call the relevant method for that specific type of bullet for methods like `playHitSound()`, `draw()`, or `update()`.

**WARNING: Big example below**

This means our code might look something like this:
```python
# Here is just some setup example code, this next bit isn't polymorphism
# Skip over this big IF statement if it's confusing as it doesn't relate directly

# Random code that adds different bullets to the bullets list
if player.pressedFireButton():
  if player.bulletType == 'laser':
    bullet = Laser(player.position, player.getBulletDamage())
  elif player.bulletType == 'missile':
    bullet = Missile(player.position, player.getBulletDamage())
  elif player.bulletType == 'machinegun':
    bullet = MachineGun(player.position, player.getBulletDamage())
  else:
    bullet = Bullet(player.position, player.getBulletDamage())

  # Add the bullet created in the above if/elif/else conditional
  # We are still inside the if player.pressedFireButton() conditional
  bullets.add(bullet)

# == This Next part is where polymorphism takes over               ==
# == Each bullet in the list could be a                            ==
# == laser, missile, machinegun, or regular bullet                  ==
# == Do we call Laser.applyDamage() ? or MachineGun.applyDamage()? ==
# == We don't care, we just call the methods and                   ==
# == we let the compiler and polymorphism do its thing             ==
# == It will find the correct method for the correct class to call ==

# Loop over all bullets in the bullet list
# If any collided with a ship, play sound, damage the ship, and destroy the bullet
# If any went off the screen, destroy the bullets
# Otherwise, simply update the position of the bullet, and then draw it

for b in bullets:
  if b.collidesWith('playerShip'):
    b.playHitSound()
    b.applyDamage('playerShip')
    b.destroy()
  elif b.outOfBound(screen_size):
    b.destroy()
  else:
    b.update()
    b.draw()

```

## Items Learned:
1. What is Inheritance and how to create sub-classes
1. What is polymorphism and how does it help

---

## Part 1 Assignment Overview

We're going to make a few classes to represent different types of bullets.  This will allow us to use the code like the loop above.

We will be doing all of this in text, and will not be doing real drawing of any kind.

## Assignment Files

 - point2d.py
 - bullet.py
 - plain_bullet.py
 - laser.py
 - missile.py
 - machine_gun.py
 - classes_part2.py

## Assignment Pieces (point2d.py)

Please copy your point2d.py file from part2, or, use the part2 answer.

## Assignment Pieces (bullet.py)

We will create a class that will be our root/base/parent class.  Some of the variables in here are not going to be used, but help to illustrate the purpose of this class.

1. Inside **bullet.py** create a class called Bullet.
1. Create a class constructor method that can take the below 6 variables as input to set the instance variables.
   - Make sure only the first 4 arguments are required, and the others are set to default if not provided.
   
    |Variable|Required|Default|type|Info|
    |---|---|---|---|---|
    |**damage**|Yes|1|int|The amount of damage this bullet will do|
    |**velocity**|Yes|Point2d(0, 0)|Point2d|Direction and speed of travel|
    |**position**|Yes|Point2d(50, 50)|Point2d|X/Y location on the screen the bullet is at|
    |**active**|No|False|bool|If the bullet has been fired or not|
    |**visible**|No|True|bool|If the bullet can be seen or not|
    |**fire_sound_filename**|No|None|string|filname for the sound file that should play when a bullet is fired|
    |**hit_sound_filename**|No|None|string|filname for the sound file that should play when a bullet hits something|
    
   - Regardless of if they are provided or not, still create the instance variables.
    
1. Create a class method in bullet called `update`.
   - If the bullet is active:
     - This should update the position using the velocity.  To do this add both together, then update the position with the result.
1. Create a class method in bullet called `draw`.
   - If the bullet is visible and active.
     - Print out the following all on one line:
       - The text 'Bullet'
       - Position
       - Velocity
     - example:  Bullet 100, 100 3, 5 
1. Create a class method in bullet called `destroy`.
   - This method will change **self.active** and **self.visible** to `False`.
1. Create a class method in bullet called `apply_damage`.
   - This method accepts a string (The name of the object hit, like 'player1' or 'boss').
   - print to the screen "# damage done to $" where # is the **self.damage**, and $ is the string passed in.
   - print to the screen the name of the file that WOULD have been the sound playing
1. Create a class method in bullet called `fire`.
   - This will verify the bullet is not **active**, then set active to `True`.

That's it, our parent bullet class is complete.

## Assignment Pieces (plain_bullet.py)

This class will have no new functionality, only to demonstrate it is possible to create an empty named child class

This class will be a sub-class of Bullet.  Create it as such.  The python code below is the FULL implementation.

Note the keyword `pass` which allows us to create this empty (and pretty useless) sub-class.

```python
from bullet import Bullet
class PlainBullet(Bullet):
  pass
```

This gives us the basic framework for a child sub-class.  All other classes will start like this. 
We may override or change functionality in specific methods, add new variables, and even change the constructor.

The keyword `pass` will not be used in the other sub-classes.


## Assignment Pieces (laser.py)

This class will inherit from Bullet.  It will have a few small changes to make it unique.

### Items learned in laser.py
1. We will learn how to hard code and exclude a parameter from the sub-class constructor.
1. Learn how to override a method

### Steps to create

1. Inside **laser.py** create a class called Laser that inherits from `Bullet`.
1. Create a constructor `__init__` to override the parent Bullet's constructor.  
   - To make this easier, copy the declaration from Bullet.
   - Remove the Active parameter from the list of arguments, the laser is always on once created.
     - Notice in the code example how I explicitly pass in True for Active to the parent
   - Use the `super()` keyword to pass the variables into the parent's `__init__` constructor.
     - Example:
       ```python
       def __init__(damage, velocity, position, visible=True, etc=True):
         super().__init__(damage, velocity, position, True, etc) # This calls Bullet's __init__ method
       ```  
1. Create a new draw method, it should be the same as bullet's except it should print Laser instead
   - This is to simulate how the drawing could be completely different for the laser bullet type.
   - Example output:  Laser 100, 100 0, 1


## Assignment Pieces (missile.py)

This class will inherit from Bullet.  It will have a few small changes to make it unique.

### Items learned in missile.py
1. We will learn how to add extra parameters to the sub-class constructor.
1. Learn how to override a method

### Steps to create
1. Inside **missile.py** create a class called Missile that inherits from `Bullet`.
1. Create a constructor `__init__` to override the parent Bullet's constructor.  
   - To make this easier, copy the declaration from Bullet.
   - Add another parameter to this method.
     - **target:** string: The name of the target (Simulates the idea of the missile locking onto an enemy ship)
   - Use the `super()` keyword to pass the variables into the parent's `__init__` constructor.
     - NOTE: Do not pass the target variable into the super's init.
   - After calling super().__init(...) set the instance variable for `target`.
1. Create a new draw method, it should be the same as bullet's except:
   - it should print Missile instead
   - Add another print that prints out the word "smoke".
      - This simulates that we could be drawing smoke trails behind the missile
   - Add another print that prints out the target the missile is locked on to
     - NOTE: This is the target that was passed into the constructor.
   - This is to simulate how the drawing could be completely different for the missile bullet type.
   - Example output:  Missile 100, 100 0, 1 smoke big_boss_battle_enemy

## Assignment Pieces (machine_gun.py)

This class will inherit from Bullet.  It will have a few small changes to make it unique.

### Items learned in machine_gun.py
1. We will learn how to hard code and exclude a parameter from the sub-class constructor.
1. We will learn how to add extra parameters to the sub-class constructor.
1. Learn how to override a method

### Steps to create
1. Inside **machine_gun.py** create a class called MachineGun that inherits from `Bullet`.
1. Create a constructor `__init__` to override the parent Bullet's constructor.  
   - Similar to laser, there is no need for Active, it will always be active.
   - Add another required parameter `overheat_time`.
     - This is how long until we overheat the gun (seconds)
     - This is a variable to simulate the idea that the machine gun will overheat and we can't fire again until it cools down.
     - We won't be implementing anything for this really except toggling the next instance variable.
1. Add another instance variable called `overheated` and default it to `False`.
   - That isn't allowed to be passed in, and shouldn't be in the constructor arguments.
   - This will be toggled to True when the gun overheats (We'll simulate this) and back to False once it cools down (We won't do this)
1. Override the draw method by creating it again in this class.  It should be the same as bullet's except:
   - it should print **Machine Gun** instead
   - Add another print that prints out the message "I've given her all she's got capt'n" if overheated is True
     - This is to simulate how the drawing could be completely different for the missile bullet type.
     - For instance, the machine gun could glow red, and give off smoke, indicating it overheated
   - Example output:  Machine Gun 100, 100 0, 1 "I've given her all she's got capt'n"
1. Override the `update` method to toggle the Overheated variable every time update is called.
   - Don't forget to call super().update()

## Assignment Pieces (classes_part2.py)

This will be a class that creates instances of bullets and loops over them.

 ** Recommend doing this part last

1. From the files you've created, import the classes from each.
    ```python
    from point2d import Point2d
    from bullet import Bullet
    from plain_bullet import PlainBullet
    from laser import Laser
    from missile import Missile
    from machinegun import MachineGun
    ```

1. Create an empty list called **bullet_list**.
1. Create an instance of a `Bullet` class called **b**.
   - Damage: Anything
   - Velocity: 0, 1
   - Position: 100, 100
1. Create an instance of a `PlainBullet` class called **p**.
   - Damage: Anything
   - Velocity: 5, 1
   - Position: 200, 200
1. Create an instance of a `Laser` class called **l**.
   - Damage: Anything
   - Velocity: 0, 7
   - Position: 140, 102
1. Create an instance of a `Missile` class called **m**.
   - Damage: Anything
   - Velocity: 0, 3
   - Position: 324, 12
   - target: 'big_boss_battle_enemy'
1. Create an instance of a `MachineGun` class called **mg**.
   - Damage: Anything
   - Velocity: 0, 2
   - Position: 90, 5
   - overheat_time: anything
1. Append each of the above instances to the **bullet_list**
1. Loop over the bullet_list and call `fire` on each instance.
1. Create another new loop to loop 3 times and do the following
   - Inside the above loop: loop over the **bullet_list** 
     - Call the `update` and `draw` methods.

## Example output:

Notice how PlainBullet just prints bullet because we didn't change it's draw method.

Notice how Machine Gun, while first time calling draw it not overheated, but second time it is because we called update inbetween.

Notice how the position is updating based on the value of velocity each time we call update.
> Bullet 100, 100 0, 1
>
> Bullet 200, 200 5, 1
>
> Laser 140, 102 0, 7
>
> Missile 324, 12 0, 3 smoke big_boss_battle_enemy
>
> Machine Gun 90, 5 0, 2
>
> Bullet 100, 101 0, 1
>
> Bullet 205, 201 5, 1 
>
> Laser 140, 109 0, 7
>
> Missile 324, 15 0, 3 smoke big_boss_battle_enemy
>
> Machine Gun 90, 7 0, 2 I've given her all she's got capt'n
>
> Bullet 100, 102 0, 1
>
> Bullet 210, 202 5, 1
>
> Laser 140, 116 0, 7
>
> Missile 324, 18 0, 3 smoke big_boss_battle_enemy
>
> Machine Gun 90, 9 0, 2
