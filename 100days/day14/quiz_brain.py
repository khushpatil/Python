class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.score = 0
        self.q_list = q_list

    def still_has_questions(self):
        return self.question_no < len(self.q_list)

    def check_answer(self,correct_ans,ans):
        if(correct_ans.lower() == ans.lower()):
            self.score += 1
            print(f"You are right!\nYour Score = {self.score}\nQuestions Done = {self.question_no}/{len(self.q_list)}")
        else:print("That is the wrong answer")

    def new_question(self):
        question = self.q_list[self.question_no]
        self.question_no += 1
        ans = input(f"Q{self.question_no}: {question.text} (True/False): ")
        self.check_answer(question.answer,ans)
