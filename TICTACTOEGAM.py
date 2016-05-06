from turtle import*
width(5)
tracer(0)
turn="x"
canvas=getcanvas()
canvas.config(cursor="X_cursor")
from ttt import*
from tkinter import messagebox
win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
winref=[ "Win_NW_NE" ,"Win_W_E" ,"Win_SW_SE" ,"Win_NW_SW" ,"Win_N_S" ,"Win_NE_SE" ,"Win_NW_SE" ,"Win_NE_SW"]
boardReference=["NorthWest", "North", "NorthEast", "West", "Center", "East", "SouthWest", "South", "SouthEast"]







def tictactoe():
        penup()
        color("black")
        speed(20)
        setposition (-300,-100)
        setheading (0)
        pendown()
        forward(600)

        penup()
        setposition (-300,100)
        setheading(0)
        pendown()
        forward(600)

        penup()
        setposition(-100,300)
        setheading (-90)
        pendown()
        forward(600)

        penup()

        setposition(100,300)
        setheading(-90)
        pendown()
        forward(600)
        hideturtle()

        update()
def line(foshie):
    socratieswithsunglassesbruhh=win[winref.index(foshie)]
    print(win[winref.index(foshie)][0])
    runningthroughthesixwithmywoes=boardReference[socratieswithsunglassesbruhh[0]]
    dog=boardReference[socratieswithsunglassesbruhh[2]]
    penup()
    x, y = square_to_point(runningthroughthesixwithmywoes)
    goto(x, y)
    pendown()
    x, y = square_to_point(dog)
    goto(x, y)
    update()



def point_to_square(x,y):
        if  -300 <= x <= -100:
                if -300 <= y <= -100:
                        return "SouthWest"
                if -100 <= y <= 100:
                        return "West"
                if 100 <= y <= 300:
                        return "NorthWest"
        if  -100 <= x <= 100:
                if -300 <= y <= -100:
                        return "South"
                if -100 <= y <= 100:
                        return "Center"
                if 100 <= y <= 300:
                        return "North"
        if  100 <= x <= 300:
                if -300 <= y <= -100:
                        return "SouthEast"
                if -100 <= y <= 100:
                        return "East"
                if 100 <= y <= 300:
                        return "NorthEast"


def square_to_point(square):
        if square =="SouthWest":
                return (-200,-200)
        if square == "South":
                return (0,-200)
        if square == "SouthEast":
                return (200,-200)
        if square == "West":
                return (-200,0)
        if square == "Center":
                return (0,0)
        if square == "East":
                return (200,0)
        if square == "NorthWest":
                return (-200,200)
        if square == "North":
                return (0,200)
        if square == "NorthEast":
                return (200,200)


def drawX(square):
        x, y = square_to_point(square)
        color("blue")
        penup()
        goto(x,y)
        pendown()
        setheading(45)
        forward(70)
        backward(140)
        forward(70)
        right(90)
        forward(70)
        backward(140)
        forward(70)

        update()

def drawO(square):
        x,y = square_to_point(square)
        penup()
        color("red")

        setheading(0)
        goto (x,y-70)
        pendown()
        circle(70)

        update()


def mouse_click(x,y):
    location=point_to_square(x,y)
    print (location)
    player=current_player()
    returnvalue=move(location)
    if returnvalue == True:
        if player=="O":
            drawO(point_to_square(x,y))
            canvas.config(cursor="X_cursor")
        else:
            drawX(point_to_square(x,y))
            canvas.config(cursor="circle")

        winter,vape = check_status()
        if vape != "Draw" and vape != "Playing":
            line(vape)
            messagebutch(player)
        if vape=="Draw" :
            messagebutch(None)





def messagebutch(winner):
    if winner== "O":
        winnnnnn="O won becase X sucks"
    elif winner=="X":
        winnnnnn="X wins way to much"
    elif winner== None:
        winnnnnn="_nohbodi wins"
    if messagebox.askyesno(winnnnnn,"DO YOU WANT TO PLAY AGAIN?"):
        clear()
        initialize_board()
        tictactoe()

    else:
        bye()












onscreenclick(mouse_click)

def switchToO():
        global turn
        turn="o"
        canvas.config(cursor="circle")

def switchToX():
        global turn
        turn="x"
        canvas.config(cursor="X_cursor")


onkeyrelease(switchToO, "o")
onkeyrelease(switchToX, "x")





listen()


tictactoe()


done()
