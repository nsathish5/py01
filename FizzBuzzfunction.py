# Fizz-Buzz using function

def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

try :
    x = int(input("Enter an integer : "))
    if x == int(x):
        print (fizzbuzz(x))
except :
        print ("Invalid Input, enter an integer")    





