from point2d import Point2d
from bullet import Bullet
from laser import Laser

b = Bullet(1, Point2d(0, 1), Point2d(100, 100))
l = Laser(2, Point2d(0, 1), Point2d(200, 200))

b.draw()