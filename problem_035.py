"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from itertools import permutations, combinations_with_replacement
from functools import lru_cache 

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

def numeric_rotations(number,num_length):
    a = str(number)
    rotation_list = []
    #rotate among the offset
    for i in range(0,num_length):
        number = int("".join([a[x-i] for x in range(0,num_length)]))
        rotation_list.append(number)
    return rotation_list

def simple_better_solution(max_digits=2):
    
    viable_digits = (1,3,5,7,9)
    circulating_prime_list = [2]
    
    for tens_place in range(1,max_digits+1):
        assumed_to_be_prime = True
        if tens_place < 2:
            viable_digits = (1,3,5,7,9)
        else:
            viable_digits = (1,3,7,9) #there are no primes that end in 5
        
        combination_list = list(combinations_with_replacement(viable_digits,tens_place))
        
        for x in combination_list:
            
            print("Testing set for",x)
            for test in permutations(x):
                number = sum([x*10**(tens_place-1-a) for a,x in enumerate(test)])
                key_condition = is_prime(number) and number not in circulating_prime_list
                if key_condition:
                    temp_prime_list = []
                    assumed_to_be_prime = True
                    for x in numeric_rotations(number,tens_place):
                        #print("testing rotation",x)
                        if is_prime(x):
                            temp_prime_list.append(x)
                        else:
                            assumed_to_be_prime = False
                            #print("failed on",x)
                            break
                else:
                    pass
                    #print(number,"not tested because not prime or duplicate")
                
                if key_condition and assumed_to_be_prime is True:
                    print("prime group added for",number,":",temp_prime_list)
                    circulating_prime_list += list(set(temp_prime_list))
    
    print("The solution is...",len(circulating_prime_list))
    return circulating_prime_list

if __name__ == '__main__':
    print(simple_better_solution(2))
    simple_better_solution(3)
    simple_better_solution(4)
    a = simple_better_solution(6) #55; though it runs a bit slow.
