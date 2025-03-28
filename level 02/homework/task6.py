from turtle import *

#we want to paint a castle

# step 1: drawing a square

speed(7)
shape("turtle")
width(7)
begin_fill()
color("grey")
back(150)
left(90)
forward(150)
right(90)
forward(200)
right(90)
forward(150)
right(90)
forward(50)
end_fill()

#end of square

#step 2: drawing a door 

forward(80)
right(90)
begin_fill()
color("chocolate")
forward(85)
right(90)
forward(45)
right(90)
forward(80)
right(90)
forward(45)
end_fill()

#end of drawing a door

#step 3: drawing the Towers

begin_fill()
color("chocolate")
forward(9)
color("grey")
forward(61)
forward(90)
right(90)
forward(290)
right(90)
forward(90)
right(90)
forward(200)
end_fill()

begin_fill()
forward(90)
left(90)
forward(290)
left(90)
forward(290)
left(90)
forward(90)
left(90)
forward(290)
end_fill()
right(90)
forward(80)
begin_fill()
color("chocolate")
forward(50)
right(90)
forward(90)
right(90)
forward(45)
right(90)
forward(90)
end_fill()





hideturtle()






exitonclick()