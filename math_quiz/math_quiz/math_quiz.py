import random


def generate_random_integer(min, max):
    """
    Generates and returns a random integer between min and max.
    min = The minimum integer value for random number range
    max = The maximum integer value for random number range
    """
    return random.randint(min, max)


def generate_random_operator():
    """
    Selects and returns a random math operator from +, -, and *.
    """
    return random.choice(['+', '-', '*'])


def construct_math_problem(n1, n2, operator):
    """
    Constructs a math problem based on two numbers n1 and n2 and an operator.
    Returns a tuple with problem as a string and the correct answer
    """ 
    #Construct the problem in the form of "n1 operator n2"
    #Calculate answer based on operator
    problem = f"{n1} {operator} {n2}"
    if operator == '+': 
        answer = n1 + n2
    elif operator == '-': 
        answer = n1 - n2
    else: 
        answer = n1 * n2
    return problem, answer

def math_quiz():
    """
    The player is presented with 10 randomly geberated math questions. 
    He earns one point for each correct answer. 
    The score is displayed when all questions are answered.
    """
    #Initial score is 0
    #Total number of questions is changed to 10 because quiz length has to be an integer value
    score = 0
    number_of_questions = 10 

    #Introduction message to the player
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #
    for _ in range(number_of_questions):
        #Generates two random numbers and an operator from the given range
        n1 = generate_random_integer(1, 10); 
        n2 = generate_random_integer(1, 10); 
        operator = generate_random_operator()

        #Create problem string and calculate the answer
        problem, correct_answer = construct_math_problem(n1, n2, operator)
        
        #Display problem to the player
        print(f"\nQuestion: {problem}")

        #Error handling for the case when user input is not a valid integer
        #Error message and skip to the next question without counting this input as an attempt
        try:
            user_answer = int(input("Your answer:"))
        except ValueError:
            print("Invalid input. Please enter a valid integer value as your answer")
            continue
    
        #Check if the answer given by user is correct
        #If yes, increase score by 1 and if no, display "Wrong answer" along with the correct answer
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    #Display the final score when all questions have been answered
    print(f"\nGame over! Your score is: {score}/{number_of_questions}")

#Run the quiz
if __name__ == "__main__":
    math_quiz()
