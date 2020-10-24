import webbrowser
import time
import ctypes  # An included library with Python install

import getudemy as getud

# register Google Chrome browser (for Windows)
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

url_lines = open('urls.txt', 'r').readlines()
for url in url_lines:
    webbrowser.get("chrome").open_new_tab(url)
    time.sleep(10)
    getud.register_udemycourse()
    print("Done: " + url)

ctypes.windll.user32.MessageBoxW(0, "courseauto complete!", "Message", 0)