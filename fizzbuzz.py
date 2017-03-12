# FizzBuzz Game

colorgreen = "\033[1;32m{0}\033[00m"

a = int(raw_input("Please insert number between 1 and 100: "))

while a > 100:

     print "number exceeding maximum amount (100)"
     a = int(raw_input("Please insert number between 1 and 100: "))


for c in range (a):
    d=c+1
    divisable_by_three = d % 3
    divisable_by_five = d % 5
    divisable_by_fifteen = d % 15

    if divisable_by_fifteen == 0:
        print colorgreen.format("fizzbuzz!")
    elif divisable_by_three == 0:
        print "fizz"
    elif divisable_by_five == 0:
        print "buzz"

    else:
        print d


import time
time.sleep(10)