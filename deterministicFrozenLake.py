import random as rand

grid = []
gridX = 8
gridY = 8
holes = 4
goal = [rand.randint(0, gridX - 1), rand.randint(0, gridY - 1)]
discount = 0.9


def makeGrid():
    for i in range(gridY):
        temp = []
        for j in range(gridX):
            if i == goal[1] and j == goal[0]:
                temp.append(["G", 0])
            else:
                temp.append(["F", 0])
        grid.append(temp)

    # edge case blocked path, needs improvement not in mood

    for i in range(holes):
        x = rand.randint(0, gridX - 1)
        y = rand.randint(0, gridY - 1)
        grid[y][x] = ['H', -1]

    for x in grid:
        print(x)


def explorePath(x, y, value):
    grid[y][x][1] = value
    newVal = value * discount
    if x + 1 < gridX and grid[y][x + 1][0] != 'H':
        if grid[y][x + 1][1] < newVal:
            explorePath(x + 1, y, newVal)
    if x - 1 >= 0 and grid[y][x - 1][0] != 'H':
        if grid[y][x - 1][1] < newVal:
            explorePath(x - 1, y, newVal)
    if y + 1 < gridY and grid[y + 1][x][0] != 'H':
        if grid[y + 1][x][1] < newVal:
            explorePath(x, y + 1, newVal)
    if y - 1 >= 0 and grid[y - 1][x][0] != 'H':
        if grid[y - 1][x][1] < newVal:
            explorePath(x, y - 1, newVal)



def findPath(x, y):
    while x != goal[0] or y != goal[1]:
        max = 0
        maxMove = 4
        grid[y][x][0] = "P"
        if x+1 < gridX and grid[y][x+1][1] > max:
            max = grid[y][x+1][1]
            maxMove = 0
        if x-1 >= 0 and grid[y][x-1][1] > max:
            max = grid[y][x-1][1]
            maxMove = 1
        if y+1 < gridY and grid[y+1][x][1] > max:
            max = grid[y+1][x][1]
            maxMove = 2
        if y - 1 >= 0 and grid[y - 1][x][1] > max:
            max = grid[y-1][x][1]
            maxMove = 3
        if maxMove == 0:
            x += 1
        if maxMove == 1:
            x -= 1
        if maxMove == 2:
            y += 1
        if maxMove == 3:
            y -= 1

def printValues():
    for x in grid:
        out = ""
        for y in x:
            out = out + "{:.4f}".format(y[1]) + " "
        print(out)

def printPath():
    for x in grid:
        out = ""
        for y in x:
            out = out + y[0] + " "
        print(out)

print(goal)
makeGrid()
explorePath(x=goal[0], y=goal[1], value=1)
printValues()
startX = int(input("enter x cordinate of start : "))
startY = int(input("enter y cordinate of start : "))
findPath(x = startX, y = startY)
printPath()
