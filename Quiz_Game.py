# Introduction to the quiz game
print("Welcome to the quiz game!")
print("Answer the following questions with the correct answers.")
print("Instructions:"
      "1: Solve the questions with most suitable answer "
      "2: Each Questions is equivalent to 2 points "
      "3: If question is answered incorrectly you are Given 1 attempt answer the question correctly,correct answer(1p)"
      "4: You are not! by any circumstances allowed to copy or cheat")


# Questions and Answers
questions = [
    "What is the capital of France?",
    "What is the highest mountain in the world?",
    "What is the largest country by land area?",
    "What is the smallest country in the world?",
    "What is the currency of Japan?",
    "What is the largest ocean in the world?",
    "What is the smallest continent in the world?",
    "What is the largest desert in the world?",
    "What is the largest animal in the world?",
    "What is the smallest animal in the world?",
    "What is the national language of Spain?",
    "What is the national language of Brazil?",
    "What is the largest city in the world by population?",
    "What is the longest river in the world?",
    "What is the name of the famous clock tower in London?",
    "What is the name of the longest wall in the world?",
    "What is the name of the famous Egyptian monument?",
    "What is the name of the famous ancient Greek temple?",
    "What is the name of the famous ancient Roman arena?",
    "What is the name of the famous ancient Mayan pyramid?"
]

answers = [
    "Paris",
    "Mount Everest",
    "Russia",
    "Vatican City",
    "Yen",
    "Pacific Ocean",
    "Australia",
    "Sahara",
    "Blue Whale",
    "Bee Hummingbird",
    "Spanish",
    "Portuguese",
    "Tokyo",
    "Nile",
    "Big Ben",
    "Great Wall of China",
    "Pyramids of Giza",
    "Parthenon",
    "Colosseum",
    "Chicken Ita"
]

# Initialize score
score = 0

# Get halfway point
half_point = len(questions) // 2

# Loop through questions
for i in range(len(questions)):
    # Ask question
    print("Question", i+1, ":", questions[i])
    # Get user input
    answer = input("Your answer: ")
    # Check if answer is correct
    if answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        print("The correct answer is:", answers[i])

    # Give half score feedback
    if i+1 == half_point:
        half_score = score
        print("Halfway there! Your current score is:", half_score, "/", i+1)

# Display final score and grading
print("Congratulations on finishing the quiz!")
print("Your final score is:", score, "/", len(questions))
if score == len(questions):
    print("Excellent! You got a perfect score!")
elif score >= len(questions)/2:
    print("Good job! You got more than half of the questions correct.")
else:
    print("Better luck next time. Keep studying and learning!")
