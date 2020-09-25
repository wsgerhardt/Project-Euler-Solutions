"""
Quadratic primes
   
Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41

is clearly divisible by 41.

The incredible formula n2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n2+an+b

, where |a|<1000 and |b|≤1000

where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a and b, 
for the quadratic expression that produces the maximum number 
of primes for consecutive values of n, starting with n=0.
"""

from functools import lru_cache

def prime_41():
    prime_list = []
    for n in range(0,40):
        prime_list.append(n**2 + n + 41)
    for x in prime_list:
        print(check_if_prime(x))
        print(x)
    return prime_list


def test():
    over_41 = prime_41()
    #test appraoch to see if id all prime numbers under 41
    accurate_41_and_over_list = []
    false_primes = []
    under_41 = []
    for n in range(2,1602):
        prime_status = check_if_prime(n)
        if n < 41:
            if prime_status:
                under_41.append(n)
        if n >= 41:
            if prime_status:
                if n not in over_41:
                    false_primes.append(n)
                else:
                    accurate_41_and_over_list.append(n)
    
    
    #print(under_41)
    #print(accurate_41_and_over_list)
    #print("POSSIBLE FALSE PRIMES",false_primes)
    
    double_check = True 
    for prime in false_primes:
        for x in range(2,prime):
            if prime % x == 0:
                double_check = False
                print(prime,"fails on",x)
                
    print("double_check status is",double_check)
    if double_check:
        print("No false primes")

@lru_cache()
def check_if_prime(number):
    if number <0: #if you don't add this condition you get a slow and wrong response!
        return False 
    elif number == 2 or number == 3:
        return True
    else:
        prime_status = number % 2 != 0  
        i = 3
        while prime_status and i < int(number/3):
            if number % i == 0:
                prime_status = False
            else:
                i += 2

        return prime_status


def how_many_generated_primes(a,b):
    max_number_of_consecutive_primes = 0
    i= 0
    last_digit_was_prime = True
    while last_digit_was_prime:
        if check_if_prime(i**2 +a*i + b):
            max_number_of_consecutive_primes += 1
        else:
            last_digit_was_prime = False
        i += 1
        
    return max_number_of_consecutive_primes

def solution():
    #is not especially efficient
    top_a,top_b = -999,-1000
    max_prime_count = 0
    for a in range(-999,1000):
        for b in range(-1000,1001):
            #print("checking values for n**2 +" +str(a) + "*n + "+str(b))
            test = how_many_generated_primes(a,b)
            if test > max_prime_count:
                max_prime_count = test
                top_a,top_b = a,b
                print("new max found",max_prime_count,"for ab",top_a,top_b)

    print("The solution is " + str(top_a*top_b)+ " for a,b=("+ str(top_a) + "," + str(top_b) +"), count = " + str(max_prime_count))

if __name__ == '__main__':
    #test()
    print(how_many_generated_primes(1,41))
    print(how_many_generated_primes(-79,1601))
    solution() #The solution is -59231 for a,b=(-61,971), count = 71.. 
    