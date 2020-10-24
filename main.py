import sys
import webbrowser
import time
import ctypes  # An included library with Python install

import getudemy

# parse argument
if len(sys.argv) < 2:
    print ("Usage: py main.py [urls-filepath]")
    exit(1)

print ("Input file: ", sys.argv[1])

urlfile = sys.argv[1]

# register Google Chrome browser (for Windows)
chrome_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
# register FireFox browser (for Windows)
firefox_path = 'D:\\Program Files\\Mozilla Firefox\\firefox.exe'
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

url_lines = open(urlfile, 'r').readlines()
for url in url_lines:
    webbrowser.get(getudemy.BROWSER).open_new_tab(url)
    # wait for browser
    time.sleep(10)
    getudemy.register_udemycourse()
    print("Done: " + url)

ctypes.windll.user32.MessageBoxW(0, "courseauto complete!", "Message", 0)