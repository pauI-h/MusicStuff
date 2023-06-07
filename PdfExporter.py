import time

import pyautogui

from Util import gotoExport, gotoTab, getName, writeName, confirmNameAndWait


def pdfExporter(window_name: str, name_to_use: str, part_list: list):
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

        for i in range(3):
            pyautogui.press("tab")

        pyautogui.press("enter")

        writeName(name_to_use, part)

        pyautogui.press("enter")
        # time.sleep(0.1)

        confirmNameAndWait(window_name)

        count += 1


if __name__ == "__main__":
    pdfExporter("Get", "Get_Lucky_", ["Sop", "Mezzo", "Alto", "Baritone"])
