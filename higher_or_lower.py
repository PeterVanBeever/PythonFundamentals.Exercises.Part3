from random import randrange
print(randrange(10))
#7
print(randrange(10))
#1
print(randrange(10))
#5
print(randrange(10))
#6
print(randrange(10))
#5"""

def user_number_between_zero_ten():
    input1 = input("Enter a number btween 1 and 10:  ")
    return int(input1)

def random_number_between_one_and_ten():
    return(randrange(1,10))

def evaluate_random_number_against_user_number():
    case1 = user_number_between_zero_ten()
    case2 = random_number_between_one_and_ten()

   
    if case1 < case2:
        print("You guessed too low")
        print("The number was " + str(case2))
    elif case1 > case2:
        print("You guessed to high")
        print("The number was " + str(case2))
    elif int(case1) == int(case2):
        print("You guessed correct")
    else:
        print("Yikes")

evaluate_random_number_against_user_number()

