'''
Created on Apr 24, 2020

@author: wsgerhardt
'''

"""
Triangular, pentagonal, and hexagonal
Problem 45

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle           Tn=n(n+1)/2           1, 3, 6, 10, 15, ...
Pentagonal           Pn=n(3n−1)/2           1, 5, 12, 22, 35, ...
Hexagonal           Hn=n(2n−1)           1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

from functools import lru_cache

def triangle(n,bottom_to_top=True): #start position of bottom or top. 
    if bottom_to_top: 
        i = 0
        while i < n:
            i +=1
            yield i*(i+1)/2 
    else:
        i = n
        while i > 0:
            yield i*(i+1)/2
            i -=1

def pentagonal(n,bottom_to_top=True): #start position of bottom or top.
    if bottom_to_top:
        i = 0
        while i < n:
            i += 1
            yield i*(3*i-1)/2
    else:
        i = n
        while i > 0:
            yield i*(3*i-1)/2
            i -= 1

def hexagonal(n,bottom_to_top=True): #start position of bottom or top.
    if bottom_to_top:
        i = 0
        while i < n:
            i += 1
            yield i*(2*i-1)
    else:
        i = n
        while i > 0:
            yield i*(2*i-1)
            i -= 1


def solution(max_n):
    print("generating triangle numbers")
    a = list(triangle(max_n))
    print("generating pentagonal numbers")
    b = list(pentagonal(max_n))
    print("generating hexagonal numbers") 
    c = list(hexagonal(max_n))
    
    for x in a:
        if x in b and x in c:
            print("New solution found!",int(x))
            print(a.index(x),b.index(x),c.index(x))
            if int(x) > 40755:
                break

def alt_solution(max_n):
    b = pentagonal(max_n,False) 
    c = hexagonal(max_n,False)
    for x in triangle(max_n,False):
        print(x)
        if x in b and x in c:
            print("New solution found!",int(x))
            #print(a.index(x),b.index(x),c.index(x))
    
if __name__ == '__main__':
    solution(100_000) #1533776805
    #alt_solution(100_000) #
    
    
    