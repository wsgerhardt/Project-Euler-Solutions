"""
problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

"""

def sum_of_digits(number):
    print("The solution is",sum([int(x) for x in str(number)]))

if __name__ == '__main__':
    sum_of_digits(2**15)
    sum_of_digits(2**1000) #tada