# second_window.py

import tkinter as tk
import os
import json
from cart_window import CartWindow

class BackstockWindow:
    def __init__(self, master, location):
        self.master = master
        self.location = location
        self.filename = f"{location}_backstock.json"  #file to store backstock data
        master.title(f"Backstock - {self.location}")

        #string variable to store the prompt
        self.prompt_text = tk.StringVar()

        #label to display the prompt
        self.prompt_label = tk.Label(master, textvariable=self.prompt_text, font=("Arial", 14))
        self.prompt_label.pack(pady=10)

        #create UI
        self.button_backstock = tk.Button(master, text="Backstock", command=self.button_backstock_action)
        self.button_exit = tk.Button(master, text="Exit", command=self.button_exit_action)
        self.button_to_cart = tk.Button(master, text="To Cart", command=self.button_to_cart_action)
        self.input_entry = tk.Entry(master)

        #listbox to display backstock items
        self.listbox = tk.Listbox(master)
        self.listbox.pack(pady=10)

        #button pack
        self.input_entry.pack(pady=10)
        self.button_backstock.pack(pady=5)
        self.button_exit.pack(pady=5)
        self.button_to_cart.pack(pady=5)

        #set the initial prompt with the location
        self.set_prompt(f"Enter the item to place at {self.location}")

        #load backstock items from file or initialize an empty list
        self.backstock_items = self.load_backstock_items()

        #update the listbox with backstock items
        self.update_listbox()

    def set_prompt(self, text):
        #method to set the prompt text
        self.prompt_text.set(text)

    def button_backstock_action(self):
        #get the value from the Entry widget
        item = self.input_entry.get()

        #action for backstock
        self.backstock_items.append(item)
        self.set_prompt(f"{item} backstocked at {self.location}.")

        #update the listbox
        self.update_listbox()

        #save backstock items to file
        self.save_backstock_items()

    def button_exit_action(self):
        #action for Exit
        self.master.destroy()

    def button_to_cart_action(self):
        #move item to cart
        item = self.input_entry.get()
        CartWindow.add_to_cart(item)
        self.set_prompt(f"{item} moved to the cart at {self.location}.")

    def update_listbox(self):
        #clear and update the listbox with backstock items
        self.listbox.delete(0, tk.END)
        for item in self.backstock_items:
            self.listbox.insert(tk.END, item)

    def load_backstock_items(self):
        #load backstock items from file or return an empty list
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_backstock_items(self):
        #save backstock items to file
        with open(self.filename, 'w') as file:
            json.dump(self.backstock_items, file)
    def remove_item_from_backstock(self, item):
        #remove the item from backstock
        if item in self.backstock_items:
            self.backstock_items.remove(item)
            self.set_prompt(f"{item} removed from {self.location}.")

            #update the listbox
            self.update_listbox()

            #save backstock items to file
            self.save_backstock_items()

    def button_to_cart_action(self):
        #move item to cart
        item = self.input_entry.get()
        CartWindow.add_to_cart(item)
        self.remove_item_from_backstock(item)