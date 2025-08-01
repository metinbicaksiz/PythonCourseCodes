from tkinter import *

window = Tk()
window.title("Converter")
window.geometry("300x300")
window.configure(padx=10, pady=10)


miles_input = Entry(width=10)
miles_input.grid(column=2, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=2, row=1)

km_text = Label(text="KM")
km_text.grid(column=3, row=1)


def convert():
    miles = float(miles_input.get())
    kilometers = miles * 1.60934
    km_result.configure(text=kilometers)

button = Button(text="Convert", command=convert)
button.grid(column=2, row=2)

window.mainloop()