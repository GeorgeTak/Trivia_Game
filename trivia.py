

questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ",
                       "How many pounds are in a ton?:",
                       "In which city did the Olympic games originate:?",
                       "How many time zones are there in Russia:?",
                       "What’s the capital of Canada:?",
                       "What year did the Berlin wall fall:?"
             )

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
                   ("A. 1000 pounds", "B. 2000 pounds", "C. 3000 pounds", "D. 4000 pounds" ),
                   ("A. Rome", "B. Madrid", "C. Athens", "D. Cairo"),
                   ("A. 8", "B. 9", "C. 10", "D. 11"),
                   ("A. Ottawa", "B. Toronto", "C. Montreal", "D. Vancouver"),
                   ("A. 1988", "B. 1989", "C. 1990", "D. 1991"))

answers = ("C", "D", "A", "A", "B", "B", "C", "D", "A", "B")
guesses = []
score = 0
question_num = 0
correct_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    if guess == "":
        print("It's not a valid option!\n")
        guess = input("Enter (A, B, C, D): ").upper()

    guesses.append(guess)
    if guess == answers[question_num]:
        score += 50
        print("CORRECT!")
        correct_num += 1
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
        score -= 25
    question_num += 1


print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score * 100)
print(f"Your score is: {score}")
print(f"You guessed {correct_num} out of {question_num} correct questions!!")