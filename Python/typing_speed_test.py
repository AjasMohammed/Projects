from tkinter import *
from timeit import default_timer as timer
import random


def game():

    window.pack(fill='both', expand=True)
    new.pack_forget()

    def check_result():
        if entry.get() == words[word]:

            end = timer()

            print(f'{round ( end - start )} Seconds..')

        else:
            print("Wrong input...")

    words = ["programming", "coding", 'algorithm', 'systems', 'python', 'software']

    word = random.randint(0, len(words)-1)

    start = timer()

    title_label = Label(window, text="Start Typing", font=("consolas", 20))
    title_label.place(x=150, y=10)

    word_label = Label(window, text=f"Type:\n\t{words[word]}", font="consolas 15", padx=0)
    word_label.place(x=1, y=50)

    entry = Entry(window, font='consolas 15')
    entry.place(x=220, y=80)
    entry.focus()

    submit_btn = Button(window, text='Done', command=check_result, font='consolas 15')
    submit_btn.place(x=150, y=150)

    tryagain_btn = Button(window, text='Try Again', command=game, font='consolas 15')
    tryagain_btn.place(x=250, y=150)
    window.mainloop()


root = Tk()
root.title("Typing Speed Tester")
root.geometry("450x200")

window = Frame(root)
new = Frame(root)
new.pack(fill="both", expand=True)

Label(new, text="Typing Speed Test", font="consolas 20").pack(expand=True)
Button(new, text="Start", font='consolas 20', command=game).pack(expand=True)

root.mainloop()
