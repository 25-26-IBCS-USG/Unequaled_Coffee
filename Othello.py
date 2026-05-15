from graphics import*
from KendylOBoard import*
from Cell import*
from Button import*

def initialPieces(cb):

    # initialize the board state to have the first 4 pieces
    cb.cells[27].updatePiece("white")
    cb.cells[28].updatePiece("black")
    cb.cells[35].updatePiece("black")
    cb.cells[36].updatePiece("white")

def main():

    win = GraphWin("Othello", 1000, 800)
    # create the othello board
    ob = OBoard(win)

    # create buttons to play the game
    quiButton = Button(win, "Exit", 60, Point(870, 220))
    passButton = Button(win, "PASS", 60, Point(870, 500))
    turnT = Text(Point(850, 620), "white plays")
    turnT.draw(win)
    multiButton = Button(win, "Multiplayer", 60, Point(850, 420))
    blackButton = Button(win, "Black", 60, Point(850, 300))
    whiteButton = Button(win, "White", 60, Point(850, 360))
    startT = Text(Point(850, 100), "START")
    startT.draw(win)
    checkT = Text(Point(850,550), "")
    checkT.draw(win)

    player = 1
    player2 = 0
    AI = 0

    # wait for player to choose how to play the game
    while True:
        m1 = win.getMouse()
        if quiButton.isClicked(m1):
            win.close()
            exit()

        if multiButton.isClicked(m1):
            player2 = 2
            break

        if whiteButton.isClicked(m1):
            player = 2
            AI = 2
            break

        if blackButton.isClicked(m1):
            AI = 1
            break

    # reset the board state
    startT.setText("RESTART")
    for i in range(64):
        ob.cells[i].empty()

    # initialize the board state
    ob.setWhoMove("black")
    turnT.setText(ob.whoMove + " plays")
    initialPieces(ob)

    over = 0

    # take turns to play the game
    while True:
        turnT.setText(ob.whoMove + " plays")
        
        # AI move by finding all possible moves and choosing
        # the 'best' one of them
        # this code runs if AI moves first
        if AI == 1:
            AImov = ob.checkMoves()
            if len(AImov) == 0:
                over += 1
                ob.changeT()
            else:
                choice = ob.findBestMove(AImov)
                ob.place(choice)
                over = 0
                for m in AImov:
                    m.unHighlight()

        mov = ob.checkMoves()
        turn = True
        while turn:
            # player's turn to click on one of the possible moves
            m1 = win.getMouse()
            if quiButton.isClicked(m1):
                win.close()
                exit()

            if passButton.isClicked(m1):
                over += 1
                ob.changeT()
                turn = False
                if (over == 2):
                    turnT.setText(ob.whoMove + " has no moves. game over")
                    print(ob.calcScore())
                    break      

        #Normal situation for a player turn
            for c in mov:
                if c.isClicked(m1):
                    ob.place(c)
                    over = 0
                    turn = False
                    break
            if not turn:
                for c in mov:
                    c.unHighlight()
                    
        # this code runs if AI moves second
        if AI == 2:
            AImov = ob.checkMoves()
            if len(AImov) == 0:
                over += 1
                ob.changeT()
            else:
                choice = ob.findBestMove(AImov)
                ob.place(choice)
                over = 0
                for m in AImov:
                    m.unHighlight()

        if (over == 2) or (ob.isOver()):
            turnT.setText(ob.whoMove + " has no moves. game over")
            print(ob.calcScore())
            break
            
                    

if __name__ == "__main__":
    main()
