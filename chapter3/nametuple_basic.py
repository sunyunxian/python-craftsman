from collections import namedtuple

Rectangle = namedtuple('Rectangle', 'width, heigh')
rect = Rectangle(100, 200)
print(rect)
print(rect.width, rect.heigh)
