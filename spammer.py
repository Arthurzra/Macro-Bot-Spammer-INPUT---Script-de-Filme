import pyautogui, time
time.sleep(5)
f = open("Patrick Bateman.txt.", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")




