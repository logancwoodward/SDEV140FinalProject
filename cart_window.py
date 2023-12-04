# cart_window.py

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

        #button to exit the cart window
        self.button_exit = tk.Button(master, text="Exit", command=self.button_exit_action)
        self.button_exit.pack(pady=5)

        #update the listbox with cart items
        self.update_listbox()

    def button_exit_action(self):
        #action for Exit
        self.master.destroy()

    @classmethod
    def add_to_cart(cls, item):
        # class method to add an item to the cart
        cls.cart_items.append(item)

        #update the listbox in all instances of CartWindow
        for instance in cls._instances:
            instance.update_listbox()

    def update_listbox(self):
        #clear and update the listbox with cart items
        self.listbox.delete(0, tk.END)
        for item in self.cart_items:
            self.listbox.insert(tk.END, item)