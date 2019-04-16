import pyautogui

def getColor():
    x, y = pyautogui.position()
    pixelColor = pyautogui.screenshot().getpixel((x,y))
    return ([pixelColor[0], pixelColor[1], pixelColor[2]], (x, y))
