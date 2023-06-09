import tkinter as tk
import pyshorteners
import pyperclip


def shorten_url():
    long_url = url_entry.get()
    short = pyshorteners.Shortener()
    short_url = short.tinyurl.short(long_url)
    shortened_label.config(text=short_url)
    return short_url


def copy_to_clipboard():
    clipboard_url = shorten_url()
    pyperclip.copy(clipboard_url)


# Create tkinter widgets here and set callbacks as needed


window = tk.Tk()
window.title("URL Shortener")
window.geometry("450x100")

url_label = tk.Label(window, text="Enter URL:")
url_label.grid(column=0, row=0)

url_entry = tk.Entry(window, width=30)
url_entry.grid(column=1, row=0)

shorten_button = tk.Button(window, text="Shorten", command=shorten_url)
shorten_button.grid(column=2, row=0)

shortened_label = tk.Label(window, text="")
shortened_label.grid(column=1, row=1)

copy_button = tk.Button(window, text="Copy", command=copy_to_clipboard)
copy_button.grid(column=2, row=1)

window.mainloop()
