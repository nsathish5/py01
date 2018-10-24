#Statistics on lists of numbers
import statistics
import sys
max = -sys.maxsize -1
min = sys.maxsize
sum = 0
l1 = []
while True:
    x = input("Enter number : ")
    if x == 'Q' :
        break
    l1.append (int(x))
    if int(x) > max :
        max=int(x)
    if int(x) < min :
        min=int(x)
    sum = sum + int(x)    
print("Here is the list you entered : ")
print(l1)
mean =  statistics.mean(l1) 
print("Mean is : %s" %mean)
median = statistics.median(l1)
print("Median is : %s" %median)
print ("Maximum number is %s" %max)
print ("Minimum number is %s" %min)
print ("Sum of list is %s" %sum)

    