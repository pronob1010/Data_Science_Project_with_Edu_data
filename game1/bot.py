from PIL import ImageGrab
import pyautogui

class cordinates():
    replayBtn= (250,120)

def restartGame():
    pyautogui.click(cordinates.replayBtn)
    restartGame()