from random import *

def squarered():
    fill(212,4,4)
    rect(0,0,100,100)
    
def squaregreen():
    fill(0,255,0)
    rect(100,0,100,100)
    
def squareblue():
    fill(0,0,255)
    rect(200,0,100,100)
    
def squareyellow():
    fill(212,212,4)
    rect(300,0,100,100)
    
def squarerainbow():
    fill(randrange(255),randrange(255),randrange(255))
    rect(400,0,100,100)
    

def setup():
    size(600,600)
      
    
def mouseDragged():
    if  mouseButton== RIGHT:
        mouseX < 100
        mouseY < 100
        fill(255,0,0)
    if mouseButton== LEFT:
        mouseX > 100 and mouseX < 200
        mouseY < 100
        fill(0,255,0)
    ellipse(mouseX,mouseY, 8,8)

def draw():
    squarered()
    squaregreen()
    squareblue()
    squareyellow()
    squarerainbow()  
if mouseButton== LEFT:
        if mouseY < 100: 
            if mouseX < 100:
                pick.color=1
                mouseDragged()
            #else mouseY < 200:
                if mouseY > 100:
                    if pick.color==2:
                        fill(0,255,0)
                        mouseDragged()
            
    
print(mouseX,mouseY)    
#check mousebutton == LEFT
# check mouseY < 100
# check mouse x < 100
# pick color 1
# check mouse Y < 200
# check mouseY > 100
# check pick color ==1
# fill(255,0,0)
#mousex,mou