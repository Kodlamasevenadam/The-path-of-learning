questions = (("How many elements are in the periodic table"),
             ("Which animal lays the largest egg"),
             ("what is the mos abbundant gas in the earths atmosphere"),
             ("How many bones are there in the human body "),
             ("Which planet in the solar system is the hottest "))


options = (("A.116", "B.117", "C.118", "D.119"),
           ("A.Chicken", "B.Whale", "C.Dog", "D.Ostrich"),
           ("A.nitrogen", "B.C02", "C.02", "D.Methane"),
           ("A.206", "B.207", "C.208", "D.209"),
           ("A.Mercury", "B.Venus", "C.Earth", "D.Mars"),)

answers = ("c", "D", "A", "A", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------")
    print(question)
    for option in options[question_num]:
        print(option)


guess = input("Enter your answer(A,B,C,D)").upper()
guesses.append(guess)

if guess == answers[question_num]:
    score += 1
    print("Correct!")
else:
    print("incorrect!")
    print(f"{answers[question_num]} is the correct answer of the question!")
question_num += 1
