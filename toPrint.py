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

            # check the cell to see if a piece is there
            if cell.piece != "":
                # if it is an opponent piece, we may be able to move
                # next to it
                if self.whoMove != cell.piece:

                    # check all directions to see if any space next
                    # to it is available to play
                    for d in directions:
                        # check that the opponent piece is within
                        # columns 1-6 OR the direction we are looking at
                        # is up or down
                        if (((i%8 != 0) and (i%8 != 7)) or (d[0] == 0)):
                            # check that the opponent piece is within
                            # rows 1-6 OR that the direction we are looking
                            # at is left or right
                            if (((i > 7) and (i < 56)) or (d[1] == 0)):
                                
                                # set the index of possible move to be
                                # the index of the opponent piece +
                                # the direction. This converts it to
                                # the corresponding index in our list of
                                # 64 cells
                                newInd = i + d[0] + d[1]

                                # check that this new index is within 0-63
                                if 0 <= newInd < 64:
                                    # check that this potential cell is empty
                                    if self.cells[newInd].piece == "":

                                        # check to see if the move can be played
                                        # which requires your own piece at the
                                        # end of consecutive opponent pieces
                                        # in the corresponding direction
                                        # assume not possible
                                        checkForValid = False
                                        pos = i

                                        # loop for the maximum amount of spaces
                                        # away your own piece could be
                                        for j in range(6):
                                            # check pieces in the direction opposite
                                            # to where you potential move is
                                            pos = pos - d[0] - d[1]
                                            
                                            # if the check moves outside of the 64 cells
                                            # it is invalid
                                            if (63 < pos):
                                                break
                                            elif (pos < 0):
                                                break
                                            # if an empty cell is found first, it is invalid
                                            elif self.cells[pos].piece == "":
                                                break
                                            
                                            # if your own piece is found first, it is valid
                                            elif self.cells[pos].piece == self.whoMove:
                                                checkForValid = True
                                                break
                                            
                                            # if check the first or last column AND we are not
                                            # moving up or down, it is invalid
                                            # same for first or last row and not moving L/R
                                            elif ((pos%8 == 0) or (pos%8==7)) and (d[0] != 0):
                                                break
                                            elif ((pos<8) or (pos>55)) and (d[1] != 0):
                                                break
                                            
                                        # if a valid move was found, add it to the list.    
                                        if checkForValid:
                                            moves.append(self.cells[newInd])
        # highlight all valid moves found
        for m in moves:
            m.highlight()
        
        return moves
