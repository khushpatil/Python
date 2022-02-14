from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

def main():

    question_bank = []
    for q in question_data:
        question = Question(q["text"], q["answer"])
        question_bank.append(question)

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.new_question()
        print("\n")
    if input(f"Your score is {quiz.score}/12!\nType y to try again or n to quit: ") == "y":
        os.system("cls")
        main()
    else:os.system("cls")
main()