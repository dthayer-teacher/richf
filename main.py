import turtle
import random

score = 0

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('aquamarine')

t = turtle.Turtle()
t.hideturtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t2.hideturtle()
t2.fillcolor('red')
t2.penup()
t2.goto(0, 100)
t2.pendown()
t3.penup()
t3.goto(0, 200)
t4 = turtle.Turtle()
t4.penup()
t4.goto(0, 150)

t.penup()
t.goto(0, 50)
t.pendown()
t.write("Tom The Flying Turtle", font=("Arial", 24, "bold"), align="center")
t.penup()
t.goto(0, -50)
t.pendown()
t.write("Camryn Temme", font=("Arial", 24, "bold"), align="center")

enter = input("Press Enter to Start")
t.clear()
t2.clear()

running = True
while running:
    for i in range(1, 6):
        t3.clear()
        t3.write("Round " + str(i), font=("Arial", 24, "bold"), align="center")
        t4.clear()
        t4.write(str(score) + " / " + str(i), font=("Arial", 24, "bold"), align="center")
        t.clear()
        t2.clear()

        mult = 0
        sign = random.randint(1, 2)
        if sign == 1:
            mult = -1

        else:
            mult = 1

        x_num = random.randint(80, 200)
        x_dir = mult * x_num

        TARGET_LOW_LEFT_X = x_dir
        TARGET_LOW_LEFT_Y = random.randint(-200, 200)
        TARGET_WIDTH = random.randint(15, 50)

        t.penup()
        t.goto(0, 0)
        t.pendown()

        screen.bgcolor('silver')
        t.setheading(0)
        t.penup()
        t.goto(TARGET_LOW_LEFT_X, TARGET_LOW_LEFT_Y)
        t.pendown()
        t.forward(TARGET_WIDTH)
        t.left(90)
        t.forward(TARGET_WIDTH)
        t.left(90)
        t.forward(TARGET_WIDTH)
        t.left(90)
        t.forward(TARGET_WIDTH)
        t.left(90)

        t.setheading(0)
        t.penup()
        t.goto(0, 0)
        t.showturtle()

        angle = float(input("Enter an angle: "))
        t.setheading(angle)
        force = float(input("Enter force (1-10): "))
        distance = force * 25
        t.forward(distance)

        if (t.xcor() >= TARGET_LOW_LEFT_X and t.xcor() <= TARGET_LOW_LEFT_X + TARGET_WIDTH) and (
                t.ycor() >= TARGET_LOW_LEFT_Y and t.ycor() <= TARGET_LOW_LEFT_Y + TARGET_WIDTH):
            t2.write("Hit!", font=("Arial", 32, "bold"), align="center")
            score = score + 1
            t4.clear()
            t4.write(str(score) + " / " + str(i), font=("Arial", 24, "bold"), align="center")

        else:
            t2.write("Miss", font=("Arial", 32, "bold"), align="center")
        enter = input("End of Round " + str(i))
    screen.bgcolor('hotpink')
    t.clear()
    t2.clear()
    t3.clear()
    t4.clear()
    t3.goto(0, 100)
    t3.write("Game Over", font=("Arial", 32, "bold"), align="center")
    # dont include this
    question = input("Play Again(y/n): ")
    if question != "y":
        running = False