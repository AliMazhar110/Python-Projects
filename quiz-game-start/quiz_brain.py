class QuizBrain:
    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)? = ")
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def check_answer(self, u_answer, actual_answer):
        if u_answer == actual_answer:
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {actual_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def final_score(self):
        print("\nYou have completed the quiz.")
        print(f"Your final score: {self.score}/{self.question_number}")
