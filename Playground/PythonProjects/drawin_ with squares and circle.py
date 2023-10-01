from turtle import 

shape("turtle")

color('blue')
def square(length):
     for i in range (0, 4):
         forward(length)
         left(90)
         
square(60)
color('red')
square(100)
color('green')
square(150)

right(180)
color('blue')
square(60)
color('red')
square(100)
color('green')
square(150)

right(45)
forward(150)
color('purple')
circle(40)
color('green')
back(300)
color('purple')
right(180)
circle(40)

done()