# 2020/10/24
# Uses pyautogui to detect feature images and handling click operations

import os
import pyautogui

def locate_rectangle(picpathlist, conf=0.8):
    pyautogui.PAUSE = 1

    tryCount = 5 # times to try
    while tryCount >= 0:
        tryCount -= 1
        for path in picpathlist: # for each picture-template
            # find register button
            registerbtn = pyautogui.locateOnScreen(path, confidence=conf)
            if registerbtn == None:
                # try simplified chinese case
                registerbtn = pyautogui.locateOnScreen(path, confidence=conf)
            if registerbtn != None:
                return registerbtn

def collect_pictureseries(templatename):
    postfixes = ['_small_cht_chrome.png', '_cht_chrome.png', '_small_chs_chrome.png', '_chs_chrome.png',
                 '_small_cht_firefox.png', '_cht_firefox.png', '_small_chs_firefox.png', '_chs_firefox.png']
    
    series = []
    for postf in postfixes:
        filename = str(templatename) + postf
        if os.path.isfile(filename):
            series.append(filename)
    
    return series

def register_udemycourse():
    pyautogui.PAUSE = 10
    
    print ("Detect Udemy logo: ", pyautogui.locateOnScreen('pics\\udemylogo.png', confidence=0.8))
    picfiles = collect_pictureseries('pics\\gotocoursegreenbg')
    picfiles += collect_pictureseries('pics\\startlearnredbg')
    startRect = locate_rectangle(picfiles)
    if startRect != None:
        pyautogui.PAUSE = 1
        pyautogui.moveTo(startRect, duration=0.5)
        print ("Already registered.")
        return

    # confidence = 0.8, not works
    picfiles = collect_pictureseries('pics\\free')
    freeRect = locate_rectangle(picfiles, 0.7)
    if freeRect == None:
        print("Not a free course.")
        return

    picfiles = collect_pictureseries('pics\\registernow')
    registerbtnRect = locate_rectangle(picfiles)
    if registerbtnRect == None:
        print ("Not found register button, give it up.")
        return
    
    pyautogui.moveTo(registerbtnRect, duration=0.5)
    pyautogui.PAUSE = 10
    pyautogui.click(registerbtnRect) # 1st click register

    # try looking for start course button
    picfiles = collect_pictureseries('pics\\startlearnredbg')
    startRect = locate_rectangle(picfiles)
    if startRect == None:
        # search for red-background register button again
        picfiles = collect_pictureseries('pics\\registernowredbg')
        registerbtnRect = locate_rectangle(picfiles)
        if registerbtnRect == None:
            print ("Not found register button to continue, give it up.")
            return
        
        pyautogui.moveTo(registerbtnRect, duration=0.5)
        pyautogui.PAUSE = 10
        pyautogui.click(registerbtnRect) # 2nd click register
        picfiles = collect_pictureseries('pics\\startlearnredbg')
        startRect = locate_rectangle(picfiles)
    
    if startRect == None:
        print ("Not found start course button, give it up.")
    else:
        pyautogui.moveTo(startRect, duration=0.5)
        print ("Register this course successfully.")

    
