from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=10, pady= 20)


def button_clicked():
    print("i got checked")
    new_text = input.get()
    number = float(new_text) * 1.609
    number = round(number, 2)
    result_label.config(text=str(number))

#Entry
input = Entry(width = 5)
print(input.get())
input.grid(column=1, row=0)

#Label
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0) 

is_equal_label = Label(text="Is equal to")
is_equal_label.config(text="Is equal to")
is_equal_label.grid(column=0, row=1)


result_label = Label(text="0") 
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.config(text="Km")
km_label.grid(column=2, row=1)

#buttom
button = Button(text ="calculate", command =button_clicked)
button.grid(column=1, row=2)

window.mainloop()


