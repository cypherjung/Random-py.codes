#quiz
import random
import time

class MentalMathQuiz:
    def __init__(self):
        self.score = 0

    def generate_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"What is {num1} {operator} {num2}?"
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        return question, answer

    def get_user_answer(self):
        while True:
            user_input = input("Enter your answer: ")
            if user_input.lstrip('-').isdigit():
                return int(user_input)
            print("Invalid input. Please enter an integer.")

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")

    def run_quiz(self, duration):
        start_time = time.time()
        end_time = start_time + duration
        question_count = 0

        while time.time() < end_time:
            question_count += 1
            question, answer = self.generate_question()
            print(f"Question {question_count}:")
            print(question)
            user_answer = self.get_user_answer()
            self.check_answer(user_answer, answer)
            print()

        print("Quiz completed!")
        print("Your score is {}/{}".format(self.score, question_count))


# Create an instance of the MentalMathQuiz class
quiz = MentalMathQuiz()

# Set the duration of the quiz in seconds
duration = 60

# Run the quiz
quiz.run_quiz(duration)



     
