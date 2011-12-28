from graphics import *
class Board():
    def __init__(self):
        win=GraphWin("Battle Ship", 675, 675)
        win2=GraphWin("Radar", 675, 675)
        let=['H','G','F','E','D','C','B','A']
        for i in range(1,10):
            l=Line(Point(0,i*75),Point(675,i*75))
            l2=Line(Point(i*75,0),Point(i*75,675))
            if i!=9:
                t=Text(Point((75/2)+(i*75),675-(75/2)), str(i))
                t.draw(win)
                t.draw(win2)
            if let !=[]:
                t2=Text(Point(75/2,((i-1)*75)+(75/2)), let.pop())
                t2.draw(win)
                t2.draw(win2)
            l.draw(win)
            l.draw(win2)
            l2.draw(win)
            l2.draw(win2)
        self.win=win
        self.radar=win2
    def shipPlacement(self,p1,p2):
        p1Ships=p1.shipPlacement()
        p2.shipPlacement()
        for ship in p1Ships:
            p=Pixmap(ship.pic)
            i=Image(interpret(ship.pos),p)
            i.draw(self.win)
    def move(self,player,other):
        pos=player.move()
        m=Mark(interpret(pos),player2.checkHit(pos))
        if isinstance(player,Player):
            m.draw(self.radar)
        else:
            m.draw(self.win)
        other.moveInfo(pos)
    def end(self):
        self.win.close()
def interpret(pos):
    d={'A':75/2,'B':75+(75/2),'C':150+(75/2),'D':225+(75/2),'E':300+(75/2),'F':375+(75/2),'G':450+(75/2),'H':525+(75/2)}
    if isinstance(pos,List):
        l=len(pos)
        if isEven(l):
            x1=75/2+(75*int(pos[l//2-1][1]))
            x2=75/2+(75*int(pos[l//2][1]))
            y1=d[pos[l//2-1][0]]
            y2=d[pos[l//2][0]]
            x=x1+x1-x2
            y=y1+y1-y2
            return Point(x,y)
        return Point(75/2+(75*int(pos[l//2][1])),d[pos[l//2][0]])
    return Point(75/2+(75*int(pos[1])),d[pos[0]])
def isEven(num):
    if num%2==1:
        return False
    return True
class mark():
    def __init__(self,pos,typ):
        self.rep=Circle(pos,25)
        if typ:
            self.rep.setFill('red')
        else:
            self.rep.setFill('white')
    def draw(self,win):
        self.rep.draw(win)
class ship():
    def __init__(name):
        self.name=name
        self.pic=''
        self.pos=[]
        self.rotation=0
        self.hits=0
        if name=='Carrier' or name=='BlueWhale':
            self.spaces=5
        elif name=='Battleship' or name=='Fin':
            self.spaces=4
        elif name=='Submarine' or name=='Cruiser' or name=='Orca' or name=='Narwhal':
            self.spaces=3
        elif name=='FishBoat' or name=='Sperm':
            self.spaces=2
    def place(self,pos,r):
        self.pos=pos
        self.rotation=r
        self.pic=self.name+str(r)+'.gif'
    def checkSunk(self):
        return self.hits==self.spaces
