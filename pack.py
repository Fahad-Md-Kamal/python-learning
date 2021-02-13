from tkinter import *

parent = Tk()

window = Label(parent, width='40', height='15')
window.pack()

redbutton = Button(parent, text = 'Red', fg= 'red')
redbutton.pack(side=LEFT)
greebutton = Button(parent, text='Black', fg='black')
greebutton.pack(side=RIGHT)
blueButton = Button(parent, text='Blue', fg='blue')
blueButton.pack(side=TOP)
blackButton= Button(parent, text= 'Green', fg='red')
blackButton.pack(side=BOTTOM)
parent.mainloop()
