from collections import namedtuple

Color = namedtuple("Color", ['red', 'green', 'blue'])

white = Color(255,255,255)
gray = Color(200,200,200)
black = Color(0,0,0)

print(black.blue)