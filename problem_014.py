"""
Longest Collatz sequence
   
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from functools import lru_cache

@lru_cache()
def longest_collatz(n):
    if n == 1:
        return None
    elif n % 2 == 0:
        return int(n/2)
    else:
        return int(3*n+1)

def chain_me_up(x):
    sequence_list = [x]
    current_number = x
    while current_number > 1:
        current_number = longest_collatz(current_number)
        sequence_list.append(current_number)
    return sequence_list

def solution(max_number):
    max_length = 0
    max_list = None 
    i = 1
    while i < max_number:
        current_list = chain_me_up(i)
        if len(current_list) > max_length:
            max_list = current_list[:]
            max_length = len(current_list)
            print("new max list, starting number",i,"length",max_length)
        else:
            pass
        i += 1
        
    print(max_list[0],"produces the longest collatz chain seqeuence under",max_number)

if __name__ == '__main__':
    print(chain_me_up(13))
    solution(1_000_000) #837799 probably be sped up significantly by better leveraging caching and removing int type conversion
    