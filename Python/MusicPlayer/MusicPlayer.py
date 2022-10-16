# Importing all Modules
import os

import pygame
import pygame.mixer as mixer
from tkinter import *
from tkinter import filedialog

mixer.init()  # Initializing mixer


def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    try:
        song_name.set(songs_list.get(ACTIVE))

        mixer.music.load(songs_list.get(ACTIVE))
        mixer.music.play()

        status.set("Song Playing")
        btn_enable()

    except pygame.error:
        status.set("Select a Song")


def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song Stopped")


def btn_enable():
    stop_btn.config(state=ACTIVE)
    resume_btn.config(state=ACTIVE)
    pause_btn.config(state=ACTIVE)


def load(listbox):
    try:
        os.chdir(filedialog.askdirectory(title="Select a Folder"))

        tracks = os.listdir()

        for track in tracks:
            listbox.insert(END, track)
        play_btn.config(state=ACTIVE)
    except OSError:
        pass


def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song Paused")


def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song Resumed")


# initializing root window
root = Tk()
root.title("Music Player")
root.geometry("700x250")
root.resizable(0, 0)

# Creating Frames

song_frame = LabelFrame(root, text="Current Song", bg="LightBlue", width=400, height=80)
song_frame.place(y=0, x=0)

button_frame = LabelFrame(root, text="Control Buttons", bg="Turquoise", width=400, height=150)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text="Playlist", bg="RoyalBlue")
listbox_frame.place(x=400, y=0, height=250, width=300)

current_song = StringVar(root, value="<Not Selected>")
song_status = StringVar(root, value="<Not Available>")


# PlayLIst ListBox
playlist = Listbox(listbox_frame, font=("consolas", 11), selectbackground="red")

scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=BOTH)


playlist.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=playlist.yview)

playlist.pack(fill=BOTH, pady=5, padx=5)

# Song Frame
Label(song_frame, text="Currently Playing : ", bg="green", font=("consolas", 10, "bold")).place(x=5, y=20)

song_lbl = Label(song_frame, textvariable=current_song, bg="red", font=("consolas", 10), width=25)
song_lbl.place(x=150, y=20)

# Buttons
pause_btn = Button(button_frame, text="Pause", bg="white", font=("consolas", 13), width=7, state=DISABLED,
                   command=lambda : pause_song(song_status))
pause_btn.place(x=15, y=10)

stop_btn = Button(button_frame, text="Stop", bg="white", font=("consolas", 13), width=7, state=DISABLED,
                  command=lambda : stop_song(song_status))
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, text="Play", bg="white", font=("consolas", 13), width=7, state=DISABLED,
                  command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, text="Resume", bg="white", font=("consolas", 13), width=7, state=DISABLED,
                  command=lambda: resume_song(song_status))
resume_btn.place(x=285, y=10)

load_btn = Button(button_frame, text="Load", bg="white", font=("consolas", 13), width=40,
                  command=lambda: load(playlist), padx=5, pady=5)
load_btn.place(x=10, y=55)


# Label for bottom display status of song
Label(root, textvariable=song_status, bg="yellow", font=("consolas", 10), justify=LEFT).pack(side=BOTTOM, fill=X)

root.update()
root.mainloop()
