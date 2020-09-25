"""
Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations

def pandigital_0_9_strings():
    return ["".join(x).rjust(10,'0') for x in permutations("0123456789")]
     
def has_odd_property(n_string):
    string_rep = str(n_string)
    #print("for",string_rep)
    remains_true = True
    for i, prime in enumerate((2,3,5,7,11,13,17)):
        #print(i,prime)
        arbitrary_value = ""
        for x in range(2,5):
            arbitrary_value += string_rep[i+x-1]
        if int(arbitrary_value) % prime == 0:
            pass
            #print("d"+str(2+i) +"d"+str(3+i)+"d"+str(4+i), string_rep,"is divisible by",prime) 
        else:
            #print("breaks on","d"+str(2+i) +"d"+str(3+i)+"d"+str(4+i))
            remains_true = False
            break

    if remains_true:
        print("Valid Pandigital number found!",string_rep)
        return int(string_rep)
    else:
        return None

def solution():
    big_sum = 0
    for x in pandigital_0_9_strings():
        #print(x)
        result = has_odd_property(x)
        if result is not None:
            big_sum += int(result)
    
    print("the solution appears to be",big_sum)

if __name__ == '__main__':
    #has_odd_property(1406357289)
    solution() #16695334890
    