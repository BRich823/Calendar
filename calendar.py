import event
import tkinter as tk
from tkinter import ttk

class Calendar:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar")
        self.master.geometry("500x500")
        self.master.resizable(False, False)
        self.master.configure(bg="white")
        self.events = []
        self.create_widgets()
        self.create_calendar()

    def create_widgets(self):
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        
if __name__ == "__main__":
    root = tk.Tk()
    cal = Calendar(root)
    root.mainloop()
    