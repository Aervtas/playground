import tkinter as tk
import requests
from PIL import Image, ImageTk

def get_image_urls(board, thread_id):
    api_url = f"https://a.4cdn.org/{board}/thread/{thread_id}.json"
    response = requests.get(api_url)
    data = response.json()

    image_urls = []
    for post in data["posts"]:
        if "tim" in post and "ext" in post:
            image_url = f"https://i.4cdn.org/{board}/{post['tim']}{post['ext']}"
            image_urls.append(image_url)

    return image_urls

def download_images(image_urls):
    images = []
    for url in image_urls:
        response = requests.get(url, stream=True)
        response.raw.decode_content = True
        image = Image.open(response.raw)
        image = image.resize((100, 100))  # Adjust the size as per your needs
        images.append(ImageTk.PhotoImage(image))

    return images

def update_images():
    selected_board = board_var.get()
    thread_id = thread_entry.get()

    if selected_board and thread_id:
        image_urls = get_image_urls(selected_board, thread_id)
        images = download_images(image_urls)

        # Clear existing images
        for label in image_labels:
            label.grid_forget()
        image_labels.clear()

        # Display new images
        columns = 3  # Number of columns in the grid
        for i, image in enumerate(images):
            row = i // columns
            column = i % columns
            label = tk.Label(root, image=image)
            label.grid(row=row, column=column)
            image_labels.append(label)

# Create the main window
root = tk.Tk()

# Board selection
board_var = tk.StringVar()
board_label = tk.Label(root, text="Board:")
board_label.grid(row=0, column=0, sticky=tk.E)
board_entry = tk.Entry(root, textvariable=board_var)
board_entry.grid(row=0, column=1)

# Thread ID input
thread_label = tk.Label(root, text="Thread ID:")
thread_label.grid(row=1, column=0, sticky=tk.E)
thread_entry = tk.Entry(root)
thread_entry.grid(row=1, column=1)

# Update button
update_button = tk.Button(root, text="Update Images", command=update_images)
update_button.grid(row=2, column=0, columnspan=2)

# Image labels
image_labels = []

# Run the main event loop
root.mainloop()
