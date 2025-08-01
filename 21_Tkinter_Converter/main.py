from tkinter import *

window = Tk()
window.title("My Converter")
window.minsize(width=500, height=400)

#Label
my_label = Label(text="My Label", font=("Helvetica", 24))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

#Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button1 = Button(text="New button")
button1.grid(column=2, row=0)

button = Button(text="My Button", font=("Helvetica", 24), command=button_clicked)
# button.pack()
# button.place(x=0, y=50)
button.grid(column=1, row=1)

#Entry
input = Entry(width=10)
# input.pack(
# input.place(x=0, y=100)
input.grid(column=3, row=2)




window.mainloop()