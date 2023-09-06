class gameBoard:
    def __init__(self, gameNumb):
        self.game = []
        self.gameLog = []
        self._moves = 0
        self._gameOn = True
        gameNumb = gameNumb * 10
        for i in range(1, 10):
            self.game.append(i + gameNumb)
        self.gameLog.append(self.game)
        self.showBoard()
        self.runGame()

    def showBoard(self):
        x = 0
        print("┌──┬──┬──┐")
        for i in range(3):
            for p in range(3):
                print("│", end="")
                print(self.game[x], end="")
                x += 1
            print("│")
            if i < 2:
                print("├──┼──┼──┤")
        print("└──┴──┴──┘")

    def runGame(self):
        player = "x"
        while self._gameOn == True:
            space = int(input(f"It's {player}'s turn. Pick a space: "))
            if self.playSpace(player, space) == "Invalid":
                print("Invalid input, try again!")
            elif player == "x":
                player = "o"
            else:
                player = "x"


    def playSpace(self, player, space):
        try:
            indexSpace = self.game.index(space)
        except:
            return "Invalid"
        else: 
            self._moves += 1
            self.game.pop(indexSpace)
            self.game.insert(indexSpace, " " + player)
            self.showBoard()
            self.saveMoves()
            self.checkWin()

    def checkWin(self):
        winConditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for i in winConditions:
            if (self.game[i[0]-1] == " x") and (self.game[i[1]-1] == " x") and (self.game[i[2]-1] == " x"):
                print(f"X has three in a row in squares {i}")
                self.gameOver()
                break
            elif (self.game[i[0]-1] == " o") and (self.game[i[1]-1] == " o") and (self.game[i[2]-1] == " o"):
                print(f"O has three in a row in squares {i}")
                self.gameOver()
                break
            elif self._moves >= 9:
                print("No more moves!")
                self.gameOver()
                break
    
    def gameOver(self):
        print("The game is over, thank you for playing!")
        self._gameOn = False

    def saveMoves(self):
        self.gameLog.append(self.game)
        print(self.gameLog) #FIXME Find out why it saves twice in GameLog

        

game1 = gameBoard(1)    