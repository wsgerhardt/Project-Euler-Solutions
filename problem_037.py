"""
Truncatable primes
   
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove 
digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

from itertools import permutations, combinations_with_replacement
from functools import lru_cache

#copies from problem 35
@lru_cache()
def is_prime(number):
    if number <= 1:
        return False
    else:
        i=2
        no_break = True
        while i < number and no_break:
            if number % i == 0:
                no_break = False
            i += 1
        return no_break

@lru_cache()
def trunc_list(number,digits):
    holding = [number]
    str_rep = str(number)
    print(number,digits)
    for x in range(1,digits):
        forward = int(str_rep[x:])
        reverse = int(str_rep[:digits-x])
        holding.append(forward)
        if number > 9:
            holding.append(reverse)
    
    holding = list(set(holding))
    holding.sort(reverse=False)
    #print("returning trunc list",holding)
    return holding

@lru_cache()
def premutaiton_processing(number,tens_place):
    assumed_to_be_prime = True
    temp_prime_list = []
    a_trunc_list = trunc_list(number,tens_place) 
    if a_trunc_list is not None: 
        for x in trunc_list(number,tens_place):
            #print("testing",x)
            key_condition = is_prime(x)
            if key_condition:
                temp_prime_list.append(number)
                #print(number,"added to valid trun list")
            else:
                #print(x,"is not prime")
                assumed_to_be_prime = False
                break
    
        if assumed_to_be_prime:
            return temp_prime_list
   

def draft_solution(max_digits):
    #test solution based on problme 35
    viable_digits = (1,2,3,5,7,9) #I admit I experimented with trial and error to get this list. :) 
    all_truncable_primes = []
    for tens_place in range(2,max_digits+1):
        if tens_place < 2:
            raise ValueError("Digits must be greater than 2.")
  
        combination_list = list(combinations_with_replacement(viable_digits,tens_place))
        for x in combination_list:
            print("Testing set for",x)
            for test in permutations(x):
                number = sum([x*10**(tens_place-1-a) for a,x in enumerate(test)])
                add_list = premutaiton_processing(number,tens_place)
                if add_list is not None:
                    print("prime group added for",number,":",add_list)
                    all_truncable_primes += add_list
    
    possible_solution = list(set(all_truncable_primes))
    if len(possible_solution) == 11:
        print("The solution appears to be",sum(possible_solution))            
    return list(set(all_truncable_primes))
    

def better_combination_list(max_digits=2):
    available_digits = max_digits -2
    pass

"""
the prime cannot start or end in 1 or 9 here, so the order is...
[3,7][1,3,7,9][3,7]
"""

if __name__ == '__main__':
    trunc_list(3797,4)
    print(draft_solution(3))  
    print(draft_solution(6)) #try and brute force it! But why...
    