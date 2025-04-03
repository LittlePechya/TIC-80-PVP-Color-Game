# title:   PvP Clor Blocks
# author:  https://littlepechya.itch.io/
# desc:    Paint more blocks than your friend and prove that you are really cool.
# site:    https://littlepechya.itch.io/
# license: MIT License
# version: 1.0
# script:  python

startX = 0
startY = 0

currentX = 0
currentY = 0

player1Blocks = 0
player2Blocks = 0

scaleVar = 4
step = scaleVar * 8

fieldLen = 239 - step
fieldHeight = 135 - step

gameOver = False


def BOOT():
    cls()


def TIC():
    global gameOver
    global currentX, currentY
    global player1Blocks, player2Blocks

    if gameOver:
        gameOverScreen(player1Blocks, player2Blocks)
        if btnp(4) or btnp(5):
            resetGame()
        return

    handlePlayerInput(currentX, currentY)


def handlePlayerInput(currentX, currentY):
    global player1Blocks
    global player2Blocks

    if btnp(4):
        MarkBlock(currentX, currentY, 1)
        player1Blocks += 1
        nextMove()
    elif btnp(5):
        MarkBlock(currentX, currentY, 2)
        player2Blocks += 1
        nextMove()


def nextMove():
    global currentX
    global currentY
    global gameOver

    currentX += step

    if currentX > fieldLen:
        currentX = 0
        currentY += step

    if currentY > fieldHeight:
        gameOver = True


def MarkBlock(x, y, player):
    if player == 1:
        spr(0, x, y, scale=scaleVar)
    elif player == 2:
        spr(1, x, y, scale=scaleVar)


def resetGame():
    global currentX, currentY, gameOver, gameWaiting
    currentX = 0
    currentY = 0
    gameOver = False
    gameWaiting = True
    cls()


def gameOverScreen(p1Blocks, p2Blocks):
    global fieldLen, fieldHeight
    print("Game Over!", 84, 52, 12)

    if p1Blocks > p2Blocks:
        message = "Player 1 won!"
    elif p2Blocks > p1Blocks:
        message = "Player 2 won"
    else:
        message = "It's a tie!"

    print(message, 76, 60, 12)
    print("Press Z or X to restart", 48, 68, 12)
