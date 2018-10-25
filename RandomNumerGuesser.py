#Random number guesser
import random
rn = random.randrange(100)
ch = 0
while True :
    x = input ("Guess the number : ")
    if x == 'Q' :
        break
    if int(x) == rn :
        print ("Congratulations! You guessed right.")
        break
    if int(x) > rn + 25 :
        print ("Too High, Guess again")
    if int(x) < rn - 25 :
        print ("Too Low, Guess again")
    if int(x) != rn :
        print ("Try Again")
    if int(x) == (rn + 2) or int(x) == (rn - 2) :
        print ("You are very close, try again") 
    ch = ch + 1
print ("You took %s chances to guess" %ch)

# import random

# secret_number = random.choice(range(101)) # this is slightly more random on many OSs

# guess_counter = 0

# while True:
#     guess = input("Enter a number or type \'q\' to quit\t")
#     print(guess)
#     if guess == 'q':
#         break
#     else:
#         try:
#             my_guess = int(guess)
#             guess_counter += 1
#         except:
#             print("That's not an Integer! (Whole Number)")
#             continue
    
#     if my_guess == secret_number:
#         print("You Win!")
#         print("It took {0} guesses".format(guess_counter))
#         break
#     elif my_guess < secret_number:
#         print("Too low... Try a larger number")
#     elif my_guess > secret_number:
#         print("Too high... Try a smaller number")
