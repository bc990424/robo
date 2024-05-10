import turtle


t1=turtle.Turtle()
t1.width(10)
def cl(x,y):
    global b
    if b:
        b=False
        t1.pu()
    else:
        b=True
        t1.pd()
#t2=turtle.Turtle()
a=turtle.Screen()
b=True
t1.speed(0)
turtle.shape('turtle')
canvas = turtle.getcanvas()

a.onscreenclick(cl)
while True:

    t1.goto(canvas.winfo_pointerx()-975,-canvas.winfo_pointery()+574)


turtle.mainloop()
