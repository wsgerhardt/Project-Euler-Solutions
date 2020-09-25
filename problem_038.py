"""
Pandigital multiples
   
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from functools import lru_cache

@lru_cache()
def turn_into_attmpted_pandigital(i,n):
    big_number = ""
    for x in range(1,n+1):
        big_number += str(i*x)
    return big_number

def is_pandigital_product(i,n):
    big_number = turn_into_attmpted_pandigital(i,n)
    check = list(big_number)
    check.sort()
    if "".join(check) =="123456789":
        return True
    else:
        return False

def max_i():
    i=99999
    while i > 0 and is_pandigital_product(i,2) is not True:
        i -= 1
        print(i)
    print("i solution for min n is",i)

def solution():
    max_theoretical_pandigital = 987654321 
    min_theoretical_pandigital = 123456789

    #the largest starting intiger will be i <= 9327 and 2
    #For the smallest starting integer 1, the largest n value will be... 9

    i = 1
    max_pandigital = 0
    wining_solution = (1,1)
    while i <= 9327:
        n = 1
        while n <= 9:
            attempted_result = int(turn_into_attmpted_pandigital(i,n))
            if attempted_result > 987654321:
                break #onto the next integer values!
            elif is_pandigital_product(i,n):
                if attempted_result > max_pandigital:
                    max_pandigital = attempted_result
                    wining_solution = (i,n)
            n += 1
        i += 1

    print("The max pandigital number is",max_pandigital,"for i =",wining_solution[0],"and n =",wining_solution[1])
    return max_pandigital, wining_solution

if __name__ == '__main__':
    print(is_pandigital_product(192,3))
    print(is_pandigital_product(9327,2))
    print(is_pandigital_product(1,9))
    solution()
    print(is_pandigital_product(9327,2)) #tada
