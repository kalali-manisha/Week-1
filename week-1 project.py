class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question, options):
        print(question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        user_input = input("Your answer (enter the number): ")
        return int(user_input) - 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect. The correct answer is:", correct_answer + 1)

    def run_quiz(self):
        print("Welcome to the Quiz Game!")
        for q in self.questions:
            question = q["question"]
            options = q["options"]
            correct_answer = q["correct_answer"]
            user_answer = self.display_question(question, options)
            self.check_answer(user_answer, correct_answer)
        print("Quiz ended!")
        print("Your final score is:", self.score)


if __name__ == "__main__":
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "correct_answer": 1,  # Index of correct option (Paris)
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Venus", "Jupiter", "Mercury"],
            "correct_answer": 0,  # Index of correct option (Mars)
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "O2", "NaCl"],
            "correct_answer": 0,  # Index of correct option (H2O)
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
            "correct_answer": 1,  # Index of correct option (Leonardo da Vinci)
        },
        {
            "question": "What is the tallest mammal on Earth?",
            "options": ["Elephant", "Giraffe", "Whale", "Horse"],
            "correct_answer": 1,  # Index of correct option (Giraffe)
        },
    ]

    quiz = Quiz(questions)
    quiz.run_quiz()
