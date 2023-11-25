import pyautogui
import cv2 as cv
import numpy as np
from dataclasses import dataclass
import time
from random import random


class Area:
    def __init__(self,tl,bl,tr,br,img_path = None):
        self.tl = tl
        self.bl = bl
        self.tr = tr
        self.br = br
        self.img_path= img_path

    def current(self,screenshot):
        screenshot_crop = screenshot[self.tl:self.bl,self.tr:self.br]
        return screenshot_crop




fold = Area(1352, 1450, 1180, 1350)
card1 = Area(655,765,565,630)


fold_path = "/Users/ezracitron/my_projects/learning/py-autogui/fold.png"
fold_img = cv.imread(fold_path, cv.IMREAD_GRAYSCALE)

while True:
    screenshot = pyautogui.screenshot().convert("RGB")
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    cv.imwrite("tmp/screenshot.png", screenshot)
    # print(screenshot.size)
    # print(fold)

    screenshot_fold = screenshot[fold.tl : fold.bl, fold.tr : fold.br]
    # print(screenshot_fold.size)
    # print(fold_img.size)

    if np.sum(fold_img - screenshot_fold) < 100:
        print("press fold")
        time.sleep(random() / 5)
        pyautogui.moveTo(630+random()*2, 700+random()*2, duration=random() * 2, tween=pyautogui.easeInOutQuad)
        time.sleep(random() / 10)
        pyautogui.click()
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.moveTo(
            currentMouseX + random() * 100,
            currentMouseY + random() * 100,
            duration=random(),
            tween=pyautogui.easeInOutQuad,
        )

    else:
        print("Nothing to do")

    time.sleep(3)
