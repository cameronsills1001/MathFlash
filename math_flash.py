
import random

total_questions = 0
number_correct = 0

def num_gen():
    """Return a random number between 0 and 12"""
    return random.randint(0,12)

def question_generator(num1, num2):
    """Generate a question for the student to answer and checks answer"""
    global number_correct
    answer = num1 * num2
    print("%d X %d =" % (num1, num2))
    user_answer = input("Your answer: ")
    if answer==int(user_answer):
        print("Correct\n")
        number_correct += 1
        return True
    else:
        print("Incorrect\n")
        return False


def welcome():
    """Starts and begins set up for the session"""
    global total_questions
    print("Welcome to Math Flash")
    print("\nLet's set up your flash cards")
    total_questions = set_up()
    rand_or_not = first_number()
    if rand_or_not:
        double_random(total_questions)
    else:
        single_random(total_questions, fixed())


def double_random(how_many):
    """Will give the student 2 random numbers when they do not wish to 
    work on a specific times table"""
    for i in range(how_many):
        num1 = num_gen()
        num2 = num_gen()
        question_generator(num1, num2)

def single_random(how_many, num):
    """Uses a student defined number and a random number"""
    for i in range(how_many):
        num1 = num
        num2 = num_gen()
        question_generator(num1, num2)

    
    
def set_up():
    """Set up for how many questions the student would like to attempt"""
    print("How many questions would you like?")
    return int(input(": "))
    
def first_number():
    """interface for choosing if both number should be random 
    or a student defined times table"""                  
    print("\nDo you have a certain times table you would like to work on? Y or N")
    answer = input(":")
    if answer.lower() == 'y':
        return False
    else:
        return True

def fixed():
    """When student chooses a single times table it allows them to select which one"""
    print("What times table would you like to work on?")
    num = int(input("Please enter a number 0-12: "))
    return num
    
def tabulate_score():
    """Prints the score of the session"""
    print(f"You got {number_correct}/{total_questions} with a score of {int(number_correct/total_questions*100)}%")



welcome()
tabulate_score()


    
