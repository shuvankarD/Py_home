#Get Guess
import random
def get_guess():
    return list(input("What is your guess?"))


#Generate Computer Code
def generate_code():
    digits=[str(num) for num in range(10)]

    random.shuffle(digits)
    return digits[:3]


#Generate the clues
def generate_code(code,user_guess):

    if user_guess==code:
        return "Code Cracked"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")

        elif num in code:
            clues.append("close")

    if clues == []:
        return ["nope"]
    else:
        return clues


#Run Game logics
print("Welcome to code breaker")

secret_code = generate_code()

clue_report = []
while clue_report != "Code cracked"

   guess = get_guess()

   clue_report = generate_clues(guess,secret_code)
   print("Here is your result:")
   for clue in clue_report:
       print(clue)
