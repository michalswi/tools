#!/usr/bin/env python3

"""
./makeScreenshot.py "['<domain1>', '<domain2>', '<domain3>']"
"""

from selenium import webdriver
import time
from datetime import datetime
import sys
import threading

supportedBrowsers = ["firefox", "chrome"]

def startBrowser(name):
    try:
        if name.lower() == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif name.lower() == "chrome":
            driver = webdriver.Chrome()
            return driver
        else:
            print("Browser not found")
    except Exception as msg:
        print("Message: %s", str(msg))

def makeScreenshot(url, name):
    if name in supportedBrowsers:
        print(f"Job for domain '{url}', START time: {datetime.now().strftime('%H:%M:%S')}")
        driver = startBrowser(name)
        try:
            driver.get("https://"+url)
            time.sleep(5)
            driver.save_screenshot(f'{url}_.png')
        finally:
            driver.quit()
            print(f"Job for domain '{url}', END time: {datetime.now().strftime('%H:%M:%S')}")
    else:
        print(f"Browser '{name}' not supported")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Missing list of domains")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many args")
        sys.exit(1)
    else:
        victimURLs=eval(sys.argv[1])
        if type(victimURLs) == list:
            threads = []
            for i in range(len(victimURLs)):
                # 'firefox' recommended for macos
                # 'chrome' recommended for linux
                t = threading.Thread(target=makeScreenshot, args=(victimURLs[i], "firefox"))
                threads.append(t)
                t.start()
            for t in threads:
                t.join()
