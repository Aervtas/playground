import tkinter as tk
import json

def add_text_to_json():
    # Get the text from the text box
    text = text_entry.get()

    # Load existing data from the JSON file
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Add the text to the data list
    data["text"].append(text)

    # Save the updated data to the JSON file
    with open("data.json", "w") as file:
        json.dump(data, file)

    # Clear the text box
    text_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()

# Create a label and pack it
label = tk.Label(root, text="Enter Text:")
label.pack()

# Create a text entry widget
text_entry = tk.Entry(root)
text_entry.pack()

# Create a button to add text to JSON
button = tk.Button(root, text="Add Text", command=add_text_to_json)
button.pack()

# Run the main event loop
root.mainloop()
