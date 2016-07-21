from random import *


board = [["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"]]
board[int(randrange(4))][int(randrange(4))]= "X"
board[int(randrange(4))][int(randrange(4))] = "S" 
def setup():

    size(500, 500)
    
    for i in range(len(board)):
        for j in range(len(board)):
            rect(i*100, j*100, 100, 100)
    
def draw(): 
    img = loadImage("notbad.jpg")
    
    print (board)
    
    if mouseButton==LEFT:
        xPos = int(mouseX/100)
        yPos = int(mouseY/100)
        fill (255,10, 30) 
        rect(xPos*100, yPos*100, 100, 100)

        
        if board[xPos][yPos] =="X":
            textSize(32)
            fill(randrange(255),randrange(255),randrange(255)) 
            rect(xPos*100,yPos*100,100,100)
            text("One more soldier",100,100)
            
            
        if board[xPos][yPos] == "S":
            fill(0)
            background(0)
            fill(255)
            textSize(32)
            image(img,1,1)
        
            fill(randrange(255))
            text("Good job soldier!",100,100)
            fill(randrange(255),randrange(255),randrange(255)) 
            rect(xPos*100,yPos*100,100,100)
            textSize(36)
            text("You win!",30,30)
        elif board[xPos][yPos] == "0":
            textSize(36)
            text("You miss",30,30)
            

        
        print(mouseX)
        print(mouseY)
    
        
    
        