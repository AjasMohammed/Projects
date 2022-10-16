from tkinter import *
from tkinter import filedialog
import os
import pygame
import pygame.mixer as mixer


mixer.init()

track_list = []
tracks = []
track_names = []


def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    try:
        song_name.set(songs_list.get(ACTIVE))

        mixer.music.load(songs_list.get(ACTIVE))
        mixer.music.play(-1)

        status.set("Song Playing")

        play_btn.config(command=lambda: pause_song(song_status), image=pause_icon)

    except pygame.error:
        status.set("Select a Song")

next = None


def next_track():
    global next
    next = tracks.index(str(current_song.get()))
    try:
        nexttrack = tracks[next+1]
    except IndexError:
        next = 0
    else:
        current_song.set(nexttrack)
        mixer.music.load(current_song.get())
        try:
            mixer.music.play()
        except pygame.error:
            pass

prev = None


def prev_track():
    global prev
    prev = tracks.index(str(current_song.get()))
    try:
        prevtrack = tracks[prev-1]
    except IndexError:
        prev = -1
    else:
        current_song.set(prevtrack)
        mixer.music.load(current_song.get())
        try:
            mixer.music.play()
        except pygame.error:
            pass


def load(listbox):
    global track_list, tracks, track_names

    try:
        os.chdir(filedialog.askdirectory(title="Select a Folder"))

        tracks = os.listdir()

        for track in tracks:
            listbox.insert(END, track)
            track_list.append(track)

        for track in track_list:
            tracks.append(track)
            track_names.append(track.split(".")[0])

    except OSError:
        pass


def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song Paused")

    play_btn.config(command=lambda: resume_song(song_status), image=play_icon)


def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song Stopped")
    play_btn.config(command=lambda: play_song(current_song, playlist, song_status), image=play_icon)
    current_song.set(value="")


def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song Resumed")

    play_btn.config(command=lambda: pause_song(song_status), image=pause_icon)


root = Tk()
root.geometry("500x500")
root.resizable(False, False)

current_song = StringVar(root, value="")
song_status = StringVar(root, value="<Not Available>")

# Buttons Icons
play_icon = PhotoImage(file="playbutton.png")
forward_icon = PhotoImage(file="forwardbutton.png")
prev_icon = PhotoImage(file="backwardbutton.png")
menu_icon = PhotoImage(file="menubtn.png")
pause_icon = PhotoImage(file="pausebtn.png")
stop_icon = PhotoImage(file="stopbtn.png")


display_frame = Frame(root)
display_frame.pack()

listbox_frame = LabelFrame(display_frame, text="PLAYLIST", width=500, height=250)
listbox_frame.pack()


playlist = Listbox(listbox_frame, selectbackground="blue", width=70, height=12)  # Creates a Listbox widget.

scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=playlist.yview)

playlist.pack()


# Button Frame
controls_frame = Frame(root, width=500, height=260, bg="blue")
controls_frame.pack()

Label(controls_frame, textvariable=current_song, bg="blue", font=("consolas", 15)).place(x=10, y=50)

# buttons

play_btn = Button(controls_frame, image=play_icon, borderwidth=0, activebackground="blue", bg="blue",
                  command=lambda : play_song(current_song, playlist, song_status))
play_btn.place(x=230, y=120)

forward_btn = Button(controls_frame, image=forward_icon, borderwidth=0, activebackground="blue", bg="blue",
                     command=next_track)
forward_btn.place(x=280, y=120)

prev_btn = Button(controls_frame, image=prev_icon, borderwidth=0, activebackground="blue", bg="blue",
                  command=prev_track)
prev_btn.place(x=180, y=120)


stop_btn = Button(controls_frame, image=stop_icon, borderwidth=0, activebackground="blue", bg="blue",
                  command=lambda: stop_song(song_status))
stop_btn.place(x=230, y=160)


menu_btn = Button(controls_frame, image=menu_icon, borderwidth=0, activebackground="blue", bg="blue",
                  command=lambda: load(playlist))
menu_btn.place(x=10, y=10)

# ellipse_icon = PhotoImage(file="Music/ellipsebtn.png")
# ellipse_btn = Menubutton(controls_frame, image=ellipse_icon, borderwidth=0, activebackground="blue", bg="blue")
# ellipse_btn.place(x=470, y=10)



root.mainloop()
