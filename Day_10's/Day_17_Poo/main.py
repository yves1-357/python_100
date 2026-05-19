from data import question_data 
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for items in question_data:
    question_texte = items['text']
    question_answer = items['answer']
    nouvelle_objet = Question(question_texte, question_answer)
    question_bank.append(nouvelle_objet)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

