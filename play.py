from graphics import *
from bs import *
from player import *
from ai import *
import random

def play():
    newgame=True
    while newgame:
        board=Board()
        player=Player('player',False)
        ai=AI()
        board.shipPlacement(player,ai)
        Winner=None
        players=[player,ai]
        players.shuffle()
        current=1
        while Winner==None:
            board.move(players[current],players[current-1])
            if checkLoss(players[current-1]):
                Winner=players[current]
            current+=1
            if current==2:
                current=0
        board.end()
        win=GraphWin("Winner",300,300)
        t=Text(Point(150,150),Winner.name+" wins!!!")
        win.getMouse()
        win.close()
        win=GraphWin("Play again?",300,300)
        t=Text(Point(150,100), "Play again?")
        b1=Square(Point(100,200),25)
        yes=Text(Point(100,200),"Yes")
        b2=Square(Point(200,200),25)
        no=Text(Point(200,200),"No")
        click=win.getMouse()
        while not b1.checkMouseClick(click) and not b2.checkMouseClick(click):
            click=win.getMouse()
        if b2.checkMouseClick(click):
            newgame=False
        win.close()
def checkLoss(p):
    return p.ships==[]
play()
