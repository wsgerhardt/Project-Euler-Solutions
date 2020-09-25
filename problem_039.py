"""
Integer right triangles
   
Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from math import sqrt
from functools import lru_cache

def is_right_triangle(a,b,c):
    if c**2 == a**2 + b**2:
        return True
    else:
        return False

"""another min max problem..."""
def determine_min(p):
    #note, the solution must have integral sides, which means that you can limit your range. 
    a, b, c = 1,1, p-2 
    triangle_list = []
    while c < b < a:
        if is_right_triangle(a,b,c):
            triangle_list
        else:
            pass
    return a,b,c
        
def c_value_candidates(p):
    #turns out its is likely unneeded
    candidate_list = []
    i = 1
    while i < p:
        candidate_list.append((i,i**2))
        i += 1
    return candidate_list
    
@lru_cache()
def a_b_value_candidates(p):
    #originally titled, a_b_value_candidates
    outcome_list = []
    for c in range(1,p-2):
        b = p - c - 1
        a = 1
        while b >= a:
            if is_right_triangle(a,b,c):
                outcome_list.append((a,b,c))
            a += 1
            b -= 1
    return outcome_list 

def solution(p_max):
    # max number of solutoin for p ≤ p_max
    p = p_max
    max_length = 0
    winning_p = p
    max_solutions = []
    while p > 1:
        print(p)
        candidate_solutions = a_b_value_candidates(p)
        candidate_length = len(candidate_solutions) 
        if candidate_length > max_length:
            max_solutions = candidate_solutions
            max_length = candidate_length
            winning_p = p
        p -= 1

    print("The winning p value is",winning_p,"with",max_length)
    print(max_solutions)
    
if __name__ == '__main__':
    print(is_right_triangle(20,48,52))
    c_value_candidates(120)
    #print(c_value_candidates(1000))
    a_b_value_candidates(1200)
    solution(1000) #slooooow until you hit the lower numbers
    #The winning p value is 840 with 8
    
     