"""
Problem 6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def arbitrary_diff(n=10):
    #seemingly trivial problem546
    square_of_sums = sum(range(1,n+1))**2
    sum_of_squares = 0

    for x in range(1,n+1):
        sum_of_squares += x**2
    
    print("The solution for this problem546 is:",square_of_sums-sum_of_squares)


if __name__ == '__main__':
    arbitrary_diff()
    arbitrary_diff(100)