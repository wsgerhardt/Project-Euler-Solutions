"""
Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

def the_prime_directive(n=6):
    #I'm clearly getting bored with normal function names
    #determines what the the nth prime number is
    #A computational drag. Probalby would be more efficient if I dumped the lists.
    
    prime_contender = 3 #the prime 2 is bakes into the formulas before, so we start on 3
    prime_list = [2]
    while True:
        if len(prime_list) == n:
            break
        for x in range(2,prime_contender):
            if prime_contender % x == 0:
                break
            if x == prime_contender-1: #no other candidates for prime  
                #print("New prime found!",prime_contender)
                prime_list.append(prime_contender)
            
        prime_contender +=1
    
    print("Item",n,"in the set of",n,"prime numbers is",prime_list[-1])

if __name__ == '__main__':
    the_prime_directive(10001) 