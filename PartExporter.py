import time

import pyautogui

from Util import gotoTab, gotoExport, getPixelValue, writeName, confirmNameAndWait


def loadFromConfig():
    file = open("Config.txt", "r")
    lines = file.readlines()
    file.close()
    offset_line = lines[0].strip("\n")
    offset = int(offset_line.split(":")[1])
    return offset


OFFSET = loadFromConfig()


def purePartExporter(window_name, name_to_use, part_list):
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

        writeName(name_to_use, part)

        pyautogui.press("enter")
        # time.sleep(0.1)

        confirmNameAndWait(window_name)

        count += 1


def backedPartExporter(window_name, name_to_use, part_list, main_part_volume, backing_volume):
    # 1/11th of the screen
    size = pyautogui.size()
    x = size[0] // 11
    y = (11 * size[1]) // 19 + OFFSET

    gotoTab(window_name)
    pyautogui.hotkey("fn", "f10")

    time.sleep(1)
    base_value = getPixelValue(x, y)
    pyautogui.moveTo(x, y)
    selected_value = getPixelValue(x, y)

    pyautogui.moveTo(size[0] / 2, 1)

    for part in range(len(part_list)):
        setPart(base_value, x, y, part, len(part_list), main_part_volume, backing_volume)
        gotoExport(window_name)

        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")

        for i in range(3):
            pyautogui.press("down")
        pyautogui.press("enter")

        pyautogui.press("tab")
        pyautogui.press("enter")

        writeName(name_to_use, part_list[part])

        confirmNameAndWait(window_name)

    resetParts(base_value, x, y, len(part_list), backing_volume)


def setPart(base_value, x, y, part_num, num_parts, main_volume, other_volume):
    while getPixelValue(x, y) == base_value:
        pyautogui.press("tab")

    time.sleep(0.3)
    if part_num == 0:
        for i in range(4):
            time.sleep(0.1)
            pyautogui.press("down")

    for i in range(num_parts):
        if i == part_num:
            if i != 0:
                for i in range(main_volume - other_volume):
                    pyautogui.press("right")
            if main_volume > 0:
                key = "left"
            else:
                key = "right"
            for i in range(abs(main_volume)):
                pyautogui.press(key)
        else:
            if i == part_num - 1 or part_num == 0:
                print(main_volume - other_volume)
                for i in range(main_volume - other_volume):
                    pyautogui.press("left")

        pyautogui.press("tab")


def resetParts(base_value, x, y, num_parts, other_volume):
    while getPixelValue(x, y) == base_value:
        pyautogui.press("tab")

    time.sleep(0.3)
    for i in range(num_parts - 1):
        for i in range(-1 * other_volume):
            pyautogui.press("right")
        for i in range(other_volume):
            pyautogui.press("left")
        pyautogui.press("tab")


if __name__ == "__main__":
    backedPartExporter("Get", "GetLucky", ["Sop", "Mezzo", "Alto", "Baritone"], 0, -30)
    # purePartExporter("Get", "GetLucky", ["Sop", "Mezzo", "Alto", "Baritone"])
