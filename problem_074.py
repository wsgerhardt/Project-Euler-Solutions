"""Digit factorial chains

Problem 74"""

from math import factorial
from functools import lru_cache
import timeit


@lru_cache()
def fast_digit_factor(digit):
    return sum([factorial(int(x)) for x in str(digit)])

def slow_digit_factor(digit):
    return sum([factorial(int(x)) for x in str(digit)])

def digit_factor_chain(maximum,digit_factor_function):
    #could use a library of prior terms to be more efficient... this way still works with a reasonable run time.
    length_sixty_count = 0 
    for a in range(1,maximum):
        previous_terms_in_sequence = [a]
        exit_condition_does_not_exist = True
        current_value = a
        while exit_condition_does_not_exist:
            test_value = digit_factor_function(current_value)
            if test_value not in previous_terms_in_sequence:
                previous_terms_in_sequence.append(test_value)
                current_value = test_value
            else:
                exit_condition_does_not_exist = False 
        
        if len(previous_terms_in_sequence) == 60:
            length_sixty_count += 1
        
        #print(a,previous_terms_in_sequence)
    
    print("There are",length_sixty_count,"chains below",maximum,"with a sixty non-repeating_chains")
    
if __name__ == '__main__':
    digit_factor_chain(1*10**6,fast_digit_factor)

    """
    a = timeit.Timer("digit_factor_chain(1*10**6,fast_digit_factor)", setup="from __main__ import digit_factor_chain,fast_digit_factor")
    a.timeit()
    b = timeit.Timer("digit_factor_chain(1*10**6,slow_digit_factor)", setup="from __main__ import digit_factor_chain,slow_digit_factor")
    b.timeit()
    """