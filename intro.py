import tkinter
screen = tkinter.Tk()
screen.title('kT')
screen.geometry('500x400')
screen.config(bg = 'orange')
wig = tkinter.Label(screen, text = 'helo', fg = 'purple', bg = 'red' )
wig.place(x = 12, y = 90)
def pront():
    print(enty.get())
button = tkinter.Button(screen, bg = 'blue', fg = 'green', text = 'pres', cursor = 'hand2', activebackground = 'yellow', activeforeground = 'yellow', bd = 4, relief = 'groove', command = pront )
button.place(x = 70, y = 30)
enty = tkinter.Entry (screen, bg = 'black', fg = 'white')
enty.place(x = 200, y = 200)
screen.mainloop()