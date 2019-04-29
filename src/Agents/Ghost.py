from src.Agents.Agent import Agent
import random

class Ghost(Agent):

    def setPacmanCatched(self):
        self.catchPacman = True
        print(str(self.goals) + ' - ' + str(self.nMoves) + ' movements')
        self.nMoves = 0
        self.goals += 1
        self.row = self.initialRow
        self.column = self.initialColumn

        self.rewardsTable.setRewardValue(self.oldGhost.getRow(), self.oldGhost.getColumn(), self.lastMovement)

    def setRow(self, row):
        self.row = row

    def setColumn(self, column):
        self.column = column

    def setOldGhost(self):
        self.oldGhost = Ghost(self.row, self.column, 'g')

    def getOldGhost(self):
        return self.oldGhost

    def getRandomMove(self):
        return random.randint(0, self.nPossibleActions - 1)

    def getBestMovement(self):
        bestMove = self.getRandomMove()
        movement = 0
        for movement in range(self.nPossibleActions):
            if(self.rewardsTable.getRewardValue(self.row, self.column, movement) > self.rewardsTable.getRewardValue(self.row, self.column, bestMove)):
                bestMove = movement
        return bestMove

    def move(self):
        self.oldGhost.setRow(self.row)
        self.oldGhost.setColumn(self.column)

        if(random.randint(0,100) < 2):
            direction = self.getRandomMove()
        else:
            direction = self.getBestMovement()
        
        self.lastMovement = direction

        if(direction == 0 and self.row < self.rowLimit - 1): # UP
            self.rewardsTable.updateRewardValue(self.row, self.column, direction)
            self.nMoves += 1
            self.row += 1
        elif(direction == 1 and self.column < self.columnLimit - 1): # RIGHT
            self.rewardsTable.updateRewardValue(self.row, self.column, direction)
            self.nMoves += 1
            self.column += 1         
        elif(direction == 2 and self.row > 0): # DOWN
            self.rewardsTable.updateRewardValue(self.row, self.column, direction)
            self.nMoves += 1
            self.row -= 1 
        elif(direction == 3 and self.column > 0): # LEFT
            self.rewardsTable.updateRewardValue(self.row, self.column, direction)
            self.nMoves += 1
            self.column -= 1
        else:
            self.move()

    def __init__(self, row, column, color, nPossibleActions = 4, rowLimit = 10, columnLimit = 10, rewardsTable = None):
        self.initialRow = row
        self.initialColumn = column
        self.row = row
        self.column = column
        self.color = color
        self.catchPacman = False
        self.nPossibleActions = nPossibleActions
        self.rowLimit = rowLimit
        self.columnLimit = columnLimit
        self.rewardsTable = rewardsTable
        self.goals = 0
        self.nMoves = 0