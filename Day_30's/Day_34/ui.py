from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
Score = 0
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizlet")
        self.window.config(padx=20, pady=20, background= THEME_COLOR) 

        self.mon_label = Label(self.window,text="Score: 0", font=("Arial", 12), bg= THEME_COLOR, fg="white" ) 
        self.mon_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=800,height=650, bg="white"  )
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.question_text = self.canvas.create_text(400, 325, text="Le texte de la question ira ici", 
                                fill=THEME_COLOR,font=("Arial", 20, "italic"), width=400 )
        
        self.true_img= PhotoImage(file="images/true.png")
        self.true_button = Button(self.window, image=self.true_img,highlightthickness=0, bd=0, command=self.get_true_pressed )
        self.true_button.grid(row=2, column=0)

        self.false_img= PhotoImage(file="images/false.png")
        self.false_button = Button(self.window, image=self.false_img,highlightthickness=0, bd=0, command=self.get_false_pressed )
        self.false_button.grid(row=2, column=1)


        self.get_next_question()



        self.window.mainloop()
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
             q_text = self.quiz.next_question()
             self.canvas.itemconfig(self.question_text, text = q_text)
             self.mon_label.config(text=f"Score: {self.quiz.score}")
             self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.question_text, text="Vous avez terminé le Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.config(bg="white")

      


    def get_true_pressed(self):
        est_correct = self.quiz.check_answer("True")
        self.feedback(est_correct)
    
    def get_false_pressed(self):
        est_correct = self.quiz.check_answer("False")
        self.feedback(est_correct)

    def feedback(self, est_correct):
        if est_correct:
          self.canvas.config(bg="green")
          self.window.after(1000, self.get_next_question)
        else:
           self.canvas.config(bg="red")  
           self.window.after(1000, self.get_next_question) 
    



        

