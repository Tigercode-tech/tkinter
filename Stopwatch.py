import tkinter
import time 
stopscreen = tkinter.Tk()
stopscreen.title('Stopwatch & Counter')
stopscreen.geometry('200x200')
stopscreen.config(bg = 'light green')
hour = tkinter.StringVar()
hour.set('00')
hourstentry = tkinter.Entry(stopscreen, bg = 'white', fg = 'black', width = 5, textvariable = hour)
minute = tkinter.StringVar()
minute.set('00')
minutestentry = tkinter.Entry (stopscreen, bg = 'white', fg = 'black', width = 5, textvariable = minute)
seccond = tkinter.StringVar()
seccond.set('00')
seccondstentry = tkinter.Entry(stopscreen, bg = 'white', fg = 'black', width = 5, textvariable = seccond)
hourstentry.place(x = 30, y = 20)
minutestentry.place(x = 75, y = 20)
seccondstentry.place(x = 120, y = 20)
def convert():
    x = int(hourstentry.get())
    z = int(seccondstentry.get())
    y = int(minutestentry.get())
    w = x*3600+y*60+z
    while w > 0:
        v = w // 60
        u = w % 60
        if v >= 60:
            global t
            global s
            t = v // 60
            s = v % 60
        print(t,s,u)
        w -=1
        time.sleep(1)
stutton = tkinter.Button(stopscreen, fg = 'black', bg = 'white', text = 'Set time countdown', command = convert)
stutton.place(x = 37.5, y = 160)
stopscreen.mainloop()