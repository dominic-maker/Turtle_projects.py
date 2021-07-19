import turtle
import collections
var_dict = {}
var_dict = collections.OrderedDict(sorted(var_dict.items()))

t = turtle.pen()
turtle.bgcolor("black")
colors = ["peru", "ivory", "dark orange", "cyan", "coral", "hot pink", "gold", "red", "green", "yellow", "ivory",
          "blue", "light blue", "green"]
my_name = turtle.textinput("Tech", "what is your name?")
sides = int(turtle.numinput("number of sides", "How many sides do you want(1 -10)?"), 5, 1, 10)
for x in range(100):
    t.pencolor(colors[x % sides % 10])
    t.penup()
    t.forward(x+4)
    t.pendown()
    t.write(my_name, font=("Arial", int(x=x*2+4)/4))
    t.left(360/sides+2)

