BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

timer = None
# ---------------------------- Components ------------------------------- #
try :
    df = pandas.read_csv("data/words_to_learn.csv")
    learn=df.to_dict(orient="records")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    learn = df.to_dict(orient="records")

def next_card():
    global timer
    global current_card
    if timer:
        window.after_cancel(timer)
        
    current_card = random.choice(learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"], fill = "black")
    timer = window.after(3000, func=flip_card)
    canvas.itemconfig(card_bg_canvas, image=logo_img)
    

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg_canvas, image=card_background)

def is_known():
    global current_card
    learn.remove(current_card)
    pandas.DataFrame(learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("Capstone project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR )
canvas = Canvas(height=526, width=800)

logo_img = PhotoImage(file="images/card_front.png")
card_bg_canvas = canvas.create_image(400, 263, image=logo_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "bold"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_background = PhotoImage(file="images/card_back.png")


wrong_image= PhotoImage(file="images/wrong.png")
Buttons1 = Button(image=wrong_image, highlightthickness=0, command=next_card)
Buttons1.grid(row=1, column=0)

right_image= PhotoImage(file="images/right.png")
Buttons2 = Button(image=right_image, highlightthickness=0, command=is_known)
Buttons2.grid(row=1, column=1)


next_card()
window.mainloop()