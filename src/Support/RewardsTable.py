class RewardsTable:

    def setValue(self, position, value):
        self.table[position] = value

    def setRewardValueOnLine(self, rewardLine, rewardColumn, rewardValue):
        self.table[(((rewardLine -1)*self.nColumns) + rewardColumn + 1)+1] = rewardValue

    def __init__(self, nColumns, nRows):
        self.nColumns = nColumns
        self.nRows = nRows
        self.table = [0] * (nColumns * nRows)