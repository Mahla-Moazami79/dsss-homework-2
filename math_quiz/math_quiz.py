import random


def generate_number(minimum: int, maximum: int):
    """
    Generate a random integer between minimum and maximum values.

    Arguments:
        minimum (int): The lowest amount of the range
        maximum (int): The highest amount of the range

    Returns:
        int: A random integer in a fixed range
    """
    return random.randint(minimum, maximum)


def get_random_operator():
    """
    Select a random mathematical operator like +, -, *.

    Returns:
        str: A random operator
    """
    return random.choice(['+', '-', '*'])


def generate_problem(num1: int, num2: int, operator: str) -> tuple[str, int]:
    """
    Generate a math problem and calculate its answer.

    Arguments:
        num1 (int): First number in the problem
        num2 (int): Second number in the problem
        operator (str): Mathematical operator (+, -, or *)

    Returns:
         the problem string and its answer
    """
    problem = f"{num1} {operator} {num2}"

    # Calculate the actual answer
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # operator is '*'
        answer = num1 * num2

    return problem, answer


def math_quiz() -> None:
    """
    Run math quiz game where users solve random math problems.
    The game has 3 questions and shows the user's score.
    """
    score = 0
    total_questions = 3  # Fixed number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for question_num in range(total_questions):
        # Generate random numbers and operator
        num1 = generate_number(1, 10)
        num2 = generate_number(1, 5)
        operator = get_random_operator()

        # Generate the problem and get correct answer
        problem, correct_answer = generate_problem(num1, num2, operator)

        # Present question and get user's answer
        print(f"\nQuestion {question_num + 1}: {problem}")

        # Handle user input with error checking
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Please enter a valid integer!")

        # Check answer and update score
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Display final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
