import random
import time

OPERATIONS = ['+', '-', '*', '//']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    operand1 = random.randint(MIN_OPERAND, MAX_OPERAND)
    operand2 = random.randint(MIN_OPERAND, MAX_OPERAND)
    operation = random.choice(OPERATIONS)

    if operation == '//':
        # Ensure division results in an integer
        operand1 = operand1 * operand2

    expr = str(operand1) + ' ' + operation + ' ' + str(operand2)
    answer = eval(expr)
    return expr, answer

wrong = 0
print("Welcome to the Timed Math Challenge!\n")
print(f"You will be given {TOTAL_PROBLEMS} problems to solve. Try to get as many correct as possible!")
input("Let's begin! Press Enter to start...")
print("-" * 40)
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    problem, correct_answer = generate_problem()
    while True:
        user_input = input(f"\nProblem {i+1}: {problem} = ")
        try:
            user_answer = int(user_input)
            if user_answer == correct_answer:
                print("Correct!")
                break
            else:
                wrong += 1
                print(f"Wrong!")
        except ValueError:
            print(f"Invalid input. Please enter an integer.")

end_time = time.time()
elapsed_time = end_time - start_time
print("-" * 40)
print(f"Challenge completed! You got {TOTAL_PROBLEMS - wrong} out of {TOTAL_PROBLEMS} correct.")
print(f"Time taken: {elapsed_time:.2f} seconds.")