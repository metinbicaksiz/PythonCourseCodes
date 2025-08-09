from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import  Quiz

NUMBER_OF_QUESTIONS = 10
QUESTION_TYPE = "boolean"

parameters = {
    "amount" : NUMBER_OF_QUESTIONS,
    "type" : QUESTION_TYPE,
    "category" : 18
}

data = requests.get("https://opentdb.com/api.php", params=parameters)
data.raise_for_status()
question_data = data.json()["results"]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = Quiz(quiz)
#
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
