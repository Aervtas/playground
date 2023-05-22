# test to open file manager

import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file:", file_path)

# Create the main window
root = tk.Tk()

# Create a button to open the file dialog
button = tk.Button(root, text="Open File", command=open_file_dialog)
button.pack(padx=20, pady=10)

# Run the main event loop
root.mainloop()
