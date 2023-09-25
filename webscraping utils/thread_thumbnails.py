import requests
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import tempfile
import math

def get_thread_thumbnails(board, thread_id):
    url = f"https://a.4cdn.org/{board}/thread/{thread_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        thread_data = response.json()
        thumbnails = []
        for post in thread_data["posts"]:
            if "tim" in post and "ext" in post:
                thumbnail_url = f"https://i.4cdn.org/{board}/{post['tim']}s{post['ext']}"
                thumbnails.append(thumbnail_url)
        return thumbnails
    else:
        return None

def calculate_thumbnail_size(frame, num_columns, num_thumbnails):
    available_width = frame.winfo_width()
    thumbnail_size = math.floor(available_width / num_columns)
    return thumbnail_size

def calculate_aspect_ratio_size(image_size, thumbnail_size):
    width, height = image_size
    if width > height:
        ratio = thumbnail_size / width
        width = thumbnail_size
        height = math.floor(height * ratio)
    else:
        ratio = thumbnail_size / height
        height = thumbnail_size
        width = math.floor(width * ratio)
    return width, height

def display_thumbnails(board, thread_id):
    thumbnails = get_thread_thumbnails(board, thread_id)
    if thumbnails is None:
        print("Error fetching thread data")
        return

    root = tk.Tk()
    root.title("4chan Thread Thumbnails")
    
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    # Calculate the optimal thumbnail size based on the number of columns
    num_columns = 5
    thumbnail_size = calculate_thumbnail_size(frame, num_columns, len(thumbnails))

    for i, thumbnail_url in enumerate(thumbnails):
        response = requests.get(thumbnail_url)
        if response.status_code == 200:
            image_data = response.content

            # Save image data to a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file.write(image_data)
            temp_file.close()

            # Open the image using PIL
            image = Image.open(temp_file.name)

            # Calculate the size based on the aspect ratio
            width, height = calculate_aspect_ratio_size(image.size, thumbnail_size)

            # Resize the image
            image = image.resize((width, height))

            # Create a Tkinter-compatible photo image
            photo = ImageTk.PhotoImage(image)

            # Create a label with the photo image
            label = ttk.Label(frame, image=photo)
            label.grid(row=i // num_columns, column=i % num_columns, padx=5, pady=5)
            label.image = photo

    root.mainloop()

# Example usage
display_thumbnails("wg", 7979395)
