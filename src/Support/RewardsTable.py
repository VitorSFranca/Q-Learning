from copy import deepcopy

class RewardsTable:

    def generateInterpolateTable(self, nRows, nColumns):
        self.interpolateTable = []
        self.newGeneratedRows = []
        self.newGeneratedColumns = []
        newRows = nRows - len(self.table)
        newColumns = nColumns - len(self.table[0])
        
        genericColumn = [0,0,0,0]
        genericRow = []

        # self.table[0][0] = [1,1,1,1]
        # self.table[0][3] = [2,2,2,2]
        # self.table[3][0] = [3,3,3,3]
        # self.table[3][3] = [4,4,4,4]

        self.table[0] = [[0, 0.0, 0, 0], [0, 0.0, 0.0, 0], [100, 0, 0, 0], [0, 0, 0, 0]]
        self.table[1] = [[0.0, 0.0, 0, 0.0], [0.0, 0.0, 0.0, 0.0], [0, 0, 0.0, 90.0], [0, 0.0, 0, 0]]
        self.table[2] = [[0.0, 0.0, 0, 0.0], [72.9, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 81.0], [0, 0, 72.9, 0.0]]
        self.table[3] = [[59.049000000000014, 0, 0, 0.0], [0.0, 0, 0.0, 65.61000000000001], [0.0, 0, 0, 0], [0, 0, 0, 0.0]]

        for i in range(nColumns):
            genericRow.append(genericColumn)

        # Create empty rows
        for i in range(len(self.table)):
            if(i%2 == 1 and newRows > 0):
                self.interpolateTable.append(deepcopy(genericRow))
                self.interpolateTable.append(self.table[i])
                self.newGeneratedRows.append(len(self.interpolateTable) - 2)
                newRows -= 1
            else:
                self.interpolateTable.append(self.table[i])

        # Create empty columns
        for i in range(len(self.interpolateTable)):
            if len(self.interpolateTable[i]) < nColumns:
                tmpNewColumns = newColumns
                oldRow = self.interpolateTable[i]
                self.interpolateTable[i] = []
                for j in range(len(oldRow)):
                    if(j%2 == 1 and tmpNewColumns > 0):
                        self.interpolateTable[i].append(deepcopy(genericColumn))
                        self.interpolateTable[i].append(oldRow[j])
                        if j not in self.newGeneratedColumns:
                            self.newGeneratedRows.append(len(self.interpolateTable[i]) - 2)
                        tmpNewColumns -= 1
                    else:
                        self.interpolateTable[i].append(oldRow[j])

    def generateInterpolateValues(self):
        for i in range(len(self.interpolateTable)):
            if(i in self.newGeneratedRows):
                for j in range(len(self.interpolateTable[i])):
                    upValue = self.interpolateTable[i+1][j][0] if i <= len(self.interpolateTable) - 1 else 0
                    rightValue = self.interpolateTable[i][j-1][1] if j > 0 else 0
                    downValue = self.interpolateTable[i-1][j][2] if i > 0 else 0
                    leftValue = self.interpolateTable[i][j+1][3] if j <= len(self.interpolateTable[i][0]) - 1 else 0
                    
                    self.interpolateTable[i][j] = [upValue,rightValue,downValue,leftValue]

    def interpolate(self, nRows, nColumns):
        self.generateInterpolateTable(nRows, nColumns)
        self.generateInterpolateValues()
        self.table = self.interpolateTable

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
        if(movement == 0): #UP
            tableToGetmax = self.table[column][row+1]
        if(movement == 1): #RIGHT
            tableToGetmax = self.table[column+1][row]
        if(movement == 2): #DOWN
            tableToGetmax = self.table[column][row-1]
        if(movement == 3): #LEFT
            tableToGetmax = self.table[column-1][row]
        
        self.table[column][row][movement] = self.gamma * max(tableToGetmax)
        

    def printTable(self):
        length = len(self.table)
        for i in range(length):
            print(i, self.table[length -1 - i])

    def getRewardValue(self, row, column, movement):
        try:
            return self.table[column][row][movement]
        except:
            print('Error')
            print(str(column), str(row), str(movement))
            exit()

    def getTable(self):
        return self.table

    def __init__(self, nRows, nColumns, nPossibleActions, gamma):
        self.gamma = gamma
        self.nPossibleActions = nPossibleActions
        
        self.table = []
        for column in range(nColumns):
            self.table.append([])
            for row in range(nRows):
                self.table[column].append([0,0,0,0])
