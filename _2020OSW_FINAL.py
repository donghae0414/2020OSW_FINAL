from bangtal import *
from GameManager import GameManager

# Game Options
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

MenuScene = Scene('MENU', 'Images/background/background.png')
GameScene = Scene('GAME', 'Images/button/start.png')

startButton = Object('Images/button/start.png')
startButton.locate(MenuScene, 500, 200)
startButton.setScale(0.15)
startButton.show()

def startButton_onMouseAction(x, y, action):
    GameScene.enter()
    manager = GameManager(GameScene)
startButton.onMouseAction = startButton_onMouseAction

startGame(MenuScene)

