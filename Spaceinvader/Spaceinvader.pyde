x=0
y=450
bullet=False
from random import *

def setup():
    size(600,600)

def draw():
    global bullet
    background(255,255,255)
    global x
    global y
    rect(x,450,100,20)
    line(x+50, y,x+50,y-30)
    if bullet==True:
        y-=10   
        if y<10:
            y = 450
            bullet=False
    

    
    
#ship
def keyPressed():
    global x
    global y
    global bullet

    if keyCode==39 and x<478:
        x+=20
        #left
    elif keyCode==37 and x>30:
        x-=20
    #bullet #(x, value+ constant num, x, other value + constant num)
    if keyCode==32:
        bullet=True

        '''if y<0:
                bullet=False
                bullet = 500
                print("hi")'''
'''keyPressed()
keyPressed()'''
        
               # if y<10:
                 #   bullet=False
            
    #keyCode==32:
            
          #  print("g")'''
       
           
    
#bullet
    #(x, value+ constant num, x, other value + constant num)
'''def bullet():
    if keyCode==38:
        print("g")
        line(x, 450,x,450-30)
        print("shoot")
press spacebar and show bullet decresing y value of bullet
, stop bullet where aliens at,define x and y