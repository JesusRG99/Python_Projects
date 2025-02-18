from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# This is the list which will contain the list of question objects
question_bank = [] 

# We loop trough each entry of the list on data.py, each entry is a dict.
# for each dictionary we create a new object from the Question class with the
# key "text" and "answer" from the dictionary and we append that object into the
# question_bank list

for entry in question_data: 
    new_question = Question(entry["question"], entry["correct_answer"])
    question_bank.append(new_question)


quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the Quiz")
print(f"Your final score was: {quiz_brain.score}/{len(question_bank)}")