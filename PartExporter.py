import time

import pyautogui

from Util import gotoTab, getName, gotoExport


def partExporter(window_name, name_to_use, part_list):
    count = 1

    for part in part_list:
        gotoTab(window_name)
        gotoExport(window_name)

        pyautogui.press("enter")
        # time.sleep(0.1)

        for i in range(count):
            pyautogui.press("down")
            # time.sleep(0.1)

        pyautogui.press("enter")
        # time.sleep(0.1)

        for i in range(2):
            pyautogui.press("tab")

        pyautogui.press("enter")

        pyautogui.press("down", 3)
        pyautogui.press("enter")
        pyautogui.press("tab")
        pyautogui.press("enter")

        pyautogui.press("backspace")
        name = name_to_use + part
        print(name)
        pyautogui.write(name)

        pyautogui.press("enter")
        # time.sleep(0.1)

        if "Confirm Save" in getName():
            print("Confirming Name")
            pyautogui.press("left")
            pyautogui.press("enter")

        while window_name not in getName():
            time.sleep(0.1)

        count += 1


if __name__ == "__main__":
    partExporter("Get", "GetLucky", ["Sop", "Mezzo", "Alto", "Baritone"])
