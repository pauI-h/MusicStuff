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


def selectRow(row_num: int):
    pyautogui.press("left")
    time.sleep(1)
    if OS == "WIN":
        print("Win")
        pyautogui.hotkey("ctrl", "home")  # command fn left
    else:
        pyautogui.hotkey("command", "fn", "left")

    time.sleep(1)
    pyautogui.press("right")
    print("right")

    time.sleep(1)
    if OS == "WIN":
        print("win")
        pyautogui.keyDown("alt")  # option
    else:
        pyautogui.keyDown("option")

    time.sleep(1)

    for i in range(row_num):
        time.sleep(0.3)
        print("down")
        pyautogui.press("down")

    time.sleep(1)

    if OS == "WIN":
        pyautogui.keyUp("alt")  # option
    else:
        pyautogui.keyUp("option")

    time.sleep(1)

    if OS == "WIN":
        pyautogui.keyDown("shift")
        time.sleep(1)

        pyautogui.keyDown("ctrl")
        time.sleep(1)

        pyautogui.press("end")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("ctrl")


def shiftRow(shift: int):
    for i in range(shift):
        pyautogui.press("down")


def export(row: int, window_name: str, file_name: str):
    pyautogui.press("left")
    pyautogui.moveTo(1, 1)
    pyautogui.click()
    time.sleep(0.5)
    press = 11
    if OS != "WIN":
        press += 1
    for i in range(press):
        pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("enter")

    if OS == "APP" and window_name not in getName():
        pyautogui.press("esc")
        gotoTab(window_name)
        export(row, window_name, file_name)
        return

    if OS == "WIN":
        if "Log in" in getName():
            pyautogui.press("esc")
            export(row, window_name, file_name)
            return

        if "Export" not in getName():
            pyautogui.press("esc")
            gotoTab(window_name)
            export(row, window_name, file_name)
            return

    time.sleep(0.5)
    pyautogui.press("enter")
    for i in range(row + 1):
        pyautogui.press("down")

    pyautogui.press("enter")

    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    for i in range(3):
        pyautogui.press("down")
    pyautogui.press("enter")

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.write(file_name)
    pyautogui.press("enter")


def shifter(tab_name: str, new_file_name: str, row_to_shift: int, amount_to_shift: int):
    gotoTab(tab_name)
    selectRow(row_to_shift)
    shiftRow(amount_to_shift)
    export(row_to_shift, tab_name, new_file_name)


if __name__ == "__main__":
    if sys.platform == "win32":
        name = "Get"
    else:
        name = "Muse"

    gotoTab(name)
    size = pyautogui.size()
    pyautogui.moveTo(size[0]/2, 1)
    selectRow(3)
    #shiftRow(2)
    #export(3, name, "Get Lucky Lower Bass")
