from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    question_bank.append(Question(question_data[i-1]["text"], question_data[i-1]["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz\nYour final score was {quiz.score}/{len(quiz.question_number)}")