from src.Map.Grid import Grid
from src.Agents.Agent import Agent
from src.Agents.Ghost import Ghost
from src.Support.RewardsTable import RewardsTable

nRows = 4
nColumns = 4

pacmanInitialRow = nRows - 1
pacmanInitialColumn = 0

ghostInitialRow = 0
ghostInitialColumn = nColumns - 1

nPossibleActions = 4
goalReward = 100
gamma = 0.9

if __name__ == "__main__":
    rewardsTable = RewardsTable(nRows, nColumns, nPossibleActions, gamma)
    # rewardsTable.setGoalReward(pacmanInitialRow, pacmanInitialColumn, goalReward)

    pacman = Agent(pacmanInitialRow, pacmanInitialColumn, 'yellow')
    ghost = Ghost(ghostInitialRow, ghostInitialColumn, 'b', nPossibleActions, nRows, nColumns, rewardsTable)
    ghost.setOldGhost()
    
    grid = Grid(nRows, nColumns, Ghost(ghostInitialRow, ghostInitialColumn, 'b', nPossibleActions, nRows, nColumns, rewardsTable),  Agent(pacmanInitialRow, pacmanInitialColumn, 'yellow'))

    while(True):
        grid.updateGrid(ghost, pacman)
        ghost.move()
        if(grid.checkPacmanCatch(ghost, pacman)):
            ghost.setPacmanCatched()
            grid.resetGrid()
    print('End')
    grid.blockGrid()