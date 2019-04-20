import random
from Support.RewardsTable import RewardsTable


class Ghost:
    nColumns = 10
    nRows = 10
    oldGreatestValue = -1
    oldGreatestValueIndex = -1
    greatestValue = -1
    greatestValueIndex = -1
    auxiliarList = []
    actionValuesTable = [0] * (nColumns * nRows)
    # rewardsTable = [0] * (nColumns * nRows)
    auxiliarCounter = 0
    totalNumberOfActions = 4
    actionValue = 0
    oldAgentLine = 0
    oldAgentColumn = 0
    agentLine = 0
    agentColumn = 0
    catchPacman = False
    gamma = 0.9
    goal = 0

    # Select a random action:
    # 0 - up
    # 1 - right
    # 2 - down
    # 3 - left
    def getRandomAction(self):
        self.greatestValue = random.randint(0, self.totalNumberOfActions-1)

    def getValueForActionInTableLine(self, actionCode, line, column):
        print(((line -1)*self.nColumns*self.totalNumberOfActions)+((((column -1)*self.totalNumberOfActions)+actionCode)+1))
        self.actionValuesTable[((line -1)*self.nColumns*self.totalNumberOfActions)+((((column -1)*self.totalNumberOfActions)+actionCode)+1)] = self.actionValue

    def getValueForAction(self, auxiliarCounter):
        return self.getValueForActionInTableLine(auxiliarCounter, self.agentLine, self.agentColumn)

    def getGreatestValue(self):
        self.auxiliarCounter = 1
        self.greatestValue = -1
        self.greatestValueIndex = 1
        for (x, index) in enumerate(self.auxiliarList):
            if(x > self.greatestValue):
                self.greatestValue = 1
                self.greatestValueIndex = index

    def getActionsValuesForCurrentPosition(self):
        self.auxiliarList.clear()
        self.auxiliarCounter = 0
        for self.auxiliarCounter in range(self.totalNumberOfActions):
            self.getValueForAction(self.auxiliarCounter)
            self.auxiliarList.append(self.actionValue)
            self.auxiliarCounter += 1


    def getBestActionWithoutRandomChance(self):
        self.getActionsValuesForCurrentPosition()
        self.getGreatestValue()

    def act(self):
        if(self.greatestValueIndex > 0 and self.greatestValueIndex < (self.totalNumberOfActions + 1)):
            if(self.greatestValueIndex == 1): # Up
                self.agentLine = self.oldAgentLine - 1
                self.agentColumn = self.oldAgentColumn
            elif(self.greatestValueIndex == 2): # Right
                self.agentLine = self.oldAgentLine
                self.agentColumn = self.oldAgentColumn + 1
            elif(self.greatestValueIndex == 3): # Down
                self.agentLine = self.oldAgentLine + 1
                self.agentColumn = self.oldAgentColumn
            elif(self.greatestValueIndex == 4): # Left
                self.agentLine = self.oldAgentLine
                self.agentColumn = self.oldAgentColumn - 1

    def setValueInTheValuesTableAtLine(self, value, actionCode, line, column):
        self.actionValuesTable[((line -1)*nColumns*totalNumberOfActions)+((((column -1)*totalNumberOfActions)+actionCode)+1)] = value

    def setValueInTheOldPosition(self, rewardValue, actionCode):
        self.setValueInTheValuesTableAtLine(rewardValue, actionCode, oldAgentLine, oldAgentColumn)        


    def getRewardValueOnLine(self, column, row):
        self.rewardsTable.setValue((((row - 1)*self.nColumns)+(column -1)+1), self.rewardValue)

    def updateActionValueInTheOldPosition(self):
        self.oldGreatestValue = self.greatestValue
        self.oldGreatestValueIndex = self.greatestValueIndex
        self.getRewardInTheCurrentPosition()
        self.getBestActionWithoutRandomChance()
        self.setValueInTheOldPosition(self.rewardValue + (gamma * self.greatestValue), self.oldGreatestValueIndex - 1)
        self.oldAgentLine = self.agentLine
        self.oldAgentColumn = self.agentColumn


    def getBestAction(self):
        # Choose a random place by 1% of chance
        if(random.randint(1,100) < 2):
            self.getRandomAction()
        else:
            self.getBestActionWithoutRandomChance()
            # If greatestValue == 0, sprint always move to the first possible action according
            # To the order: up, right, down, left
            if(self.greatestValue == 0):
                self.getRandomAction()

    def __init__(self):
        self.agentLine = 1
        self.agentColumn = 1
        self.gamma = 0.9
        self.goal = 0

        self.rewardsTable = RewardsTable(self.nColumns, self.nRows)
        while(not self.catchPacman):
            self.getBestAction()
            self.act()
            self.updateActionValueInTheOldPosition()
