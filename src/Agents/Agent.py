class Agent:

    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column

    def getColor(self):
        return self.color

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
