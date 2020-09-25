"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from itertools import combinations

def is_numeric_palindrome(n):
    value = str(n)
    if len(value) % 2 == 0:
        string_list = list(value)
        for x in range(int(len(value)/2)): #only go to the list midpoint
            if string_list[x] != string_list[(x+1)*-1]: #compare the elements reflected over the midpoint
                return False #early exit condition
        return True #all the values match
    else:
        return False

def largest_palindrome_from_digits(n):
    # n is the length of the integer
    start = int("1000"[:n])
    stop = int("9999"[:n])
    max_product = 0
    
    for x in combinations(range(start,stop+1),2):
        product = x[0]*x[1]
        if is_numeric_palindrome(product):
            print("New palindrome found!",product," = ",x[0]," x ",x[1])
            max_product = max(max_product,product)

    print("The largest palindrome from ",n,"digits is ",max_product)

if __name__ == '__main__':
    #I only need to look at the products of all non-duplicate three-digit numbers 100-999, determine if they are a 'palindromic'
    largest_palindrome_from_digits(3)  