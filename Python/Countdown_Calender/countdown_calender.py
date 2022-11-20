from tkinter import *
from datetime import date, datetime


def get_events():
    events = []
    with open('event.txt') as file:
        for lines in file.readlines():
            event = lines.strip().split(',')
            event_date = datetime.strptime(event[1], '%d/%m/%Y').date()
            event[1] = event_date
            events.append(event)
    return events


def day_count(date1, date2):

    time_between_dates = str(date1 - date2)
    no_days = time_between_dates.split(' ')
    return no_days[0]


root = Tk()

canvas = Canvas(root, width=800, height=800, bg='black')
canvas.pack()

canvas.create_text(100, 50, text='Countdown Calendar', font=('comic sans MS', 40, 'bold underline'),
                   fill="Ghost white", anchor='w')

events = get_events()
today = date.today()

space = 200
for event in events:
    programme = event[0]
    no_days = day_count(event[1], today)

    display = f'*   {no_days} to go for {programme}'

    canvas.create_text(100, space, text=display, fill='ghostwhite', font=('comic sans MS', 20, 'bold'), anchor='w')
    space += 50

root.mainloop()
