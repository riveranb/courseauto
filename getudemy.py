# 2020/10/24
# Uses pyautogui to detect feature images and handling click operations

import pyautogui

def locate_rectangle(picpathlist, conf=0.8):
    pyautogui.PAUSE = 1

    for path in picpathlist:
        tryCount = 5
        while tryCount >= 0:
            tryCount -= 1
            # find register button
            registerbtn = pyautogui.locateOnScreen(path, confidence=conf)
            if registerbtn == None:
                # try simplified chinese case
                registerbtn = pyautogui.locateOnScreen(path, confidence=conf)
            if registerbtn != None:
                return registerbtn

def register_udemycourse():
    pyautogui.PAUSE = 10
    
    print ("Detect Udemy logo: ", pyautogui.locateOnScreen('pics\\udemylogo.png', confidence=0.8))
    startRect = locate_rectangle(['pics\\gotocoursegreenbg_cht.png', 'pics\\startlearnredbg_cht'], 0.45)
    if startRect != None:
        print ("Already registered.")
        return

    freeRect = locate_rectangle(['pics\\free_cht.png', 'pics\\free_chs.png'], 0.45)
    if freeRect == None:
        print("Not a free course.")
        return

    registerbtnRect = locate_rectangle(['pics\\registernow_cht.png', 'pics\\registernow_chs.png', 'pics\\registernow_small_cht.png'], 
                                        0.45)
    if registerbtnRect == None:
        print ("Not found register button, give it up.")
        return
    
    pyautogui.moveTo(registerbtnRect, duration=0.5)
    pyautogui.PAUSE = 10
    pyautogui.click(registerbtnRect) # 1st click register

    # try looking for start course button
    startRect = locate_rectangle(['pics\\startlearnredbg_cht.png'], 0.45)
    if startRect == None:
        # search for red-background register button again
        registerbtnRect = locate_rectangle(['pics\\registernowredbg_cht.png'], 0.45)
        if registerbtnRect == None:
            print ("Not found register button to continue, give it up.")
            return
        
        pyautogui.moveTo(registerbtnRect, duration=0.5)
        pyautogui.PAUSE = 10
        pyautogui.click(registerbtnRect) # 2nd click register
        startRect = locate_rectangle(['pics\\startlearnredbg_cht.png'], 0.45)
    
    if startRect == None:
        print ("Not found start course button, give it up.")
    else:
        pyautogui.moveTo(startRect, duration=0.5)
        print ("Register this course successfully.")

    
