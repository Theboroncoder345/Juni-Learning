import turtle
import random
screen = turtle.Screen()
Cooper = turtle.Turtle()
Cooper.speed(1000)

screen.bgcolor("black")

Cooper.shape("turtle")
Cooper.color("white")
Cooper.penup()
Cooper.goto(0,0)

Target = turtle.Turtle()
Target.shape("circle")
Target.color("cyan")
x = random.randint(-200, 200)
y = random.randint(-200, 200)
Target.penup()
Target.goto(x,y)

def shoot():
    Bullet = turtle.Turtle()
    Bullet.color("yellow")
    Bullet.penup()
    Bullet.goto(0, 0)
    Bullet.setheading(Cooper.heading())
    for i in range (200):
        Bullet.forward(5)
        if abs(Bullet.xcor() - Target.xcor()) < 10 and abs(Bullet.ycor() - Target.ycor()) < 10:
            Bullet.ht()
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            Target.goto(x,y)

def right():
    Cooper.right(5)
    
def left():
    Cooper. left(5)
    
screen.onkey(shoot,"space")
screen.onkey(right,"Right")
screen.onkey(left,"Left")
screen.listen()
