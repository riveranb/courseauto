import webbrowser

# register Google Chrome browser
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

url = 'ani.gamer.com.tw'
webbrowser.get("chrome").open_new_tab(url)