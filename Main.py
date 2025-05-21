import tkinter as tk
from Create_Display import create_widgets
from Update_Display import update_widgets
from Player import Player_Class

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.user_player = Player_Class()

        self.title("Clicker Game")
        self.geometry("960x540")

        for i in range(0, 3):
            self.rowconfigure(i, weight=1)
        for i in range(0, 4):
            self.columnconfigure(i, weight=1)

        # Build UI
        create_widgets(self)

        # Update widgets
        self.after(100, lambda: update_widgets(self))


if __name__ == "__main__":
    root = MainApp()
    root.mainloop()