import turtle as t
import random
import colorgram

timmy = t.Turtle()
timmy.shape("arrow")
timmy.color("black")
timmy.pencolor("black")
t.colormode(255)
def random_color():
    c_tuple = []
    for _ in range(3):
        c_tuple.append(random.randint(0,255))
    return tuple(c_tuple)

def square():
    dist = int(input("How much distance should timmy cover: "))
    for _ in range(4):
        timmy.forward(dist)
        timmy.right(90)
# square()
# def dashed_line():
#     space = int(input("How much space do you want between the dashes?: "))
#     line_len = int(input("How long should the line be?: "))
#     dist = 0
#     while dist != line_len/2:
#         timmy.fd(space)
#         timmy.up()
#         timmy.fd(space)
#         timmy.down()
#         dist += space
# dashed_line()
def draw_pattern():
    side_len = int(input("What do you want the side length to be?: "))
    num_side = 3
    num = int(input("How many shapes do you want to draw?(1-10): "))
    for _ in range(num):
        timmy.pencolor(random_color())
        angle = 360/num_side
        for _ in range(num_side):
            timmy.fd(side_len)
            timmy.right(angle)
        num_side += 1
# draw_pattern()
def random_walk():
    angle = [0,90,180,270]
    len = int(input("How much should timmy walk with each step?: "))
    num_steps = int(input("How many steps should timmy take?: "))
    tot_dist_cov = len*num_steps
    dist = 0
    timmy.width(4)
    timmy.speed(0)
    while dist != tot_dist_cov:
        for _ in range(num_steps):
            timmy.pencolor(random_color())
            timmy.fd(len)
            timmy.setheading(random.choice(angle))
            dist += len
# random_walk()
def spirograph():
    timmy.speed(0)
    radius = int(input("Enter the radius of individual circle: "))
    tilt = int(input("Enter the amount of shift after every circle: "))
    for _ in range(int(360/tilt)):
        timmy.pencolor(random_color())
        timmy.circle(radius)
        curr_heading = timmy.heading()
        timmy.setheading(curr_heading + tilt)
# spirograph()
colors = colorgram.extract("image.jpg", 30)
colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    colors_list.append(new_color)
for i in range(3):
    colors_list.pop(i)
timmy.speed("fast")
timmy.up()
timmy.setpos(int(-300),int(-300))
timmy.down()
uplen = int(input("How much space should be between the dots?: "))
dist = int(input("How long should the line be?: "))
def dashed_dots(uplen,dist):
    dist_cov = 0
    while dist_cov != dist:
        timmy.dot(20,random.choice(colors_list))
        timmy.up()
        timmy.fd(uplen)
        dist_cov += uplen
def hirst_painting(uplen,dist):
    tim_y_pos = -300
    while tim_y_pos != 200:
        dashed_dots(uplen,dist)
        tim_y_pos += 50
        timmy.setpos(-300,tim_y_pos)
hirst_painting(uplen,dist)
screen = t.Screen()
screen.exitonclick()
