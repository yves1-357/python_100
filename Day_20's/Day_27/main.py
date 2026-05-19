from tkinter import *

window = Tk()
window.title("First tkinter program")
window.minsize(width=500, height=300)
window.config(padx=10, pady= 20)


def button_clicked():
    print("i got checked")
    new_text = input.get()
    my_label.config(text="New Text")


#Label
my_label = Label(text="Miles", font=("Arial", 24, "bold"))
my_label.config(text="Miles")
my_label.grid(column=2, row=0) #pour que le label soit visible 


#buttom
button = Button(text ="click me ", command ="")
button.grid(column=1, row=1)



#Entry
input = Entry(width = 10)
print(input.get())
input.grid(column=1, row=0)




window.mainloop()


