import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

# set up the screen
wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#this creates the head of the snake
head = turtle.Turtle()
head.speed(0) #this is the animation speed
head.shape("square")
head.color("white")
head.penup() #this avoids turtle drawing anything
head.goto(0, 0)
head.direction = "stop"

#this creates the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#functions
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#main game loop
while True:
    wn.update()

    # this checks for collisions with the border
    if head.xcor() > 290 or head.xcor()<-290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0

        pen.clear()
        pen.write("Score: {} High Score {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #food mechanics
    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # move the last segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    #this checks for segment collision with the head
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0

            pen.clear()
            pen.write("Score: {} High Score {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()