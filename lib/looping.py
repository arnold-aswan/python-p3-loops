#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    stop = 0
    start = 10
    while (start != stop):
        print(start)
        start -= 1
    else:
        print("Happy New Year!")
        
def square_integers(int_list):
    # code goes here!
    int_list = [int * int for int in int_list]
    return int_list

def fizzbuzz():
    # code goes here!
    stop = 100
    start = 0
    while (start != stop):
        start += 1
        if start % 3 == 0 and start % 5 == 0:
            print("FizzBuzz")
        elif start % 3 == 0:
            print("Fizz")
        elif start % 5 == 0:
            print("Buzz")
        else:    
           print(start)
    
