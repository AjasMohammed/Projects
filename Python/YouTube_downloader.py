from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from pytube import YouTube
from pytube.cli import on_progress


def dowmloader():
    url = YouTube(str(link.get()), on_progress_callback=on_progress)
    save_path = filedialog.asksaveasfilename(initialdir='C:/Users/Anandhu/Downloads', defaultextension='.mp4')
    video = url.streams[1].download(save_path)
    showinfo('Details', message='Download Completed.')


root = Tk()
root.title('YT Video Downloader')
root.geometry('600x400')
root.resizable(0, 0)
root.config(bg='#ffe396')

icon = PhotoImage(file='PY.png')
root.iconphoto(True,icon)

link = StringVar()

label = Label(root, text='Youtube Video Downloader', font=('ink free', 30, 'bold'), fg='red', bg='#ffe396')
label.pack()

link_label = Label(root, text='Enter Link : ', font=('ink free', 15, 'bold'), fg='dark blue', bg='#ffe396')
link_label.place(x=2, y=120)

search_bar = Entry(root, textvariable=link, relief=FLAT, font=15)
search_bar.place(x=30, y=150, relwidth=0.9, relheight=0.07)

download_btn = Button(root, text='Download', padx=30, pady=8, command=dowmloader,
                      relief=FLAT, bg='#3b86cc', activebackground="#1d466e")
download_btn.place(x=250, y=200)

root.mainloop()
