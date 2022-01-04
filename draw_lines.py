import turtle
sc=turtle.Screen()
trtl=turtle.Turtle()
 
# method to draw y-axis lines
def drawy(val):
     
    # line
    trtl.forward(800)
     
    # set position
    trtl.up()
    trtl.setpos(val,800)
    trtl.down()
     
    # another line
    trtl.backward(800)
     
    # set position again
    trtl.up()
    trtl.setpos(val+40,-800)
    trtl.down()
     
# method to draw y-axis lines
def drawx(val):
     
    # line
    trtl.forward(800)
     
    # set position
    trtl.up()
    trtl.setpos(800,val)
    trtl.down()
     
    # another line
    trtl.backward(800)
     
    # set position again
    trtl.up()
    trtl.setpos(-800,val+40)
    trtl.down()
     
# method to label the graph grid

 
# Main Section
# set screen
sc.setup(800,800)   
 
# set turtle features
trtl.speed(100)
trtl.left(90)
trtl.up()
trtl.goto(-800, -800) 
trtl.color('lightgreen')
 
# y lines
for i in range(-20,20):
    drawy(40*(i+1))
 
# set position for x lines
trtl.right(90)
trtl.up()
trtl.setpos(-400,-400)
trtl.down()
 
# x lines
for i in range(-20,20):
    drawx(40*(i+1))
 
# axis

# labeling

 
# hide the turtle
trtl.hideturtle()