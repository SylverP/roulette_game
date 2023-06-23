#import random module and define range 1 to 6 inclusive
import random 
key_num = random.randint (1,6)

#for testing/debugging only
##print (key_num)

guess = int(input ("Guess a number between 1 and 6 "))

#function requires str() for sorting algorithm
def algorithm_direction(key_direction):
     global guess
     print ("Too " + key_direction)
     guess = int (input ("Guess Again. "))

#sorting algorithm
while guess != key_num:
     if guess > key_num:
          algorithm_direction ("high")
     if guess < key_num:
          algorithm_direction ("low")
if guess == key_num:
     print ("Correct")



