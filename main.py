from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()

def move_fd():
  t.fd(10)

def move_bk():
  t.bk(10)

def rotate_lt():
  t.lt(10)

def rotate_rt():
  t.rt(10)

def clear_screen():
  t.reset()

def change_colour():
  a = random.randint(0,1.0)
  b = random.randint(0,1.0)
  c = random.randint(0,1.0)
  t.pencolor(a, b, c)

def pen_up():
  t.penup()

def pen_down():
  t.pendown()

s.listen()

s.onkey(move_fd, "Up")
s.onkey(move_bk, "Down")
s.onkey(rotate_lt, "Left")
s.onkey(rotate_rt, "Right")
s.onkey(clear_screen, "x")
s.onkey(change_colour, "c")
s.onkey(pen_up, "u")
s.onkey(pen_down, "d")

print('''
Press a key to perform the corresponding action:

UP - move in the direction the cursor is facing
DOWN - move in the direction opposite to the one the cursor is facing
LEFT - rotate the cursor anticlockwise
RIGHT - rotate the cursor clockwise
X - clear the screen and move the cursor to default position
C - change the colour of the pen
U - move the pen without drawing
D - move the pen while drawing

''')

