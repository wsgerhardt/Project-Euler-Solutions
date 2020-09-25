"""
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""


from functools import lru_cache

@lru_cache()
def quick_fib(n):
    #god bless caching :)
    if n==1 or n ==2:
        return 1
    else:
        return quick_fib(n-1) + quick_fib(n-2)


def the_big_fib(max_digits):
    i= 1
    result_len = 0
    while result_len != max_digits: 
        result_len = len(str(quick_fib(i)))
        i+=1
    
    print("The index of the first fib sequence with",max_digits,"digits is",i-1)
if __name__ == '__main__':
    the_big_fib(3)
    the_big_fib(1000)