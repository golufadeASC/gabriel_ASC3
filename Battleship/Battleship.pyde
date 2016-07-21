from random import randint
from random import *
global board
global i
global x
global y

board= [[1,0,0,0,0],[1,1,0,0,0],[0,0,1,0,0]]
x=0
y=0
i=0
for i in range(5):
        board.append(["0"]*5)
board[randint(0, len(board) - 1)][randint(0, len(board[0]) - 1)]="x"
        #board[range(0,6)][range(0,6)]= "x"
        


def setup():
    size(500,500)
    

def draw():
    
    def square(x):
        x=0
        while x < 400:
            x=x+100
            print("u")
            rect(x,y,100,100)
            rect(0,0,100,100)
            
    square(x)
    
    def square(y):
        y=0
        while y< 400:
            y=y+100
            rect(x,y,100,100)
            rect(0,0,100,100)
    square(y)
    
    def square(xy):
        while y<400 and x =100:
            y=y+100
            x=100
            rect(x,y,100,100)
            rect(x,0,100,100)
    
    

    