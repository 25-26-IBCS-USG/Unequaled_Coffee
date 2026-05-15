from Button import*
from Cell import*

class OBoard():

    def __init__(self, win):
        # initialize the board as 64 cells. List of 64 cells with
        # coordinates (0,0) to (7,7). Cells go left to right, then down
        self.cells = []
        for i in range(8):
            for j in range(8):
                # 'even' cells are white and odd are grey to demonstrate
                # checkered pattern
                if (i+j)%2 == 0:
                    color = "LightGreen"
                else:
                    color = "MediumSeaGreen"
                # add a cell object to the list of 64
                # this cell is being initialized with its coordinates
                # and its color
                self.cells.append(Cell(win, (j, i), color))
                
        # initialize the board state with a list of potential moves
        # and whose turn it is
        self.potentMoves = []
        self.whoMove = "black"

    # method for setting whose turn it is first
    def setWhoMove(self, pl):
        self.whoMove = pl

    # method for changing whose turn it is
    def changeT(self):
        if self.whoMove == "black":
            self.whoMove = "white"
        else:
            self.whoMove = "black"

    # method to access the list of potential moves
    def getPotentMoves(self):
        return self.potentMoves

    # method to get the list of 64 cells
    def getAllCells(self):
        return self.cells

    # method to check if the game is over by seeing if all cells
    # are filled. This should also check potential move list for
    # both players...
    def isOver(self):
        for c in self.cells:
            if c.piece == "":
                return False
        return True

    # method to calculate who won after the game is over
    def calcScore(self):
        b = 0
        w = 0
        for c in self.cells:
            if c.piece == "black":
                b+=1
            if c.piece == "white":
                w+=1
        return "black: " + str(b) + " -- white: " + str(w)

    # method for basic AI (pick first possible move)
    # definitely not AI at all
    def findBestMove(self, moves):
        if not moves:
            return None

        #Score Chart
        points = [
            100, 0,  50,   10,   10,  50, 0, 100,
            0, 0,  5,  5,  5,  5, 0, 0,
            50,  5,   5,   1,   1,   5,  5,  50,
            10,  5,   1,   0,   0,   1,  5,   10,
            10,  5,   1,   0,   0,   1,  5,   10,
            50,  5,   5,   1,   1,   5,  5,  50,
            0, 0,  5,  5,  5,  5, 0, 0,
            100, 0,  50,   10,   10,  50, 0, 100
            ]
        
        bestScore = -float('inf')
        bestMove = moves[0]
        
    #loop through all the moves to see them
        for m in moves:
            ind = self.cells.index(m)
            score = 0
            #check for a corner
            score = points[ind]
          
               
            if score > bestScore:
                bestScore = score
                bestMove = m
                
        return bestMove

    # method for creating a list of all possible moves    
    def checkMoves(self):
        # initialize list
        moves = []

        # initialize 8 possible directions to check
        UL = [-1, -8]
        U = [0, -8]
        UR = [1, -8]
        L = [-1, 0]
        R = [1, 0]
        DL = [-1, 8]
        D = [0, 8]
        DR = [1, 8]
        directions = [UL, U, UR, L, R, DL, D, DR]

        # loop through all 64 cells
        for i in range(64):
            cell = self.cells[i]

            # check the cell has opponent piece
            if cell.piece != "":
                if self.whoMove != cell.piece:

                    # check all directions to see if any space
                    # next to it is available to play
                    for d in directions:

                        # check that the opponent piece is within
                        # columns 1-6 OR the direction we are looking at
                        # is up or down
                        if (((i%8 != 0) and (i%8 != 7)) or (d[0] == 0)):

                            # check that the opponent piece is within
                            # rows 1-6 OR that the direction  we are looking
                            # at is left or right
                            if (((i > 7) and (i < 56)) or (d[1] == 0)):

                                # set the index of possible move to be
                                # the index of the opponent piece +
                                # the direction
                                newInd = i + d[0] + d[1]

                                # check that the new index is withing 0-63
                                if 0 <= newInd < 64:

                                    # check that the cell is empty
                                    if self.cells[newInd].piece == "":

                                        # check to see if the move can be played
                                        # which requires your own piece at the
                                        # end of consecutive opponent pieces
                                        # in the corresponding direction
                                        # ASSUME it is not possible
                                        checkForValid = False
                                        pos = i

                                        # loop for the maximum amount of spaces
                                        # away our piece could be
                                        for j in range(6):

                                            # check pieces in the direction opposite
                                            # to our potential move
                                            pos = pos - d[0] - d[1]

                                            # if the check moves outside of the 64 cells
                                            # it is invalid
                                            if (pos > 63):
                                                break
                                            elif (pos < 0):
                                                break

                                            # if an empty cell is found first
                                            # it is invalid
                                            elif self.cells[pos].piece == "":
                                                break

                                            # if your own piece is found first
                                            # it is VALID
                                            elif self.cells[pos].piece == self.whoMove:
                                                checkForValid = True
                                                break

                                            # if check the first or last column AND we
                                            # are not moving up or down it is invalid
                                            # same for first or last row
                                            elif ((pos%8 == 0) or (pos%8 == 7)) and (d[0] != 0):
                                                break
                                            elif ((pos<8) or (pos>55)) and (d[1] != 0):
                                                break

                                        # if a valid move was found, add it to the list
                                        if checkForValid:
                                            moves.append(self.cells[newInd])
                

        # highlight all valid moves
        for m in moves:
            m.highlight()
        
        return moves

    # method to place a move and flip all necessary pieces' colors
    def place(self, c):
        # place your own piece on the cell
        c.updatePiece(self.whoMove)

        # initiate list of pieces to flip
        toFlip = []
        ind = self.cells.index(c)
        UL = [-1, -8]
        U = [0, -8]
        UR = [1, -8]
        L = [-1, 0]
        R = [1, 0]
        DL = [-1, 8]
        D = [0, 8]
        DR = [1, 8]
        directions = [UL, U, UR, L, R, DL, D, DR]

        # iterate through the 8 directions similar to checking moves
        # note that more than one direction may have pieces to flip
        for d in directions:
            newInd = ind + d[0] + d[1]

            # initiate a temporary 'toFlip' list
            tempFlip = []
            for i in range(7):

                # do not flip any pieces if you reach the end of a row
                # while moving left or right
                if (newInd%8 == 7) and (d[0] == -1):
                    break
                if (newInd%8 == 0) and (d[0] == 1):
                    break

                # check that the potential cell to flip is within the
                # 64 possible cells
                if 0 <= newInd < 64:
                    # if an opponent piece is found, at it to the temporary list
                    if (self.cells[newInd].piece != self.whoMove) and (self.cells[newInd].piece != ""):
                        tempFlip.append(newInd)
                    # if your own piece is found, stage the temporary flips
                    # in the current direction to be ready to get flipped
                    elif (self.cells[newInd].piece == self.whoMove):
                        for t in tempFlip:
                            toFlip.append(t)
                        break
                    # if an empty cell is found, break and do not flip any
                    # in that direction
                    else:
                        break
                    
                    # continue to move in the current direction otherwise
                    newInd = newInd + d[0] + d[1]

        # flip all pieces in the 'toFlip' list
        if self.whoMove == "black":
            change = "white"
        else:
            change = "black"
        for f in toFlip:
            self.cells[f].updatePiece(self.whoMove)
        self.whoMove = change
        
            
        
            
            


