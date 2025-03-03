'''
Task_02 :
Take an integer number as user input. If that number is divisible by 3, 5, or 7, print "Divisible by 3, 5, 7", else print "Not useful".
'''
number= int(input("Enter the number to check the divisibility by 3, 5, or 7 :"))
if number % 3 == 0 or number % 5 == 0 or number % 7 == 0 :
        print("Divisible by 3, 5, 7")
else:
        print("Not useful")
