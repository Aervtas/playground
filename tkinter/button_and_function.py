import tkinter as tk

def button_click():
    # Function to execute when the button is clicked
    text = textbox.get("1.0", "end-1c")  # Get the text from the text box
    # Replace the following line with your desired program logic
    print("Button clicked! Text entered: ", text)

# Create the main window
window = tk.Tk()

# Create a label
label = tk.Label(window, text="Enter some text:")
label.pack()

# Create a text box
textbox = tk.Text(window, height=5, width=30)
textbox.pack()

# Create a button
button = tk.Button(window, text="Click me!", command=button_click)
button.pack()

# Run the main event loop
window.mainloop()
