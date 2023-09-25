import tkinter as tk
import os
from PIL import Image, ImageTk

def display_images_from_folder(folder_path):
    # Create the main window
    root = tk.Tk()

    # Get a list of image files in the folder
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))]

    # Iterate through the image files and display them in the window
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        
        # Open and resize the image
        image = Image.open(image_path)
        image.thumbnail((200, 200))  # Adjust the size as per your requirement

        # Create a PhotoImage from the temporary file
        photo = ImageTk.PhotoImage(image)

        # Create a label and display the image
        label = tk.Label(root, image=photo)
        label.pack()

    # Run the main event loop
    root.mainloop()

# Specify the folder path containing the images
folder_path = "/run/media/kevin/Storage/unsorted pictures/Women in Videogames"

# Call the function to display the images from the folder
display_images_from_folder(folder_path)
