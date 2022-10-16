from tkinter import *
import random as rd


def next_turn(row, col):

    reset.config(state=ACTIVE)
    global player

    if buttons[row][col]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][col]["text"] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=f"{players[1]}'s turn")
            elif check_winner() is True:
                label.config(text=f"{players[0]} Wins!")
            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:
            buttons[row][col]["text"] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=f"{player[0]}'s turn")
            elif check_winner() is True:
                label.config(text=f"{players[1]} Wins!")
            elif check_winner() == "Tie":
                label.config(text="Tie!")


def check_winner():

    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "" :
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")

            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "" :
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty_space() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="yellow")
        return "Tie"
    else:
        return False


def empty_space():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = rd.choice(players)
    label.config(text=f"{player}'s Turn")

    reset.config(state=DISABLED)

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#f0f0f0")



root = Tk()
root.title("Tic-Tac-Toe")
root.resizable(0,0)
root.geometry("360x500")
root.config()

players = ["x", "o"]
player = rd.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=f"{player}'s Turn", font=("consolas",40))
label.pack()

reset = Button(text="restart", font=("consolas",10), command=new_game,state=DISABLED)
reset.pack(side="top",expand=True)
frame = Frame(root)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=("consolas",30),
                                   width=5, height=2,relief="groove",
                                   command= lambda row=row, col=col:next_turn(row, col)
                                   )
        buttons[row][col].grid(row=row, column=col)


root.mainloop()