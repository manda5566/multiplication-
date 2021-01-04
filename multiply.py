#  practice solving multiplication problems 

import random
from cs50 import get_int

# how many questions?
q = get_int("how many question do you want ? ")

score = 0

# ask q questions (0,1,...,q - 1)
for i in range(q):

    # get 2 random numbers
    x = random.randrange(1,12)
    y = random.randrange(1,12)
    
    # ask the user 
    ask = get_int(f"\nwhat's {x} * {y} = ")
    # the actual result
    result = x * y
    
    # if the actual answer = the answer that the user typed:    
    if ask == result:
        score += 100 # add 100 to the score
        print("True!")
    
    # if the actual answer != the answer that the user typed:
    else:
            print(f"false :(\nthe answer: {result}")

# at the end, print the score
print(f"\nyour score:\n{score}")
