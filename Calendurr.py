import calendar
import tkinter
calendarr = calendar.calendar(2026)
ccreen = tkinter.Tk()
ccreen.title('Calendar')
ccreen.geometry('500x500')
label = tkinter.Label(ccreen, text = 'Enter the year', fg = 'black', bg = 'white' )
label.place(x = 250, y = 200)
entry = tkinter.Entry(ccreen, fg = 'black', bg = 'white')
entry.place(x = 250, y = 250)
def click():
    year = entry.get()
    print(calendar.calendar(int(year)))
button = tkinter.Button(ccreen, text = 'Confirm', fg = 'black', bg = 'white', command = click)
button.place(x = 250, y = 300)
ccreen.mainloop()