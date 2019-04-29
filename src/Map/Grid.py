import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

plt.ion()
plt.show()
class Grid:
    def setUpGrid(self):
        # make an empty data set
        self.data = np.ones((self.nColumns, self.nRows))

        # make a figure + axes
        self.fig = plt.figure()
        self.fig.set_tight_layout(True)
        self.fig.canvas.set_window_title('Q-Learning')
        self.ax = self.fig.add_subplot(111)
        # self.fig, self.ax = plt.subplots(1, 1, tight_layout=True)


        # make color map
        self.my_cmap = matplotlib.colors.ListedColormap(['r', 'g', 'b'])


        # set the 'bad' values (nan) to be white and transparent
        self.my_cmap.set_bad(color='w', alpha=0)


        # draw the grid
        for x in range(self.nColumns + 1):
            self.ax.axhline(x, lw=2, color='k', zorder=5) # Y line
        for x in range(self.nRows + 1):
            self.ax.axvline(x, lw=2, color='k', zorder=5) # X line


        # draw the boxes
        self.ax.imshow(self.data, interpolation='none', cmap=self.my_cmap, extent=[0, self.nRows, 0, self.nColumns], zorder=0)

        # turn off the axis labels
        self.ax.axis('off')

    def updateGrid(self, ghost, pacman):
        self.drawAgent(ghost.getOldGhost())

        self.drawAgent(ghost)
        self.drawAgent(pacman)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.001)

    def blockGrid(self):
        plt.show(block = True)

    def drawAgent(self, agent, size = 0.1):
        agentImage = plt.Circle((agent.getColumn() + 0.5, agent.getRow() + 0.5), size, color=agent.getColor())
        self.ax.add_artist(agentImage)
        
    def checkPacmanCatch(self, ghost, pacman):
        if(ghost.getColumn() == pacman.getColumn() and ghost.getRow() == pacman.getRow()):
            self.updateGrid(ghost, pacman)
            return True

    def resetGrid(self):
        self.drawAgent(self.initialGhost)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def __init__(self, columns, rows, initialGhost, initialPacman):
        self.nRows = rows
        self.nColumns = columns

        self.initialGhost = initialGhost
        self.initialPacman = initialPacman

        self.setUpGrid()
