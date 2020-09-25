"""
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

"""
    Planning:
    We are looking at integers under or equal to 28123
    We are looking for the sum of all integers under or equal to 28123 that cannot 
        be written as the sum of two abundant numbers.
    
    All that is needed to solve this problem is find perfecte numbers, then abundant numbers.    
"""

from itertools import combinations_with_replacement

def factor_lookup_leql(n):
    factor_dict = {}
    for x in range(1,n+1):
        factor_list = []
        for i in range(1,x):
            if x % i == 0:
                factor_list.append(i)
        factor_dict[x] = factor_list
    print("generated factor_dict containing",len(factor_dict),"values")
    return factor_dict

def abundant_sums_list_leql(n):
    abundant_list = []
    f_dict = factor_lookup_leql(n)
    for x in range(1,n+1):
        if sum(f_dict[x]) > x:
            abundant_list.append(x)
    return abundant_list 

def abundent_summable_set(n):
    abundnat_list = abundant_sums_list_leql(n)
    combos = list(combinations_with_replacement(abundnat_list,2))
    available_abundent_values = []
    print("calculating all pairs from",len(combos),"combinations")
    for pair in combos:
        value = pair[0]+pair[1]
        if value <= n:
            available_abundent_values.append(value)
    print("attempting to make a set...")
    resulting_set=set(available_abundent_values)
    print("There are ",len(resulting_set),"numbers leql to",n,"that can be generated from the sum of two abundant numbers")
    print("the min is",min(resulting_set),"and the max is ",max(resulting_set))
    return resulting_set

def solution():
    summation = 0
    all_below_abundant_thresh = set([x for x in range(1,28124)])
    summable_set = abundent_summable_set(28123)
    #print("we have a set of all summable abundant numbers")
    diff_set = all_below_abundant_thresh-summable_set
    print("there are",len(diff_set),"elements that cannot be summed from abundant numbers")
    print("the min is",min(diff_set),"and the max is",max(diff_set))
    solution = sum(list(diff_set))
    print("The sum of these numbers is ",solution)
    return solution

if __name__ == '__main__':
    print(solution(),"is the solution") #!!!!! fixing it so it was combaintions with replacements did the trick.
    