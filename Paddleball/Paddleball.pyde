'''static rectangle
mouse imput to move it
'''
from random import *
xpos = 50#randrange(470) 
ypos = 50#randrange(470)
dir= randrange(1,4)
dir2=randrange(1,4)
#xnegspeed=0
#ynegspeed=0
def setup():
    size(500,500)
    ellipse(xpos, ypos,50,50)
    #background(0)
    
def draw():
    global xpos
    global ypos
    global dir
    global dir2
   
    background(200)
    fill(0,0,0)
    #fill(randrange(255),randrange(255),randrange(255))
    

    if xpos < 10  or xpos > 497:
        dir = dir * -1
    xpos+=dir
    #ellipse(xpos, ypos,50,50)
    #two different dir
    
    if ypos < 10: #or ypos > 450:
        dir2 = dir2 * -1
        
    print(ypos, xpos, mouseX)
    if ypos>=400 :
        if xpos >mouseX and xpos<mouseX + 110:
            dir2=dir2* -1
  
    ypos+=dir2
    ellipse(xpos, ypos, 50,50)
    rect(mouseX,450,110,20)
    #if ypos ==443:
    #    dir2=dir2* -1
    
  
    