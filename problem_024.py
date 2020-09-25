"""

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations

def lexographica_permutations(max_digits):
    decode_list = []
    for num_set in permutations(range(0,max_digits)):
        string_rep = "".join([str(x) for x in num_set])
        decode_list.append(string_rep)
    
    decode_list.sort()
    return decode_list

def solution():
    print("The solution is",lexographica_permutations(10)[999_999])

if __name__ == '__main__':
    lexographica_permutations(3)
    solution() #2783915460 tada