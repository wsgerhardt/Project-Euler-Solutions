"""
Digit factorials
   
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial

def fact_sum(number):
    num_list = [factorial(int(a)) for a in str(number)]
    return sum(num_list)

def solution_helper(upper_bound):
    sum_me_up = 0
    #note, this could be made more efficient 
    #by doing the calculation ranges incrementally (100,200,300,400,500) 
    # cutting out when the number a min number within a band is greater than the max fact_sum in that band
    for a in range(3,upper_bound+1):  
        fact_summation = fact_sum(a) 
        #print(a)
        if fact_summation == a:
            print(a," is a solution")
            sum_me_up += fact_summation
    return sum_me_up
    
def solution_prep():
    #if done carefully, this problem is 100% about identifying what the theoretical upper-bound is.
    for digit in range(1,9):
        print("for digits length",digit)
        min = int(str(1)*digit)
        min_fact = fact_sum(min) 
        max = int(str(9)*digit)
        max_fact = fact_sum(max)
        print("min-max:",min,max,min_fact,max_fact)
        #Note, it looks like for length 8 the min value is greater than the max fact_sum. n < 8
    
def solution():
    #if done carefully, this problem is 100% about identifying what the theoretical upper-bound is.
    n = 2 #n identifies the max digit length of the number here 
    while 1*10**(n-1) < fact_sum(int(str(9)*(n-1))): #While the lowest candidate number is less than the maximum digital factor for that number of decimal places...  
        #when this loop exists it will mean the solution must be less than the 
        n += 1
    upper_bound = int(str(9)*(n-1))
    the_solution = solution_helper(upper_bound)
    print("The Solution is definintively",the_solution)
    

if __name__ == '__main__':
    #solution_helper(100_000_000) #brute force it! 40730
    solution_prep()
    solution()
        