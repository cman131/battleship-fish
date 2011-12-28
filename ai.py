"""
Complete the shipPlacement, move, and moveInfo.
Add any slots, variables, functions or so that you want.
(any positions should be like this: E5)
"""

from board import Ship

class AI():
    __slots__=('name', 'ships', 'board')
    def __init__(self,name):
        self.ships=[Ship('Cruiser'),Ship('Battleship'),Ship('Submarine'),Ship('Cruiser'),Ship('FishBoat')]
        self.name=name
        self.board=None
    def sunkShip(ship):
        self.ships.remove(ship)
        print 'You sunk my '+ship.name
    def shipPlacement(self):
        """We need this class to decide and place the ships
        accordingly in your representation of the board.
        After that call ship.place(position, rotation) on each ship and
        then return the new ships list"""
        
        return self.ships
    def move(self):
        """This should decide, modify the board,
        and then return the move as a string. ex: E5 or H2"""
        pass
    def moveInfo(self,pos):
        """This will be called when the other player makes a move.
        pos is the coordinates of the move. To check if a ship is sunk
        call ship.checkSunk(). if a ship is sunk call self.sunkShip"""
        pass
    def checkHit(self,pos):
        """returns true or false depending on whether or not there is a ship
        at coordinate pos"""
        for ship in self.ships:
            if pos in ship.pos:
                ship.hits+=1
                return True
        return False
