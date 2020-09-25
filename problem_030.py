"""

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def sum_of_power_digits(digit,power):
    return sum([int(x)**power for x in str(digit)])

def powers_of_digits(power=4):
    positive_matches = []
    too_much_power = False
    for x in range(2,999999):
        value = sum_of_power_digits(x,power)
        print(x,value)
        if x == value:
            positive_matches.append(x)
            print("POSITIVE MATCH FOUND")
    print(" ".join([str(x) for x in positive_matches]))
    print("The sum of all " + str(power) + "th digit power numbers is",sum(positive_matches))
    
if __name__ == '__main__':
    print(sum_of_power_digits(999999,5)) 
    #powers_of_digits(5) #can blindly find the answer by making the upper range 10,000,000. 
    #You find the naswer is the numbers: 4150 4151 54748 92727 93084 194979 = 443839
        