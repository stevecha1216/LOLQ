import pyautogui as pag
import time
import keyboard

#search for accept button, then click it
searching = True
while searching:
    time.sleep(3)
    if keyboard.is_pressed("*"):
        searching = False
    acceptLoc = pag.locateOnScreen('accept.jpg', grayscale = True, confidence = 0.8)
    if acceptLoc is not None:
        acceptCenter = pag.center(acceptLoc)
        pag.moveTo(acceptCenter)
        pag.leftClick()
        print("Queue Accepted")
    else:
        print("Waiting for Queue...")






