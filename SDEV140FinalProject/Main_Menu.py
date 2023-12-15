"""Program Name: LoganWork
Author: Logan Woodward 
This program allows users to record where merchandise is stored in a retail backroom setting. Items can be placed into the
storage locations and can also be moved from storage to the cart. The cart represents what employees would take from the backrooms 
the salesfloor."""

# Main_Menu.py

import tkinter as tk
from second_window import BackstockWindow
from cart_window import CartWindow 

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Welcome to LoganWork")

        self.label = tk.Label(master, text="""Please enter what item you are placing in this location. 
                              Otherwise, enter an item and click 'To cart' to remove it from this location.""")
        self.label.pack()

        #buttons for different locations
        self.button_location1 = tk.Button(master, text="Location 1", command=lambda: self.open_second_window("Location 1"))
        self.button_location1.pack()

        self.button_location2 = tk.Button(master, text="Location 2", command=lambda: self.open_second_window("Location 2"))
        self.button_location2.pack()

        #button to view the cart
        self.button_view_cart = tk.Button(master, text="View Cart", command=self.view_cart)
        self.button_view_cart.pack()

    def open_second_window(self, location):
        second_window = tk.Toplevel(self.master)
        BackstockWindow(second_window, location)

    def view_cart(self):
        cart_window = tk.Toplevel(self.master)
        CartWindow(cart_window)



#startprogram
import tkinter as tk
from Main_Menu import MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()