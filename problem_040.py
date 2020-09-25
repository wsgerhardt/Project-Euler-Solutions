"""
Champernowne's constant
   
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def slightly_inefficient_champernowne(max_number_deiminals):
    growing_len = 0
    champernowne = ""
    i = 0
    while growing_len < max_number_deiminals:
        i += 1
        champernowne += str(i)
        growing_len += len(str(i))
                
    return champernowne

def solution():
    long_string = slightly_inefficient_champernowne(1_000_000)
    solution = 1
    for x in range(0,7):
        solution *= int(long_string[1*10**x-1])
    print("The solution is",solution)

if __name__ == '__main__':
    print(slightly_inefficient_champernowne(1))
    print(slightly_inefficient_champernowne(10))
    print(slightly_inefficient_champernowne(10)[9])
    solution() #easy