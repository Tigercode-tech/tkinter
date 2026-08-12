import tkinter
from time import strftime
cleen = tkinter.Tk()
cleen.title('Clock')
cleen.geometry('500x125')
cleen.config(bg = '#bd691a')
clabel = tkinter.Label (cleen, bg = 'orange', fg = 'white',font = ('alien dude', 48, 'bold') )
clabel.place(x= 62, y = 25)
def clock():
    time = strftime('%H:%M:%S:%p')
    clabel.config(text = time)
    clabel.after(1000, clock)
clock()
cleen.mainloop()