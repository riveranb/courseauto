import webbrowser
import time
import ctypes  # An included library with Python install
import pyautogui   

# register Google Chrome browser (for Windows)
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

url_lines = open('urls.txt', 'r').readlines()
for url in url_lines:
    print(url)
    webbrowser.get("chrome").open_new_tab(url)
    time.sleep(1)

ctypes.windll.user32.MessageBoxW(0, "courseauto complete!", "Message", 0)