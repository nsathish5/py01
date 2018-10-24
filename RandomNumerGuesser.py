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