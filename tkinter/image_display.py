import tkinter as tk
from PIL import ImageTk, Image

# Create the main window
root = tk.Tk()

# Load the image
image = Image.open("/run/media/kevin/Storage/unsorted pictures/Women in Videogames/1681731220326005.jpg")
image.thumbnail((300,300))
photo = ImageTk.PhotoImage(image)

# Create a label and set the image
label = tk.Label(root, image=photo)
label.pack()

# Load the image
image1 = Image.open("/run/media/kevin/Storage/unsorted pictures/Women in Videogames/1681567801136302.jpg")
image1.thumbnail((300,300))
photo1 = ImageTk.PhotoImage(image1)

# Create a label and set the image
label = tk.Label(root, image=photo1)
label.pack()

# Run the main event loop
root.mainloop()
