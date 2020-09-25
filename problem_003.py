"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def prime_factorize(n):
    factors_found = []
    x = 2 #integer
    running_sub_factor = n
    while running_sub_factor > 1:
        if running_sub_factor % x == 0:
            factors_found.append(str(x))
            print("factor found",x)
            running_sub_factor /= x
        x+=1
    print("The prime factors of",str(n),"are",", ".join(factors_found))
    print("The largest prime factor of",str(n),"is",factors_found[-1])

if __name__ == '__main__':
    prime_factorize(600851475143)