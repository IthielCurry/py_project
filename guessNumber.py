import random

print("Guess the number: fun game")

generate_number = random.uniform(1, 100)

question = float(input("quess a number from 1 to 100:  "))

if question == generate_number:
    print("Congratulations: you guessed right: ")

elif question >= generate_number:
    print("Too high try again. ")

elif question <= generate_number:
    print("Too low try again ")

else:
    ("Search this error code: err934y7823b")



