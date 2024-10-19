import turtle as t

t.fillcolor("red") # SELECT COLOR
t.begin_fill() # START FILLING COLOR

for i in range(4):
    t.left(90)
    t.forward(50)

t.end_fill() # END FILLING COLOR

t.penup()
t.left(90)
t.forward(50)
t.left(35)
t.pendown()

t.fillcolor("blue") # Add
t.begin_fill() # Add

t.forward(45)
t.left(110)
t.forward(45)

t.end_fill() # Add


t.exitonclick()
