import sys
import time

import pyautogui

OS = "APP"
if sys.platform == "win32":
    from win32gui import GetForegroundWindow, GetWindowText

    OS = "WIN"


    def getName():
        return GetWindowText(GetForegroundWindow())
else:
    from AppKit import NSWorkspace


    def getName():
        return NSWorkspace.sharedWorkspace().activeApplication()


def gotoExport(window_name):
    pyautogui.press("left")
    pyautogui.moveTo(1, 1)
    pyautogui.click()
    time.sleep(0.3)
    press = 11
    if OS != "WIN":
        press += 1
    for i in range(press):
        pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("enter")

    if OS == "APP" and window_name not in getName():
        pyautogui.press("esc")
        gotoTab(window_name)
        gotoExport(window_name)
        return

    if OS == "WIN":
        if "Log in" in getName():
            pyautogui.press("esc")
            gotoExport(window_name)
            return

        if "Export" not in getName():
            pyautogui.press("esc")
            gotoTab(window_name)
            gotoExport(window_name)
            return


def gotoTab(name: str):
    window = getName()
    count = 0
    while name not in str(window):
        count += 1
        if OS == "WIN":
            pyautogui.keyDown("alt")
        else:
            pyautogui.keyDown("command")

        for i in range(count):
            pyautogui.press("tab")

        if OS == "WIN":
            pyautogui.keyUp("alt")
        else:
            pyautogui.keyUp("command")

        window = getName()
        print(getName())
        if count > 10:
            raise Exception("Could not find tab")
        # time.sleep()


def getPixelValue(x, y, handle=True):
    if OS == "WIN":
        try:
            return pyautogui.pixel(x, y)
        except Exception as e:
            if handle:
                time.sleep(0.5)
                return getPixelValue(x, y, False)
            else:
                raise e


def writeName(name, part):
    time.sleep(0.3)
    pyautogui.write(part + "_" + name)
    pyautogui.press("enter")
