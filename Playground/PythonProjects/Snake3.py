import turtle
 
wn = turtle.Screen()
wn.title("Ping pong by Cagatay em")
wn.bgcolor("blue")
wn.setup(width=900, height=600)
wn.tracer(0)  #oyunu hizlandirir silersen cok yavaslar
 
 
class PaddleFirst():
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.shapesize(stretch_wid=5, stretch_len=1)
        self.pen.penup()
        self.pen.goto(-350, 0)
 
    def up(self):
        y = self.pen.ycor()
        y += 20
        self.pen.sety(y)
 
    def down(self):
        y = self.pen.ycor()
        y -= 20
        self.pen.sety(y)
 
 
class PaddleSecond():
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.shapesize(stretch_wid=5, stretch_len=1)
        self.pen.penup()
        self.pen.goto(350, 0)
 
    def up(self):
        y = self.pen.ycor()
        y += 20
        self.pen.sety(y)
 
    def down(self):
        y = self.pen.ycor()
        y -= 20
        self.pen.sety(y)
 
 
 
class Ball():
    def __init__(self):
 
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.speed(0)
        self.pen.shape("Square ")
        self.pen.color("Red")
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.dx = 00.1
        self.pen.dy = 00.1
 
    def letsgo(self):
        self.pen.setx(self.pen.xcor() + self.pen.dx)
        self.pen.sety(self.pen.ycor() + self.pen.dy)
 
    def move(self):
        if self.pen.ycor() > 290:
            self.pen.sety(290)
            self.pen.dy *= -1
 
        if self.pen.ycor() < -290:
            self.pen.sety(-290)
            self.pen.dy *= -1
 
        if self.pen.xcor() > 390:
            self.pen.goto(0, 0)
            self.pen.dx *= -1
 
        if self.pen.xcor() < -390:
            self.pen.goto(0, 0)
            self.pen.dx *= -1
 
 
class Wall():
   def moving(self):
        if ball.pen.xcor() > 340 and (ball.pen.ycor() < paddle2.pen.ycor() + 40 and ball.pen.ycor() > paddle2.pen.ycor() - 40):
           ball.pen.dx *= -1
        if ball.pen.xcor() < -340 and (ball.pen.ycor() < paddle1.pen.ycor() + 40 and ball.pen.ycor() > paddle1.pen.ycor() - 40):
            ball.pen.dx *= -1
 
 
paddle1 = PaddleFirst()
print(paddle1)
paddle2 = PaddleSecond()
print(paddle2)
ball = Ball()
print(ball)
wall = Wall()
 
 
wn.listen()
wn.onkeypress(paddle1.up, "w")
wn.onkeypress(paddle1.down, "s")
wn.onkeypress(paddle2.up, "Up")
wn.onkeypress(paddle2.down, "Down")
 
 
 
while True:
    wn.update() # everytime uptades the screen
    ball.letsgo()
    ball.move()
    wall.moving()