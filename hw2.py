import turtle, platform, math

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

#Remember, you must place a # before any comment, or it will be
# interpreted as Python code, and will probably cause errors.

# cents
#==========================================
# Purpose: The function computes the total number of cents based upon
# the number of quarters, dimes,  nickels, and pennies given
# Input Parameter(s): number of quarters($0.25), dimes($0.10),
# nickels($0.05), and pennies($0.01)
# Return Value: total value of money, in cents
#==========================================

def cents(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters*25
    total += dimes*10
    total += nickels*5
    total += pennies
    return total

# draw_M
#==========================================
# Purpose: The function draws the official logo of the University of Minnesota
# using turtle graphics
# Input Parameter(s): None
# Return Value: None
#==========================================

def draw_M():
    turtle.delay(0)
    turtle.bgcolor("gold")
    turtle.hideturtle()
    turtle.color("maroon")
    turtle.penup()
    turtle.setpos(-200,-100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(14)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(128)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(14)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(28)
    turtle.right(60)
    turtle.forward(140)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(140)
    turtle.right(60)
    turtle.forward(28)
    turtle.left(90)
    turtle.forward(64)
    turtle.end_fill()

# Part B: star8
#==========================================
# Purpose: The following function draws an 8-pointed star using turtle graphics
# Input Parameter(s): None
# Return Value: None
#==========================================

def star8():
    turtle.penup()
    turtle.setpos(0,100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(200)
    turtle.right(45)
    turtle.backward(200)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.backward(200)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.backward(200)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.backward(200)
    turtle.right(45)

# Part C: trajectory
#==========================================
# Purpose: The following function computes the horionztal and vertical speeds,
# flight time, and distance travelled of a ball thrown
# Input Parameter(s):
# height = initial height in meters, relative to the ground, at which the ball is thrown
# speed = the initial speed at which the ball is thrown in meters per second
# angle = the initial angle at which the ball is thrown in degrees between 0 and 90
# Return Value: The distance travelled by the ball, in meters
#==========================================

def trajectory(height, speed, angle):
    horizontal_speed = speed * math.cos(angle * math.pi / 180)
    vertical_speed = speed * math.sin(angle * math.pi / 180)
    time = 0
    time = (vertical_speed + (vertical_speed**2 + 19.6*height)**(1/2)) / 9.8
    distance_travelled = 0
    distance_travelled = round(horizontal_speed * time, 3)
    print("Horizontal Speed: " + str(round(horizontal_speed, 3)) + " m/s")
    print("Vertical Speed: " + str(round(vertical_speed, 3)) + " m/s")
    print("Flight Time: " + str(round(time, 3)) + " s")
    return str(round(distance_travelled, 3)) + " m"
