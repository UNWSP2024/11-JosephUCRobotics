# Author: Joseph Kracht
# Last Modified: 11/13/2025
# Title: Buttons Display

import tkinter
class MyGUI:
    def __init__(self):
        # Create the main window`
        self.main_window = tkinter.Tk()

        # Display a Title
        self.main_window.title("Button Test")

        # Create a show info button
        self.my_button = tkinter.Button(self.main_window, text="Show Info", command=self.on_button_click)
        self.my_button.pack(pady=10, padx=50)

        # Create a exit button
        self.my_exit_button = tkinter.Button(self.main_window, text="Exit", command=self.close_window)
        self.my_exit_button.pack(pady=10, padx=50)

        # Create a label but don't pack it
        self.label = tkinter.Label(self.main_window, text="Name: Joseph\nAddress: 1002 Fake Ave")

        # Enter the main loop
        tkinter.mainloop()

    def on_button_click (self):
        # Pack the label
        self.label.pack(pady=20, padx=50)

    def close_window(self):
        # Close the window
        self.main_window.destroy()

my_gui = MyGUI()
