from point2d import Point2d

p1 = Point2d(10, 100)
p2 = Point2d(50, 10)

p3 = p1 + p2
print('\nP3', p3)
print('P3.x', p3.x == 60)
print('P3.y', p3.y == 110)

p4 = p1 - p2
print('\nP4', p4)
print('P4.x', p4.x == -40)
print('P4.y', p4.y == 90)

p5 = p1 / 10
print('\nP5', p5)
print('P5.x', p5.x == 1.0)
print('P5.y', p5.y == 10.0)

p6 = p1 * 10
print('\nP6', p6)
print('P6.x', p6.x == 100)
print('P6.y', p6.y == 1000)

print('')

if p1 == p2:
    print('Fail Equal Test')
else:
    print('Pass Equal Test')

if p1 != p2:
    print('Pass Not-Equal Test')
else:
    print('Fail Not-Equal Test')