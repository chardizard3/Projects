#A small project that makes a simple GUI that can make a list, add, remove,
# and delete a list

import tkinter as tk
from tkinter import ttk

#GUI PARAMETERS
main = tk.Tk() #initialize tkinter
main.title("List Project") #naming main window
#window dimensions
window_width = 500
window_height = 500
# get the screen dimension
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
#centers window
main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') 
#Allow resizing of main window
main.resizable(True, True) 

"""
#GRID
# configure the grid

#textbox
textbox_entry = ttk.Entry(main)
textbox_entry.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

#add button
add_button = ttk.Button(main, text="Add")
add_button.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

#remove button
remove_button = ttk.Button(main, text="Remove")
remove_button.grid(column=2, row=1, sticky=tk.E, padx=5, pady=5)



"""

#SettingsMenu
def exit():
    exit()
def on_settings_change(event):
    selected_setting = settings_combobox.get()
    # Do something with the selected setting
    print(f"Selected setting: {selected_setting}")

settings_options = ["Option 1", "Option 2", "Option 3", "Option 4"]

settings_combobox = ttk.Combobox(main, values=settings_options)
settings_combobox.set(settings_options[0])  # Set the default selection
settings_combobox.bind("<<ComboboxSelected>>", on_settings_change)
settings_combobox.pack(pady=10)


main.mainloop()