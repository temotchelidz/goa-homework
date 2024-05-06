from turtle import *

width(7)
speed(7)

#square
color("red")
forward(150)
left(90)

forward(150)
left(90)

forward(150)
left(90)

forward(150)
left(90)
#end


#door
color("red")
forward(50)
left(90)
begin_fill()

forward(70)
right(90)

forward(50)
right(90)
forward(70)
end_fill()
#end 


#triangle
color("red")
penup()
goto(150,150)
right(150)
begin_fill()
pendown()
forward(150)

left(120)
forward(145)
end_fill()
#end


#window
color("blue")
penup()
goto(90,90)
pendown()

left(120)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)
 


color("blue")
penup()
goto(60,90)
pendown()

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)
#end






exitonclick()