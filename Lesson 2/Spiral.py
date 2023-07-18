import turtle
loadWindow = turtle.Screen()
turtle.speed(0)
 
# loop and create circle
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

#  make the window exit when clicked
turtle.exitonclick()