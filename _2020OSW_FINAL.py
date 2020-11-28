from bangtal import *
from GameManager import GameManager

MenuScene = Scene('MENU', 'Images/background/background.png')
GameScene = Scene('GAME', 'Images/button/start.png')

startButton = Object('Images/button/start.png')
startButton.locate(MenuScene, 570, 200)
startButton.show()

def startButton_onMouseAction(x, y, action):
    GameScene.enter()
    manager = GameManager(GameScene)
startButton.onMouseAction = startButton_onMouseAction

startGame(MenuScene)
