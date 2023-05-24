import tkinter as tk
import json
from thread_status import url_helper

def load_data():
    # Load data from the JSON file
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"url": [], "archived_url": []}

    return data

def update_status():
    remove_list = []
    for i in range(len(data["url"])):
        if url_helper(data["url"][i]):
            data["archived_url"].append(data["url"][i])
            remove_list.append(data["url"][i])
    data["url"] = [i for i in data["url"] if i not in remove_list]
    save_data(data)

def save_data(data):
    # Save data to the JSON file
    with open("data.json", "w") as file:
        json.dump(data, file)

def add_text():
    text = text_entry.get()
    data["url"].append(text)
    save_data(data)
    update_status()
    refresh_lists()
    text_entry.delete(0, tk.END)

def refresh_lists():
    # Clear the existing lists
    listbox1.delete(0, tk.END)
    listbox2.delete(0, tk.END)
    update_status()

    # Add items from the data to the lists
    for item in data["url"]:
        listbox1.insert(tk.END, item)

    for item in data["archived_url"]:
        listbox2.insert(tk.END, item)

def launch_new_window(event):
    selected_item = listbox2.get(listbox2.curselection())
    new_window = tk.Toplevel(root)
    new_window.title("Selected Item")
    label = tk.Label(new_window, text=selected_item)
    label.pack()

# Load initial data from the JSON file
data = load_data()

# Create the main window
root = tk.Tk()

# Create a label and pack it
label = tk.Label(root, text="Enter Text:")
label.pack()

# Create a text entry widget
text_entry = tk.Entry(root)
text_entry.pack()

# Create a button to add text to active threads
button = tk.Button(root, text="Add URL", command=add_text)
button.pack()

# Create a button to refresh status of all active urls
button = tk.Button(root, text="Refresh", command=refresh_lists)
button.pack()

# Create a label for Column 1
column1_label = tk.Label(root, text="Active")
column1_label.pack()

# Create a listbox for Column 1
listbox1 = tk.Listbox(root)
listbox1.pack()

# Create a label for Column 2
column2_label = tk.Label(root, text="Archived")
column2_label.pack()

# Create a listbox for Column 2
listbox2 = tk.Listbox(root)
listbox2.pack()

# Bind the launch_new_window function to listbox item selection
listbox2.bind("<<ListboxSelect>>", launch_new_window)

# Refresh the lists initially
refresh_lists()

# Run the main event loop
root.mainloop()
