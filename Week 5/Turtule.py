

# ------------------ کشیدن فرفره
# import turtle
# import time
# #
# for i in range(4):
#     turtle.goto(1,1)
#     turtle.forward(300)
#     turtle.right(90)
#     turtle.pensize(5)
#     turtle.pencolor("green")
#
#     for i in range(2):
#         turtle.forward(300)
#         turtle.right(90)
#         turtle.goto(1,1)

# ----------------------------------------

# import turtle
# import time
#
# for i in range(4):
#     turtle.goto(1,1)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.pensize(5)
#     turtle.pencolor("green")
#
#     for i in range(2):
#         turtle.forward(100)
#         turtle.right(90)
#
# for i in range(3):
#     turtle.backward(100)
#     turtle.left(90)


# ----------------------------------------

# ------------------------  ی شکل جدید
# import turtle as t
# import time
# #t.goto(100,100)
#
# for i in range(4):
#         t.hideturtle() # make the turtle invisible
#         # t.speed(0) # set its movement speed to instant
#         t.forward(270)
#         t.right(90)
#         t.pensize(5)
#         t.pencolor("green")
#         t.hideturtle()
# #t.forward(30)
# # t.right(90)
#         for i in range(2):
#             t.forward(30)
#             t.right(90)

# ----------------------------------------

# import turtle as t
# import time
# #t.goto(100,100)
#
# for i in range(4):
#         t.hideturtle() # make the turtle invisible
#         # t.speed(0) # set its movement speed to instant
#         t.forward(270)
#         t.right(90)
#         t.pensize(5)
#         t.pencolor("green")
#         t.hideturtle()
#
# # t.right(90)
# for i in range(2):
#     t.forward(30)
#     t.right(90)

#  --------------------------

# from turtle import *
# import time

# color('blue', 'yellow')
# begin_fill()
# toggle = True
# while True:
#     forward(180)
#     if toggle:
#         right(90)
#     else:
#         right(90)
#     toggle = not toggle
#     if abs(pos()) < 90:
#         break

#forward(30)

# ------------------------------
# def soduko():
#   for i in range(4):
#      forward(240)
#      right(90)
# for n in range(5):
#     backward(30)
#     print(soduko())
# done()

# ------------------------------

import turtle

sc = turtle.Screen()

trtl = turtle.Turtle()

trtl.speed(1)
for i in range(4):
    trtl.forward(270)
    trtl.right(90)


# --------------------------
#set position for y axis

trtl.left(90)
trtl.up()
trtl.setpos(90, -270)
trtl.down()
trtl.forward(270)

#set position for y axis

trtl.up()
trtl.setpos(180, -270)
trtl.down()
trtl.forward(270)




# set position for x lines

trtl.right(90)
trtl.up()

trtl.setpos(90, 90)
trtl.down()
trtl.toward(270)






















# -----------------------------------------
# set position for y lines

# trtl.right(90)
# trtl.up()
#
# trtl.setpos(0,0)
# trtl.down()

# -----------------------------------------
# y lines
#
# for i in range(2):
#     drawy(10 * (i + 1))