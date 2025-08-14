import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer

wrong = 0
print(f"Welcome to the Math Quiz! You have {TOTAL_PROBLEMS} questions.")
input("Press Enter to start!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem #{i + 1}: {expr} = ")
        try:
            if int(guess) == answer:
                break
            else:
                print("Incorrect, try again!")
                wrong += 1
        except ValueError:
            print("Please enter a valid number.")
            wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print(f"Nice work! You finished in {total_time} seconds!")
print(f"You got {wrong} wrong answer(s) in total.")
