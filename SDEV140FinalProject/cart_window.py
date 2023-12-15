# cart_window.py

"""This module deals with the cart. Users could send items from the backstock locations to the cart. Items sent to the cart are displayed in a list box, until the 
cart is emptied, using the 'Clear cart' button."""

from PIL import Image, ImageTk
import tkinter as tk


class CartWindow:
    cart_items = []
    _instances = []

    def __init__(self, master):
        self.master = master
        master.title("Cart Window")

        #label to display prompt
        self.prompt_label = tk.Label(master, text="Items in the Cart", font=("Arial", 14))
        self.prompt_label.pack(pady=10)
        self._instances.append(self)

        #listbox to display cart items
        self.listbox = tk.Listbox(master)
        self.listbox.pack(pady=10)

        #button to clear the cart
        original_image = Image.open("final\SDEV140FinalProject\shopping_cart_PNG46.png")
        resized_image = original_image.resize((30, 30))
        self.clear_cart_image = ImageTk.PhotoImage(resized_image)
        self.button_clear_cart = tk.Button(master, text="Clear Cart", command=self.clear_cart, image=self.clear_cart_image, compound=tk.LEFT)
        self.button_clear_cart.image = self.clear_cart_image
        self.button_clear_cart.pack(pady=5)

        #button to exit the cart window
        self.button_exit = tk.Button(master, text="Exit", command=self.button_exit_action)
        self.button_exit.pack(pady=5)

        #update the listbox with cart items
        self.update_listbox()

    def button_exit_action(self):
        #action for Exit
        self.master.destroy()
    
    def clear_cart(self):
        #method to clear the cart
        self.cart_items = []
        #update the listbox in all instances of CartWindow
        for instance in self._instances:
            instance.update_listbox()

    @classmethod
    def add_to_cart(cls, item):
        #class method to add an item to the cart
        cls.cart_items.append(item)

        #update the listbox in all instances of CartWindow
        for instance in cls._instances:
            instance.update_listbox()

    def update_listbox(self):
        #clear and update the listbox with cart items
        self.listbox.delete(0, tk.END)
        for item in self.cart_items:
            self.listbox.insert(tk.END, item)