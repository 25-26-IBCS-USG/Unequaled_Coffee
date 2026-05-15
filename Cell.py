from graphics import*

class Cell():

    def __init__(self, win, coord, color):
        self.win = win
        self.coord = coord

        # convert cell coordinate (0-7, 0-7) to the pixels on the window
        self.minX = coord[0]*(win.getWidth()/8) - 300*coord[0]/8 + 50
        self.minY = coord[1]*(win.getHeight()/8) - 100*coord[1]/8 + 50
        self.maxX = self.minX + (win.getWidth() - 300)/8
        self.maxY = self.minY + (win.getHeight() - 100)/8

        # initiate the cell of the Othello board as a rectangle
        self.r = Rectangle(Point(self.minX, self.minY), Point(self.maxX, self.maxY))
        self.r.setFill(color)
        self.r.setOutline("black")
        self.r.draw(win)

        # initiate the circle to draw a piece (but do not draw it yet)
        self.circ = Circle(Point((self.maxX + self.minX)/2, (self.maxY + self.minY)/2), 40)

        # initial cells will be empty (no piece) and not be highlighted
        self.piece = ""
        self.highlighted = False

    # cells are functioning like buttons... perhaps should inherit from button
    def isClicked(self, p):
        x = p.getX()
        y = p.getY()
        if x > self.minX:
            if x < self.maxX:
                if y > self.minY:
                    if y < self.maxY:
                        return True
        return False

    # method for highlighting the cell
    def highlight(self):
        self.r.setOutline("blue")
        self.r.setWidth(8)
        self.highlighted = True

    # method for unhighlighting the cell
    def unHighlight(self):
        self.r.setOutline("black")
        self.r.setWidth(1)
        self.highlighted = False

    # method to place the color of the piece in the cell
    def updatePiece(self, piece):
        # change the piece to be whatever color is in the parameter
        self.piece = piece
        if self.piece == "black":   
            self.circ.setFill("black")
        else:
            self.circ.setFill("white")
        # undraw before drawing because the piece may have already had
        # a circle drawn in the cell
        self.circ.undraw()
        self.circ.draw(self.win)
        
    # accessor for the cell's coordinates
    def getCoord(self):
        return self.coord

    # method for resetting a cell
    def empty(self):
        self.piece = ""
        self.circ.undraw()

            
            
        
