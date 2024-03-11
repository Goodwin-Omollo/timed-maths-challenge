import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 9
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    exp = str(left) + " " + operator + " " + str(right)
    answer = eval(exp)
    return exp,answer

wrong = 0
input("Press Enter to begin:")
print("--------------------------")
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    exp,answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + " : " + exp + " = ")
        if guess == str(answer):
            break
            wrong += 1


end_time = time.time()
elapsed_time = round(end_time - start_time)

print("---------------------------")
print("Nice Work! You took " + str(elapsed_time) + " seconds to complete this test!")