import tkinter as tk

def open_new_window():
    # Create a new window
    new_window = tk.Toplevel(root)
    
    # Hide the main window
    root.withdraw()
    
    # Center the new window on the screen
    new_window.geometry("300x200")
    new_window.title("New Window")
    
    # Restore the main window when the new window is closed
    new_window.protocol("WM_DELETE_WINDOW", lambda: close_window(new_window))

def close_window(window):
    # Destroy the new window
    window.destroy()
    
    # Restore the main window
    root.deiconify()

# Create the main window
root = tk.Tk()
root.geometry("300x200")
root.title("Main Window")

# Create a button to open a new window
button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack(pady=50)

# Run the main event loop
root.mainloop()
