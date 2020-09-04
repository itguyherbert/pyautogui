import pyautogui
cards = int(input("How many cards do you want to disenchant?"))
for x in range(cards):
    pyautogui.moveTo(426, 296, 0.3)
    pyautogui.click(button='right')
    pyautogui.moveTo(792, 919, 0.3)
    pyautogui.click()
    pyautogui.moveTo(874, 646, 0.3)
    pyautogui.click()
    pyautogui.moveTo(792, 919, 0.3)
    pyautogui.click()
    pyautogui.moveTo(171, 469, 0.3)
    pyautogui.click()