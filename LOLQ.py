import tkinter as tk
from tkinter import *
import pyautogui as pag
import time
import keyboard

class LOLQ(tk.Tk):
    def __init__(self):
        super().__init__()

        self.searching = None
        self.title("LOLQ")
        self.geometry("250x150")

        self.lf = LabelFrame(self, text = "Click button to start or stop the Auto Accept program")
        self.lf.pack(expand = "yes", fill = "both")

        self.startButton = Button(self.lf, text = "Start", command = self.startCall)
        self.startButton.pack()

        self.stopButton = Button(self.lf, text = "Stop", command = self.stopCall)
        self.stopButton.pack()

        self.lf2 = LabelFrame(self, text = "Status")
        self.lf2.pack(expand = "yes", fill = "both")

        self.after(3000, self.autoAccept)
    
    def autoAccept(self):
        # search for accept button, then click it
        if self.searching:
            acceptLoc = pag.locateOnScreen('accept.jpg', grayscale=True, confidence=0.8)
            if acceptLoc is not None:
                acceptCenter = pag.center(acceptLoc)
                pag.moveTo(acceptCenter)
                pag.leftClick()
        self.after(1000, self.autoAccept)

    def startCall(self):
        #clear frame
        for widgets in self.lf2.winfo_children():
            widgets.destroy()
        #Display message
        self.msg = Message(self.lf2, text = "Running Auto Accept program")
        self.msg.pack()
        self.searching = True

    def stopCall(self):
        #clear frame
        for widgets in self.lf2.winfo_children():
            widgets.destroy()
        #display message
        self.msg = Message(self.lf2, text = "Auto Accept program is stopped")
        self.msg.pack()
        self.searching = False




if __name__ == "__main__":
    app = LOLQ()
    app.mainloop()
