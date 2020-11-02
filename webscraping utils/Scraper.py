import tkinter as tk

window = tk.Tk()
window.title("Image Scraper")

entry = tk.Entry(width=50)

def handle_click(event):
    url = entry.get()
    print(url)

button = tk.Button(text="Search")
button.bind("<Button-1>", handle_click)

entry.place(x=0,y=0)
button.place(x=420,y=0)

window.mainloop()
