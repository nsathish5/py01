#Statistics on lists of numbers
import statistics
import sys

# sum, and max are built-in functions
# and you should avoid using variable
# names that clash with the names
# of functions

# max = -sys.maxsize -1
# min = sys.maxsize
# sum = 0
# l1 = []

number_list = []

while True:
    x = input("Enter number or \'Q\' if you're done adding numbers : ")
    if x.upper() == 'Q' :
        break
    try:
        number_list.append(int(x))
    except ValueError:
        print("You didn't give me a number or Q")
        continue # this forces the next loop early
    # l1.append (int(x))
    # if int(x) > max :
    #     max=int(x)
    # if int(x) < min :
    #     min=int(x)
    # sum = sum + int(x)    
print(f"Here is the list you entered : {number_list}")
#print(l1)
#mean =  statistics.mean(l1) 
print(f"Mean is : {statistics.mean(number_list)}")
#median = statistics.median(l1)
print(f"Median is : {statistics.median(number_list)}")
print (f"Maximum number is {max(number_list)}")
print (f"Minimum number is {min(number_list)}")
print (f"Sum of list is {sum(number_list)}")

# See how the program became shorter and a little 
# neater? I used "f" strings and the built-in 
# functions