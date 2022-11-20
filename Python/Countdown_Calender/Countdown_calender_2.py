from tkinter import *
from datetime import date, datetime


def check():
    today = date.today()
    events = event.get()
    eve_date = event_date.get()
    try:
        eventDate = datetime.strptime(eve_date, '%d/%m/%Y').date()

        days_count = str(eventDate - today).split(',').pop(0)
        display = f"{days_count} left for the {events}."
        # print(display)
        count_label = Label(root, text=display, font=('comic sans MS', 20, 'bold underline'), bg='black', fg='orange')
        count_label.place(x=100, y=400)
    except ValueError:
        pass

root = Tk()
root.config(bg="black")
root.geometry('600x500')
root.title("Countdown Calender")
event = StringVar()
event_date = StringVar()


Label(root, text='Countdown Calender', font=('comic sans MS', 40, 'bold underline'),
      bg='black', fg='white').place(x=30, y=10)


event_label = Label(root, text='Enter Event Name : ', bg='Black', fg='white', font=('comic sans MS', 15, 'bold'))
event_label.place(x=1, y=120)

event_entry = Entry(root, textvariable=event, width=50, font=10)
event_entry.place(x=5, y=150, relheight=0.07)


date_label = Label(root, text='Enter Event Date :', bg='black', fg='white', font=('comic sans MS', 15, 'bold'))
date_label.place(x=1, y=200)

date_entry = Entry(root, textvariable=event_date, width=50, font=10)
date_entry.place(x=5, y=230, relheight=0.07)

Button(root, text='CHECK', bg='orange', activebackground='dark orange',
       width=20, height=2, command=check,
       pady=10, padx=10).place(x=200, y=300)


root.mainloop()
