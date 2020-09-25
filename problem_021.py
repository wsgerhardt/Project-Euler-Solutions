"""
Amicable numbers
   
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

def find_divisors(number):
    #note, the result of the smallest divisor will also be the max
    divisor_candiate = 2
    max_value = number
    i = divisor_candiate
    divisor_list = [1]
    while i < max_value: 
        a,b = divmod(number,i)
        if b == 0:
            divisor_list.append(i)
            divisor_list.append(a)
            max_value = a
        i += 1

    return divisor_list

def is_amicable(number):
    sum_test = sum(find_divisors(number))
    if sum_test != number and number == sum(find_divisors(sum_test)):
        return True
    else:
        return False 

def solution():
    solution = 0
    for x in range(1,10000):
        if is_amicable(x):
            solution += x

    print("The sum of all the amicable numbers under 10000 is",solution)

if __name__ == '__main__':
    a = find_divisors(220)
    a.sort()
    print(a,is_amicable(220))
    solution()    
    