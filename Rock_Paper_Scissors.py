import tkinter
import random
def compare():
    if value == 1 and computer == 3:
        win()
    elif value == 3 and computer == 1:
        lose()
    elif value > computer:
        win()
    elif value == computer:
        drawlabel = tkinter.Label (rpscreen, bg = 'white', fg = 'black', text = 'draw')
    else:
        lose()

rpscreen = tkinter.Tk()
rpscreen.title('Rock Paper Scissors')
rpscreen.geometry('500x500')
rpscreen.config(bg = 'white')
def press1():
    global value
    value = 3
def press2():
    global value
    value = 2
def press3():
    global value
    value = 1
rpsabel = tkinter.Label (rpscreen, bg = 'white', fg = 'black', text = 'Rock Paper Scissors')
rpsabel.place(x = 175, y = 25 )
rpsutton1 = tkinter.Button (rpscreen, bg = '#DB776B', fg = 'black', text = 'Rock', command = press1)
rpsutton1.place(x = 100, y =100 )
rpsutton2 = tkinter.Button (rpscreen, bg = 'light grey', fg = 'black', text = 'Paper', command = press3)
rpsutton2.place(x = 200, y =100 )
rpsutton3 = tkinter.Button (rpscreen, bg = 'light blue', fg = 'black', text = 'Scissors' command = press2)
rpsutton3.place(x = 300, y =100 )
computer = random.randint(1,3)
def win():
    winlabel = tkinter.Label()
rpscreen.mainloop()