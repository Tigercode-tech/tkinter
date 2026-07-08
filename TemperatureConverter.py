import tkinter
treen = tkinter.Tk()
treen.title('Temperature konverter')
treen.geometry('500x500')
treen.config(bg = 'red')
def convert():
    temp = int(word.get())
    talue = temp * 1.8 + 32
    taluething = tkinter.Label (treen, bg = 'black', fg = 'white', text = str(talue) + ' degrees Fahrenheit')
    taluething.place(x = 250, y = 300 )
word = tkinter.Entry (treen, bg = 'black', fg = 'white')
word.place(x = 300, y = 200 )
table = tkinter.Label (treen, bg = 'black', fg = 'white', text = 'Enter temperature in celsius')
table.place(x= 100, y = 200)
tabel = tkinter.Label (treen, bg = 'black', fg = 'white', text = 'Celsius -> Fahrenheit')
tabel.place(x= 100, y = 50)
tutton = tkinter.Button (treen, bg = 'black', fg = 'green', text = 'Convert', command = (convert))
tutton.place(x = 250, y =400 )
treen.mainloop()