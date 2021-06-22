
import turtle

turtle.bgcolor("black")
turtle.pensize(6)
turtle.speed(0)

for i in range(10):
      for colours in["red","cyan","magenta","purple","green","white"]:
            turtle.color(colours)
            turtle.circle(200)
            turtle.left(10)
turtle.hideturtle()
'''
import turtle


win = turtle.Screen()
win.bgcolor("white")

tess = turtle.Turtle()

tess.speed(0)
tess.color("blue")             
tess.pensize(5)                 
offSet=30

def doNextEvent(x,y):

    global offSet
    global win
    tess.forward(20)
    tess.left(1+offSet)
    offSet=offSet-2
    if(offSet<1):
        win.exitonclick()


win.onclick(doNextEvent)
win.listen()
win.mainloop()            
'''
