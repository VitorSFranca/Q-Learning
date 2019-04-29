from copy import deepcopy

class RewardsTable:

    def setGoalReward(self, row, column, rewardValue):
        if(row - 1 > 0):
            self.table[column][row-1][0] = rewardValue #UP
        if(column - 1 > 0):
            self.table[column-1][row][1] = rewardValue #RIGHT
        if(row + 1 < len(self.table[0])):
            self.table[column][row+1][2] = rewardValue #DOWN
        if(column + 1 < len(self.table)):
            self.table[column+1][row][3] = rewardValue #LEFT

    def setRewardValue(self, row, column, movement):
        self.table[column][row][movement] = 100

    def updateRewardValue(self, row, column, movement):
        tableToGetmax = [0] * self.nPossibleActions
        if(movement == 0):
            tableToGetmax = self.table[column][row+1]
        if(movement == 1):
            tableToGetmax = self.table[column+1][row]
        if(movement == 2):
            tableToGetmax = self.table[column][row-1]
        if(movement == 3):
            tableToGetmax = self.table[column-1][row]
        
        self.table[column][row][movement] = self.gamma * max(tableToGetmax)

    def printTable(self):
        print(self.table)

    def getRewardValue(self, row, column, movement):
        try:
            return self.table[column][row][movement]
        except:
            print('Error')
            print(str(column), str(row), str(movement))
            exit()


    def __init__(self, nRows, nColumns, nPossibleActions, gamma):
        self.gamma = gamma
        self.nPossibleActions = nPossibleActions
        
        self.table = []
        for column in range(nColumns):
            self.table.append([])
            for row in range(nRows):
                self.table[column].append([0,0,0,0])
