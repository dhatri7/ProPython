from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain

ques_bank = []
for ques in question_data:
    ques_text = ques["question"]
    ques_ans = ques["correct_answer"]
    new_ques = Question(ques_text, ques_ans)
    ques_bank.append(new_ques)

quiz = QuizBrain(ques_bank)

while quiz.still_has_ques():
    quiz.next_ques()

print("You've have completed the quiz.")    
print(f"Your final score was: {quiz.score}/{len(ques_bank)}") 
