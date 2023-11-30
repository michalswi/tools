#!/usr/bin/env python3

"""
./makeScreenshot.py "['<domain1>', '<domain2>', '<domain3>']"
"""

from selenium import webdriver
import time
from datetime import datetime
import sys
import threading

def startBrowser(name):
    try:
        if name.lower() == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif name.lower() == "chrome":
            driver = webdriver.Chrome()
            return driver
        else:
            print("browser not found")
    except Exception as msg:
        print("message %s", str(msg))

def makeScreenshot(name, url):
    print(f"job for {url}, start time: {datetime.now().strftime('%H:%M:%S')}")
    driver = startBrowser(name)
    driver.get("https://"+url)
    time.sleep(5)
    driver.save_screenshot(f'{url}_.png')
    driver.quit()

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Missing list of domains.")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many args.")
        sys.exit(1)
    else:
        victimURLs=eval(sys.argv[1])
        if type(victimURLs) == list:
            threads = list()
            for i in range(len(victimURLs)):
                t = threading.Thread(target=makeScreenshot, args=("firefox", victimURLs[i]))
                threads.append(t)
                t.start()
