import turtle
def init():
    window=turtle.Screen()
    window.bgcolor("black")
    #Drawing the R
    l1=turtle.Turtle()
    l1.penup()
    l1.goto(100, 100)
    l1.pendown()
    l1.color("cyan")
    l1.speed(6)
    l1.right(90)
    l1.forward(100)
    l1.left(90)
    l1.circle(50,180)
    l1.left(90)
    l1.forward(200)
    l1.right(180)
    l1.forward(100)
    l1.right(150)
    l1.forward(115)
    #Drawing a dot like
    angie = turtle.Turtle()
    angie.penup()
    angie.goto(-100, -100)
    angie.pendown()
    angie.shape("arrow")
    angie.forward(300)
    angie.color("green")
    angie.circle(20)
    #Drawing the E
    l2=turtle.Turtle()
    l2.penup()
    l2.goto(250, 100)
    l2.pendown()
    l2.color("cyan")
    l2.speed(6)
    l2.right(90)
    l2.forward(200)
    l2.left(90)
    for i in range(0,2):
     l2.forward(100)
     l2.right(180)
     l2.forward(100)
     l2.right(90)
     l2.forward(100)
     l2.right(90)
    l2.forward(100)
    #drawing a flower
    fl= turtle.Turtle()
    fl.penup()
    fl.goto(-200, 100)
    fl.pendown()
    fl.shape("arrow")
    fl.color("cyan")
    fl.speed(20)
    for i in range(1,37):
     fl.right(10)
     fl.circle(70)
    flo=turtle.Turtle()
    flo.penup()
    flo.goto(-200, -10)
    flo.pendown()
    flo.color("green")
    flo.right(90)
    flo.forward(300)
   
    

init()
