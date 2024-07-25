class QuizBrain:

    def __init__(self, q_list):
        self.ques_no = 0
        self.score = 0
        self.ques_list = q_list

    def still_has_ques(self):
        return self.ques_no < len(self.ques_list)

    def next_ques(self):
        curr_ques = self.ques_list[self.ques_no]
        self.ques_no += 1
        c = input(f"Q.{self.ques_no}: {curr_ques.text} (True/False): ")
        self.check_ans(c, curr_ques.answer)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.ques_no} ")
        print("\n")
