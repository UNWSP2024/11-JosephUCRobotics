# Author: Joseph Kracht
# Last Modified: 11/13/2025
# Title: Display Quote

import tkinter
class MyGUI:
    def __init__(self):
        # Create the main window`
        self.main_window = tkinter.Tk()

        # Display a Title
        self.main_window.title("Quote Display")

        # Create a label
        self.label = tkinter.Label(self.main_window, text="Be Not Afraid")
        self.label.pack(pady = 50, padx= 50)

        # Enter the main loop
        tkinter.mainloop()

# Create an instance of the window
my_gui = MyGUI()
