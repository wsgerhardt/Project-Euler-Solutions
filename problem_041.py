"""
Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations
from multiprocessing import Pool

#copied from problem 35
def is_prime(number):
    if number <= 1 or number % 2 == 0:
        return False
    else:
        i=3
        no_break = True
        while i < int(number/2)+1 and no_break:
            if number % i == 0:
                no_break = False
            i += 2
        return no_break
    
def pandigital(n):
    digits_to_check = [str(x) for x in range(1,n+1)]
    pandigital_list = []
    for x in permutations(digits_to_check):
        number = int("".join(x))
        if x[-1] in ('1','3','5') and is_prime(number):
            print("It's Prime!",number)
            pandigital_list.append(number)
    if len(pandigital_list) != 0:
        print("max digit for n =",n,"is",max(pandigital_list))
    else:
        print("no primes for digits n =",n)
    return pandigital_list

def pandigital_more_efficient(n):
    digits_to_check = [x for x in range(1,n+1)]
    pandigital_list = []
    for x in permutations(digits_to_check):
        #print(x)
        number = sum([a*10**(n-i-1) for i,a in enumerate(x)])
        #print(number)
        if x[-1] in (1,3,5) and is_prime(number):
            print("It's Prime!",number)
            pandigital_list.append(number)
    if len(pandigital_list) != 0:
        print("max digit for n =",n,"is",max(pandigital_list))
    else:
        print("no primes for digits n =",n)
    return pandigital_list


def perm_check(x):
    n = len(x)
    number = sum([a*10**(n-i-1) for i,a in enumerate(x)])
    #print(number)
    if x[-1] in (1,3,5) and is_prime(number):
        print("It's Prime!",number)
        return number

def pandigital_multiprocessing_cheat(n):
    digits_to_check = [x for x in range(1,n+1)]
    perms = permutations(digits_to_check)
    pandigital_list = []
    with Pool(5) as p:
        for x in p.map(perm_check, perms):
            if x is not None:
                pandigital_list.append(x)
    
    if len(pandigital_list) != 0:        
        print("max digit for n =",n,"is",max(pandigital_list))
    else:
        print("no primes for digits n =",n)
    return pandigital_list

def soltion(max_n):
    for digit in range(1,max_n+1):
        print("processing",digit)
        #pandigital(digit)
        #pandigital_more_efficient(digit)
        pandigital_multiprocessing_cheat(digit) #Meet the 1 minute rule! : )

if __name__ == '__main__':
    #print(pandigital(4))
    soltion(9) #7652413; though I don't like the inefficient solution

"""
After I solved this I checked the forms and everyone there was just brute forcing it. 
No one uses proper function names either. :(

"""
    
