from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    titre.config(text="Timer", fg=GREEN)
    text.config(text="")
    reps = 0
    bouton_start.config(state="normal")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
reps = 0
def start_timer():
    bouton_start.config(state="disabled")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    if reps in [1, 3, 5, 7]:
        count_down(work_sec)
        titre.config(text="Work", fg=GREEN)
    elif reps in [2, 4, 6]:
        short_break_sec = SHORT_BREAK_MIN * 60
        count_down(short_break_sec)
        titre.config(text="Pause", fg=PINK)
    elif reps == 8:
        long_break_sec = LONG_BREAK_MIN * 60
        count_down(long_break_sec)
        titre.config(text="Pause", fg=RED)
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
timer = None 
def count_down(count):
    global timer 
    minutes = count // 60
    seconds = count % 60
    time_format = f"{minutes} : {seconds}"
    if seconds < 10:
        time_format = f"{minutes} : 0{seconds}"
    canvas.itemconfig(time_text, text=time_format)

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        text.config(text=marks)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Pormodoro")
window.config(padx=100, pady=50, bg=YELLOW)

titre = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
titre.grid(column=1, row=0)

bouton_start = Button(text="Start", command=start_timer)
bouton_start.grid(column=0, row=2)



bouton_reset = Button(text="Reset", command=reset_timer)
bouton_reset.grid(column=2, row=2)

canvas = Canvas(width=200 ,height=224, bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

text= Label (text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
text.grid(column=1, row=3)


window.mainloop()