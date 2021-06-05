# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# color_codes = []
# for color in colors:
#     code = []
#     for j in color.rgb:
#         code.append(j)
#     color_codes.append(tuple(code))
# print(color_codes)
from turtle import *
import random
codes = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
         (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138),
         (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151),
         (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120),
         (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
pablo = Turtle()
pablo.shape("turtle")
pablo.speed("fastest")
pablo.color("green")
pablo.hideturtle()
colormode(255)
for i in range(1, 11):
    pablo.pendown()
    for j in range(10):
        pablo.dot(20, random.choice(codes))
        pablo.penup()
        pablo.fd(40)
    pablo.setpos(0, i * 40)
screen = Screen()
screen.exitonclick()
