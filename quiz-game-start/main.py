from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    keys = list(question.keys())
    ques = Question(question[keys[3]], question[keys[4]])
    question_bank.append(ques)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_score()
