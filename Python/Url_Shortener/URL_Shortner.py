import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.title("URL_Shortener")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="#ffe476")

url = StringVar()
url_address = StringVar()


def url_shortener():

    address = url.get()  # get value from url
    url_short = pyshorteners.Shortener().tinyurl.short(address)  # shorten the url

    url_address.set(url_short)  # set the value to shortened url


def copy_url():
    url_short = url_address.get()
    pyperclip.copy(url_short)  # copy the value to clipboard


Label(root, text="URL Shortener", font=("Consolas", 20), bg="#ffe476", fg="red").pack()

# Frame 1
link = Frame(root).pack(pady=10)

Label(link, text="Paste Your Link Here", font=("Consolas", 15), bg="#ffe476", fg="blue").pack(anchor=W)
Entry(link, textvariable=url, width=30, font=("consolas", 15)).pack()
Button(link, text="Short", font=("Consolas", 15), width=10, command=url_shortener).pack(pady=10)


# Frame 2
short_link = Frame(root).pack(pady=5)

Label(short_link, bg="#ffe476", text="Shortened Link",  font=("Consolas", 15), fg="blue").pack(anchor=W)
Entry(short_link, textvariable=url_address, font=("consolas", 15), width=30).pack()
Button(short_link, text="Copy", font=("Consolas", 15), command=copy_url, width=10).pack(pady=10)


root.mainloop()
