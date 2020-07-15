from point2d import Point2d
from bullet import Bullet
from plain_bullet import PlainBullet
from laser import Laser
from missile import Missile

b = Bullet(1, Point2d(0, 1), Point2d(100, 100))
p = PlainBullet(2, Point2d(0, 1), Point2d(200, 200))
l = Laser(3, Point2d(0, 7), Point2d(140, 102))
m = Missile(3, Point2d(0, 3), Point2d(324, 12), 'big_boss_battle_enemy')

b.fire()
b.draw()

p.fire()
p.draw()

l.draw()

m.fire()
m.draw()
