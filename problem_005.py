"""
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def alL_the_mods(upper_bound_int):
    #note this method is very computationally intensive and probably isn't the best approach.
    
    factorial_range = range(2,upper_bound_int+1) #one doesn't count
    solution_not_found = True
    growing_number = upper_bound_int
    while solution_not_found:
        for x in factorial_range:
            if growing_number % x != 0:
                growing_number += upper_bound_int
                break
            #if you get to this point you won
            if x == upper_bound_int:
                solution_not_found = False
    
    print("The first number divisible by numbers 1 through ",upper_bound_int,"is:",growing_number)

if __name__ == '__main__':
    alL_the_mods(10)
    alL_the_mods(20) #232792560 was very computationally intensive... until I realized incrementing by the upper-bound is the way to go. :)
    #alL_the_mods(30) #My computer ran like it was mining bitpoints on this one. Could be a fun problems to experiment with multi-threading.