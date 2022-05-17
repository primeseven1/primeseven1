from tkinter import *
import pyautogui as pg
import time

class Application(Tk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.geometry("300x300")
        self.resizable(width = False, height = False)
        self.title("Spam")

        # Label spam
        self.spam_label = Label(text = "What do you want to spam?")
        self.spam_label.pack()

        # Spam input
        self.spam_input = Entry()
        self.spam_input.pack()

        # Label times
        self.label_times = Label(text = "How many times?")
        self.label_times.pack()

        # Times input
        self.times_input = Entry()
        self.times_input.pack()

        # Warning
        self.warning = Label(text = "Warning: This will \n run in 5 seconds \n once you click \n this button")
        self.warning.pack()

        # Button
        self.start_button = Button(text = "Spam", command = self.setup)
        self.start_button.pack()

        # PyautoGUI settings
        pg.PAUSE = 0

    def setup(self):
        self.get_spam = self.spam_input.get()
        self.get_times = int(self.times_input.get())

        if self.get_times > 150 or self.get_times <= 0:
            self.times_input.delete(0, END)
            if self.get_times <= 0:
                self.times_input.insert(0, "Cannot be 0 or less")
            else:
                self.times_input.insert(0, "Cannot be more than 150")
        
        elif len(self.get_spam) > 18 or len(self.get_spam) <= 0:
            self.spam_input.delete(0, END)
            if len(self.get_spam) > 18:
                self.spam_input.insert(0, "Cannot be more than 18 characters")
            else:
                self.spam_input.insert(0, "Enter something here")
        
        else:
            self.main()
    
    def main(self):
        time.sleep(5)

        for i in range(self.get_times):
            pg.write(self.get_spam)
            pg.press("Enter")

if __name__ == "__main__":
    Application().mainloop()