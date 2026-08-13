import tkinter
from tkinter import messagebox
import random
computernum = random.randint(0 , 20)
def welcome():
    next = NGGtry.get()
    messagebox.showinfo("H̴̨̧̙͉̻̲̲̭̣̜̹̄͛̎́̾̅̒̏̆̔̃͌́͋̅͛̓̉̚͠͝ë̷͓͕̘̳̲͉͍́̄̓̀̈́͂̈́̍̏͂͐̊̎̒͒̄͘͠͠l̸̯͚͓̦̺̭̟̼͇̻̭̪͕͚̱̇̏̋̽̈́̓̉ͅͅļ̵̡̨̬̙̹͔̲͙͚̭̙͔͉̲̜̘̦̘͔̊̈͋̈̔͂̐̆̽̑́̓̉͊̾̈́͒̕͘͜ọ̸̓̑̂̇͊̊", "Hello "+next+" Welcome to the Number Guesing Game!\nI am thinking of a number between 1 and 20")
def verify():
    global computernum
    before = int(nggtry.get())
    if before < computernum:
            messagebox.showinfo('👎', 'The number is lower')
    elif before > computernum:
         messagebox.showinfo('👎', 'The number is higher')
    else:
         messagebox.showinfo('👍', 'Correct!')
         computernum = random.randint(0 , 20)
nggeen = tkinter.Tk()
nggeen.title('Number Guessing Game')
nggeen.geometry('500x500')
nggeen.config(bg = 'light blue')
nggabel = tkinter.Label(nggeen, text = 'Enter a number', fg = 'purple', bg = 'white' )
nggabel.place(x = 12, y = 260)
nggutton = tkinter.Button(nggeen, text = 'Guess', cursor = 'hand2', command = verify)
nggutton.place(x = 150, y = 300)
nggtry = tkinter.Entry (nggeen, bg = 'white', fg = 'black')
nggtry.place(x = 12, y = 300)
NGGabel = tkinter.Label(nggeen, text = "What's your name?", fg = 'purple', bg = 'white' )
NGGabel.place(x = 12, y = 90)
NGGtry = tkinter.Entry (nggeen, bg = 'white', fg = 'black')
NGGtry.place(x = 12, y = 120)
NGGutton = tkinter.Button(nggeen, text = 'Confirm', cursor = 'hand2', command = welcome)
NGGutton.place(x = 145, y = 120)
nggeen.mainloop()