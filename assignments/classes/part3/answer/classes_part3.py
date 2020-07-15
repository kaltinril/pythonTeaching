from point2d import Point2d
from bullet import Bullet
from plain_bullet import PlainBullet

b = Bullet(1, Point2d(0, 1), Point2d(100, 100))
p = PlainBullet(2, Point2d(0, 1), Point2d(200, 200))

b.fire()
b.draw()

p.fire()
p.draw()

