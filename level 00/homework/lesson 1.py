from turtle import *

#we want to paint a house


#step 1:   draw a square
shape("turtle")
width(7)
begin_fill()
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door


begin_fill()
forward(70)
color("yellow")
left(90)
forward(100)     #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

#drawing the roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing the first window

color("green")
left(30)
forward(30)
color("black")
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(50)

#drawing the second window

forward(5)
color("green")
forward(145)
left(90)
forward(25)
color("black")
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(50)
hideturtle()




exitonclick()