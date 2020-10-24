import pyautogui

def register_udemycourse():
    pyautogui.PAUSE = 10
    
    print (pyautogui.locateOnScreen('pics\\udemylogo.png', confidence=0.8))
    print (pyautogui.locateOnScreen('pics\\gotocoursegreenbg_cht.png', confidence=0.8))