"""
Prlblem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

## Note: The algorithm here is *really* inefficient. I am going to try later to see if it'ss faster in C.

def sum_of_all_primes(max_prime=10):
    #reurposed code from problem 7 with slightly faster algorithm for prime factoring 
    
    prime_contender = 3 #the prime 2 is bakes into the formulas before, so we start on 3
    prime_list = [2]
    while True:
        if prime_contender == max_prime:
            break
        #check to see if we can factor from the existing knonw primes first
        can_easily_factor = False
        for x in prime_list:
            if prime_contender % x == 0:
                can_easily_factor = True
                break
        #check to see if we can factor from any number larger than the last known prime
        if can_easily_factor is False:
            for x in range(prime_list[-1],prime_contender):
                #normal method
                if prime_contender % x == 0:
                    break
                
                if x == prime_contender-1: #no other candidates for prime  
                    #print("New prime found!",prime_contender)
                    prime_list.append(prime_contender)

        prime_contender +=1
    
    print("the sum of all primes below",max_prime,"is",sum(prime_list))

if __name__ == '__main__':
    sum_of_all_primes()
    sum_of_all_primes(2000000) #142913828922 slow as hell. Probably a faster way to calculate this and using multi-threading, counting from top to bottom.
    