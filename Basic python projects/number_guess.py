import random
lowest_number = 1
highest_number = 100

answer = random.randint(lowest_number,  highest_number)

print(answer)
gueses = 0
is_running = True


print("Welcome To The number guessing game ")
print(f"Sellect a number between {lowest_number} and {highest_number}")
while is_running:

    gues = input("Enter Your Guess:")

    if gues.isdigit():
        gues = int(gues)
        gueses += 1

        if gues < lowest_number or gues > highest_number:
            print("Your number is out of bounds ")
            print(
                f"Please sellect a number between {lowest_number} and {highest_number}")

        elif gues < answer:
            print("Too low try again")
        elif gues > answer:
            print("Too high try again")
        else:
            print(f"Your answer is correct.The answer was! {answer}")
            print(f"Number of gueses is : {gueses}")
            is_running = False

    else:
        print("Invalid guess")

        print(
            f"Please sellect a number between {lowest_number} and {highest_number}")
