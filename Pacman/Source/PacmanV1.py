import pygame
import math
from random import randrange
import random

# 28 Across 31 Tall
# 1: Empty Space
# 2: Tic-Tak
# 3: Wall
# 4: Ghost safe-space
# 5: Special Tic-Tak
gameBoard = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,5,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,5,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,2,3],
    [3,2,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,2,3],
    [3,2,2,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,2,2,3],
    [3,3,3,3,3,3,2,3,3,3,3,3,1,3,3,1,3,3,3,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,3,3,3,1,3,3,1,3,3,3,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,1,1,1,1,1,1,1,1,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,4,4,4,4,4,4,3,1,3,3,2,3,3,3,3,3,3],
    [1,1,1,1,1,1,2,1,1,1,3,4,4,4,4,4,4,3,1,1,1,2,1,1,1,1,1,1], # Middle Lane Row: 14
    [3,3,3,3,3,3,2,3,3,1,3,4,4,4,4,4,4,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,1,1,1,1,1,1,1,1,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,5,2,2,3,3,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,3,3,2,2,5,3],
    [3,3,3,2,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,2,3,3,3],
    [3,3,3,2,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,2,3,3,3],
    [3,2,2,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,3,3,2,3],
    [3,2,3,3,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,3,3,2,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
]




# spriteRatio = 2/3
# spriteRatio = 1
spriteRatio = 3/2
square = 40 # Size of each unit square
spriteOffset = square * (1 - spriteRatio) * (1/2)
pacmanImage = pygame.image.load("Sprites/tile048.png")
pacmanImage = pygame.transform.scale(pacmanImage, (int(square * spriteRatio), int(square * spriteRatio)))
level = 1
score = 0
highScore = 0

class Ghost:
    def __init__(self, row, col, color, delayCount):
        self.row = row
        self.col = col
        self.attacked = False
        self.color = color
        self.dir = randrange(4)
        self.dead = False
        self.delayCount = delayCount
        self.target = [-1, -1]
        self.ghostSpeed = 1/2
        self.lastLoc = [-1, -1]

    def isValidTwo(self, cRow, cCol, dist, visited):
        if cRow < 0 or cRow >= len(gameBoard) or cCol < 0 or cCol >= len(gameBoard[0]) or gameBoard[cRow][cCol] == 3:
            return False
        elif visited[cRow][cCol] <= dist:
            return False
        return True

    def isValid(self, cRow, cCol):
        if not ghostGate.count([cRow, cCol]) == 0:
            return True
        if cRow < 0 or cRow >= len(gameBoard) or cCol < 0 or cCol >= len(gameBoard[0]) or gameBoard[cRow][cCol] == 3:
            return False
        return True

    def setDir(self): #Very inefficient || can easily refactor
        # BFS search -> Not best route but a route none the less
        dirs = [[0, -self.ghostSpeed, 0],
                [1, 0, self.ghostSpeed],
                [2, self.ghostSpeed, 0],
                [3, 0, -self.ghostSpeed]
        ]
        random.shuffle(dirs)
        best = 10000
        bestDir = -1
        for newDir in dirs:
            if self.calcDistance(self.target, [self.row + newDir[1], self.col + newDir[2]]) < best:
                if not (self.lastLoc[0] == self.row + newDir[1] and self.lastLoc[1] == self.col + newDir[2]):
                    if newDir[0] == 0 and self.col % 1.0 == 0:
                        if self.isValid(math.floor(self.row + newDir[1]), int(self.col + newDir[2])):
                            bestDir = newDir[0]
                            best = self.calcDistance(self.target, [self.row + newDir[1], self.col + newDir[2]])
                    elif newDir[0] == 1 and self.row % 1.0 == 0:
                        if self.isValid(int(self.row + newDir[1]), math.ceil(self.col + newDir[2])):
                            bestDir = newDir[0]
                            best = self.calcDistance(self.target, [self.row + newDir[1], self.col + newDir[2]])
                    elif newDir[0] == 2 and self.col % 1.0 == 0:
                        if self.isValid(math.ceil(self.row + newDir[1]), int(self.col + newDir[2])):
                            bestDir = newDir[0]
                            best = self.calcDistance(self.target, [self.row + newDir[1], self.col + newDir[2]])
                    elif newDir[0] == 3 and self.row % 1.0 == 0:
                        if self.isValid(int(self.row + newDir[1]), math.floor(self.col + newDir[2])):
                            bestDir = newDir[0]
                            best = self.calcDistance(self.target, [self.row + newDir[1], self.col + newDir[2]])
        self.dir = bestDir

    def calcDistance(self, a, b):
        dR = a[0] - b[0]
        dC = a[1] - b[1]
        return math.sqrt((dR * dR) + (dC * dC))


    def setTarget(self):
        if gameBoard[int(self.row)][int(self.col)] == 4:
            self.attacked = False
            self.dead = False
            self.ghostSpeed = 1/2
            self.target = [ghostGate[0][0] - 1, ghostGate[0][1]+1]
            return
        elif self.attacked or self.dead:
            self.target = [14, 13]
            return
        while True:
            self.target = [randrange(31), randrange(28)]
            if not gameBoard[self.target[0]][self.target[1]] == 3 and not gameBoard[self.target[0]][self.target[1]] == 4:
                break

    def move(self):
        # print(self.target)
        self.lastLoc = [self.row, self.col]
        if self.dir == 0:
            self.row -= self.ghostSpeed
        elif self.dir == 1:
            self.col += self.ghostSpeed
        elif self.dir == 2:
            self.row += self.ghostSpeed
        elif self.dir == 3:
            self.col -= self.ghostSpeed

    def setAttacked(self, isAttacked):
        self.attacked = isAttacked

    def isAttacked(self):
        return self.attacked

    def setDead(self, isDead):
        self.dead = isDead

    def isDead(self):
        return self.dead

def getCount():
    total = 0
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[0])):
            if gameBoard[i][j] == 2 or gameBoard[i][j] == 5 or gameBoard[i][j] == 6:
                total += 1
    return total

(width, height) = (len(gameBoard[0]) * square, len(gameBoard) * square) # Game screen
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
ghostsafeArea = [12, 13] # The location the ghosts escape to when attacked
ghosts = [Ghost(11.0, 13.5, "red", 0), Ghost(14.0, 11.5, "blue", 1), Ghost(14.0, 13.5, "pink", 2), Ghost(14.0, 15.5, "orange", 3)]
# ghosts = [Ghost(11.0, 13.5, "red", 0)]
pacman = [23.0, 13.5] # Center of Second Last Row
dir = 0 # 0: North, 1: East, 2: South, 3: West
nextDir = 0
lives = 3
pacmanDelay = 2
pacmanCount = 0
totalCount = getCount()
collected = 0
pacForward = False # Was the last horizontal motion upwards
pacUp = True # Was the last vertical motion upwards?
mouthOpen = False
pacSpeed = 1/2
mouthChangeDelay = 5
mouthChangeCount = 0
tictakChangeDelay = 10
tictakChangeCount = 0
ghostGate = [[12, 13], [12, 14]]
ghostChangeDelay = 3
ghostChangeCount = 0
attackedTimer = 150
attackedCount = 0
ghostsAttacked = False


def canMove(row, col):
    # if row % 1.0 == 0:
    #     if col % 1.0 != 0:
    #         if pacForward and gameBoard[int(row)][math.ceil(col)] == 0:
    #             return False
    #         elif not pacForward and gameBoard[int(row)][math.floor(col)] == 0:
    #             return False
    # elif col % 1.0 == 0:
    #     if row % 1.0 != 0:
    #         if pacUp and gameBoard[math.floor(row)][col] == 0:
    #             return False
    #         elif not pacUp and gameBoard[math.ceil(row)][col] == 0:
    #             return False

    if col == -1 or col == len(gameBoard[0]):
        return True
    if gameBoard[int(row)][int(col)] != 3:
        return True
    return False

def drawGhost(ghost): # Ghosts states: Alive, Attacked, Dead
                      # Attributes: Color, Direction, Location
    ghostImage = pygame.image.load("Sprites/tile152.png")
    currentDir = ((ghost.dir + 3) % 4) * 2
    if ghost.delayCount == ghostChangeDelay:
        ghost.delayCount = 0
        currentDir += 1
    ghost.delayCount += 1
    if ghost.isDead():
        tileNum = 152 + currentDir
        ghostImage = pygame.image.load("Sprites/tile" + str(tileNum) + ".png")
    elif ghost.isAttacked():
        if attackedTimer - attackedCount < attackedTimer//3:
            print(attackedTimer - attackedCount)
            if (attackedTimer - attackedCount) % 20 < 10:
                print("here")
                ghostImage = pygame.image.load("Sprites/tile0" + str(70 + (currentDir - (((ghost.dir + 3) % 4) * 2))) + ".png")
            else:
                ghostImage = pygame.image.load("Sprites/tile0" + str(72 + (currentDir - (((ghost.dir + 3) % 4) * 2))) + ".png")
        else:
            ghostImage = pygame.image.load("Sprites/tile0" + str(72 + (currentDir - (((ghost.dir + 3) % 4) * 2))) + ".png")
    else:
        if ghost.color == "blue":
            tileNum = 136 + currentDir
            ghostImage = pygame.image.load("Sprites/tile" + str(tileNum) + ".png")
        elif ghost.color == "pink":
            tileNum = 128 + currentDir
            ghostImage = pygame.image.load("Sprites/tile" + str(tileNum) + ".png")
        elif ghost.color == "orange":
            tileNum = 144 + currentDir
            ghostImage = pygame.image.load("Sprites/tile" + str(tileNum) + ".png")
        elif ghost.color == "red":
            tileNum = 96 + currentDir
            if tileNum < 100:
                ghostImage = pygame.image.load("Sprites/tile0" + str(tileNum) + ".png")
            else:
                ghostImage = pygame.image.load("Sprites/tile" + str(tileNum) + ".png")

    ghostImage = pygame.transform.scale(ghostImage, (int(square * spriteRatio), int(square * spriteRatio)))
    screen.blit(ghostImage, (ghost.col * square + spriteOffset, ghost.row * square + spriteOffset, square, square))



# Draws pacman based on his current state
def drawPacman():
    global pacmanImage, screen, mouthOpen, mouthChangeCount

    if mouthChangeCount == mouthChangeDelay:
        mouthChangeCount = 0
        mouthOpen = not mouthOpen
    mouthChangeCount += 1

    if dir == 0:
        if mouthOpen:
            pacmanImage = pygame.image.load("Sprites/tile049.png")
        else:
            pacmanImage = pygame.image.load("Sprites/tile051.png")
    elif dir == 1:
        if mouthOpen:
            pacmanImage = pygame.image.load("Sprites/tile052.png")
        else:
            pacmanImage = pygame.image.load("Sprites/tile054.png")
    elif dir == 2:
        if mouthOpen:
            pacmanImage = pygame.image.load("Sprites/tile053.png")
        else:
            pacmanImage = pygame.image.load("Sprites/tile055.png")
    elif dir == 3:
        if mouthOpen:
            pacmanImage = pygame.image.load("Sprites/tile048.png")
        else:
            pacmanImage = pygame.image.load("Sprites/tile050.png")

    pacmanImage = pygame.transform.scale(pacmanImage, (int(square * spriteRatio), int(square * spriteRatio)))
    screen.blit(pacmanImage, (pacman[1] * square + spriteOffset, pacman[0] * square + spriteOffset, square, square))


def render():
    global tictakChangeCount
    screen.fill((0, 0, 0)) # Flushes the screen

    if tictakChangeCount == tictakChangeDelay:
        #Changes the color of special Tic-Taks
        flipColor()
        tictakChangeCount = 0

    tictakChangeCount += 1
    # Draws game elements
    currentTile = 0
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[0])):
            if gameBoard[i][j] == 3: # Draw wall
                imageName = str(currentTile)
                if len(imageName) == 1:
                    imageName = "00" + imageName
                elif len(imageName) == 2:
                     imageName = "0" + imageName
                # Get image of desired tile
                imageName = "tile" + imageName + ".png"
                tileImage = pygame.image.load("PacmanGameBoardImages/" + imageName)
                tileImage = pygame.transform.scale(tileImage, (square, square))

                #Display image of tile
                screen.blit(tileImage, (j * square, i * square, square, square))

                # pygame.draw.rect(screen, (0, 0, 255),(j * square, i * square, square, square)) # (x, y, width, height)
            elif gameBoard[i][j] == 2: # Draw Tic-Tak
                pygame.draw.circle(screen, (255, 255, 255),(j * square + square//2, i * square + square//2), square//8)
            elif gameBoard[i][j] == 5: #Black Special Tic-Tak
                pygame.draw.circle(screen, (0, 0, 0),(j * square + square//2, i * square + square//2), square//3)
            elif gameBoard[i][j] == 6: #White Special Tic-Tak
                pygame.draw.circle(screen, (255, 255, 255),(j * square + square//2, i * square + square//2), square//3)

            currentTile += 1
    # Draw Sprites
    for ghost in ghosts:
        drawGhost(ghost)
    drawPacman()

    pygame.display.update() # Updates the screen

# Reset after death
def reset():
    global ghosts, pacman, lives, dir, playing
    # ghosts = [Ghost(7, 6), Ghost(6, 6), Ghost(5, 6)]
    ghosts = [Ghost(11.0, 13.5, "red", 0), Ghost(14.0, 11.5, "blue", 1), Ghost(14.0, 13.5, "pink", 2), Ghost(14.0, 15.5, "orange", 3)]
    pacman = [23.0, 13.5]
    lives -= 1
    dir = 0
    playing = False
    render()

def movePacman(newDir):
    global pacman, pacUp, pacForward
    if newDir == 0:
        if canMove(math.floor(pacman[0] - pacSpeed), pacman[1]) and pacman[1] % 1.0 == 0:
            pacman[0] -= pacSpeed
            pacUp = True
            return True
    elif newDir == 1:
        if canMove(pacman[0], math.ceil(pacman[1] + pacSpeed)) and pacman[0] % 1.0 == 0:
            pacman[1] += pacSpeed
            pacForward = True
            return True
    elif newDir == 2:
        if canMove(math.ceil(pacman[0] + pacSpeed), pacman[1]) and pacman[1] % 1.0 == 0:
            pacman[0] += pacSpeed
            pacUp = False
            return True
    elif newDir == 3:
        if canMove(pacman[0], math.floor(pacman[1] - pacSpeed)) and pacman[0] % 1.0 == 0:
            pacman[1] -= pacSpeed
            pacForward = False
            return True
    return False
# Flips Color of Special Tic-Taks
def flipColor():
    global gameBoard
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[0])):
            if gameBoard[i][j] == 5:
                gameBoard[i][j] = 6
            elif gameBoard[i][j] == 6:
                gameBoard[i][j] = 5

def touchingPacman(ghost):
    if ghost.row - ghost.ghostSpeed == pacman[0] and ghost.col == pacman[1]:
        return True
    elif ghost.row + ghost.ghostSpeed == pacman[0] and ghost.col == pacman[1]:
        return True
    elif ghost.row == pacman[0] and ghost.col  - ghost.ghostSpeed == pacman[1]:
        return True
    elif ghost.row == pacman[0] and ghost.col + ghost.ghostSpeed == pacman[1]:
        return True
    elif ghost.row == pacman[0] and ghost.col == pacman[1]:
        return True
    return False

running = True
playing = False
render()

def pause(time):
    cur = 0
    while not cur == time:
        cur += 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            playing = True
            if event.key == pygame.K_w:
                nextDir = 0
            elif event.key == pygame.K_d:
                nextDir = 1
            elif event.key == pygame.K_s:
                nextDir = 2
            elif event.key == pygame.K_a:
                nextDir = 3
            elif event.key == pygame.K_q:
                running = False

    if not playing:
        continue

    if lives == 0:
        running = False
    pacmanCount += 1

    # Check if pacman got killed
    for ghost in ghosts:
        if touchingPacman(ghost) and not ghost.attacked:
            reset()
        elif touchingPacman(ghost) and ghost.isAttacked() and not ghost.isDead():
            ghost.setDead(True)
            pause(10000000)

    if pacmanCount == pacmanDelay:
        pacmanCount = 0
        if movePacman(nextDir):
            dir = nextDir
        else:
            movePacman(dir)
        # Update Ghosts || Ghost movement states: Moving, Waiting
    if ghostChangeCount == ghostChangeDelay:
        ghostChangeCount = 0
        for ghost in ghosts:
            if ghost.target == [-1, -1] or (ghost.row == ghost.target[0] and ghost.col == ghost.target[1]) or gameBoard[int(ghost.row)][int(ghost.col)] == 4 or ghost.attacked:
                ghost.setTarget()
            ghost.setDir()
            ghost.move()
    ghostChangeCount += 1

    # Check if pacman got killed
    for ghost in ghosts:
        if touchingPacman(ghost) and not ghost.attacked:
            reset()
        elif touchingPacman(ghost) and ghost.isAttacked() and not ghost.isDead():
            ghost.setDead(True)
            pause(10000000)


    pacman[1] %= len(gameBoard[0])
    if pacman[0] % 1.0 == 0 and pacman[1] % 1.0 == 0:
        if gameBoard[int(pacman[0])][int(pacman[1])] == 2:
            collected += 1
            gameBoard[int(pacman[0])][int(pacman[1])] = 1
            score += 10
        elif gameBoard[int(pacman[0])][int(pacman[1])] == 5 or gameBoard[int(pacman[0])][int(pacman[1])] == 6:
            collected += 1
            gameBoard[int(pacman[0])][int(pacman[1])] = 1
            attackedCount = 0
            score += 10
            for ghost in ghosts:
                ghost.setAttacked(True)
                ghost.ghostSpeed = 1/4
                ghostsAttacked = True

    if ghostsAttacked:
        attackedCount += 1
        print(attackedCount, attackedTimer)

    if attackedCount == attackedTimer and ghostsAttacked:
        ghostsAttacked = False
        attackedCount = 0
        for ghost in ghosts:
            ghost.setAttacked(False)
            ghost.setDead(False)
            ghost.setTarget()
            ghost.ghostSpeed = 1/2


    render()

    highScore = max(highScore, score)

    if collected == totalCount:
        playing = False
