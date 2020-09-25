"""Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

"""

from itertools import permutations
from itertools import combinations

def is_pandigital(n):
    no_exit = True
    n_str = str(n)
    sequential_num_string = "".join([str(a) for a in range(1,len(n_str)+1)])
    i = 0
    the_verdict = None
    while i < len(n_str) and no_exit:
        #print(n_str[i],sequential_num_string)
        if n_str[i] not in sequential_num_string:
            no_exit = False
            the_verdict = False
        i += 1

    if the_verdict is None:
        return True
    else:
        return False

def stringer(num_string_list):
    return int("".join(num_string_list))

def fun_products(max_n):
    #Note, this can be sped up significantly if eliminate scenairos where certain y and z positions will create viable products
    sequential_num_list = [str(a) for a in range(1,max_n+1)]
    test_orders = permutations(sequential_num_list,max_n)
    #note: the product of two numbers whe len > 1 should never   
    unique_product_list = []
    for sequence in test_orders:
        print("On sequence",sequence)
        for y in range(1,len(sequence)-1):
            z = y + 1
            while z < len(sequence):
                a = stringer(sequence[0:y])
                b = stringer(sequence[y:z])
                c = stringer(sequence[z:]) 
                #print(a,b,c)
                if a * b == c:
                    if c not in unique_product_list:
                        unique_product_list.append(c)
                        print("Found a valid answers!")
                z += 1
            y += 1
    print(unique_product_list)
    print("The answer appears to be",sum(unique_product_list))

if __name__ == '__main__':
    print(is_pandigital(923450))
    fun_products(9) #45228