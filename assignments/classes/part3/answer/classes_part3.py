from point2d import Point2d
from bullet import Bullet
from plain_bullet import PlainBullet
from laser import Laser
from missile import Missile
from machine_gun import MachineGun

bullet_list = []

# Create 1 of each type of bullet
b = Bullet(1, Point2d(0, 1), Point2d(100, 100))
p = PlainBullet(2, Point2d(5, 1), Point2d(200, 200))
l = Laser(3, Point2d(0, 7), Point2d(140, 102))
m = Missile(3, Point2d(0, 3), Point2d(324, 12), 'big_boss_battle_enemy')
mg = MachineGun(3, Point2d(0, 2), Point2d(90, 5), 10)

# Add all the different types of bullets to the list
bullet_list.append(b)
bullet_list.append(p)
bullet_list.append(l)
bullet_list.append(m)
bullet_list.append(mg)

# Call fire to "Activate" each bullet
# This simulates when a player would fire the bullet
for bul in bullet_list:
    bul.fire()

# Loop 3 times over all bullets, draw and update them to simulate 3 game frames
for i in range(0, 3):
    for bul in bullet_list:
        bul.draw()
        bul.update()
