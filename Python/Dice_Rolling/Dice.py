import random
from tkinter import *
from PIL import Image, ImageTk
import random as rd




root = Tk()
root.title("Dice Rolling Simulator")
root.geometry("500x500")
root.config(bg="dark red")

Label(root, text='Roll The Dice', font=("Ariel", 30, 'bold'), bg="dark red", fg="white").pack(pady=20)

dice = ['dice_png/dice-1.png', 'dice_png/dice-2.png', 'dice_png/dice-3.png',
        'dice_png/dice-4.png', 'dice_png/dice-5.png', 'dice_png/dice-6.png']

dice_image = ImageTk.PhotoImage(Image.open(rd.choice(dice)).resize((200, 200)))

image_label = Label(root, image=dice_image, bg="dark red")
image_label.image = dice_image
image_label.pack(padx=10, pady=20)


def roll_dice():
    dice_image = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((200, 200)))
    image_label.configure(image=dice_image)
    image_label.image = dice_image


roll_btn = Button(root, text='Roll', command=roll_dice, font=("consoles", 20), width=10, bg='grey')
roll_btn.pack()


root.mainloop()
