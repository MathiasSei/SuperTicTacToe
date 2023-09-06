class SmallGameBoard:
    def __init__(self, boardNumb): #Initialises board. Boardnumb sets what small board this should be numbered as inside bigBoard.
        boardNumb = boardNumb * 10
        self._game = [[1+boardNumb, 2+boardNumb, 3+boardNumb],[4+boardNumb, 5+boardNumb, 6+boardNumb],[7+boardNumb, 8+boardNumb, 9+boardNumb]]
        self.showBoard()

    def showBoard(self): #Prints board
        c = 0
        for o in self._game:
            print("|", end="")
            for i in o:
                print(i, end="")
                print("|", end="")
            print()
            if c < 2:
                print("-"*10)
            c += 1
        print("X"*10)

    def playSpace(self, player, space): #Takes player char and places on selected space.
        for y in self._game:
            try: #Finds space in board-array
                arrayX = self._game.index(y)
                arrayY = y.index(space)
            except:
                continue #TODO Error handling when space is taken/not present
            else:
                self._game[arrayX].pop(arrayY) #Removes "space-number"
                self._game[arrayX].insert(arrayY, " " + player) #Insers player char
            self.showBoard() #Prints new board


game1 = SmallGameBoard(2)

game1.playSpace("x", 21)