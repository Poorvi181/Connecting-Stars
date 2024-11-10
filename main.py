import pgzrun,random
from time import time
TITLE="Connecting Stars"
HEIGHT=600
WIDTH=800

stars=[]
linecor=[]

numberofstars=8
countstars=0
starttime=0
totaltime=0
def createstars():
    global starttime
    for i in range(0,numberofstars):
        star=Actor("stars")
        star.pos=random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
        stars.append(star)
    
    starttime=time()
def draw():
    global starttime,totaltime
    screen.blit("space",(0,0))
    number=1
    for star in stars:
        star.draw()
        screen.draw.text(str(number),(star.pos[0],star.pos[1]+30))
        number+=1
    for line in linecor:
        screen.draw.line(line[0],line[1],"white")
    if countstars < numberofstars:
        totaltime=time()-starttime
        screen.draw.text(str(round(totaltime)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(totaltime)),(10,10),fontsize=30)

def on_mouse_down(pos):
    global countstars,linecor,stars,numberofstars
    if countstars < numberofstars:
        if stars[countstars].collidepoint(pos):
            if countstars:
                linecor.append((stars[countstars-1].pos,stars[countstars].pos))
            countstars+=1
        else:
            linecor=[]
            countstars=0
                     

def update():
    pass
createstars()
pgzrun.go()