"""
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def triplet_candidates(candidate_lists,max_sum_value):
    """
    Spent the time to work out a mostly efficient algorithm for the generating the list of candidate tuple.
    The sample this was generated off of was the scenario where the a,b,c values that sum to 12.
    (Solving the solution for *finding* viable pairs of Pythagorean triples is more interesting.)  
    This should limit the range of sets to ones that work, without brute forcing it.
    """ 

    a,b,c = 1,2,max_sum_value-3  #upper bound starting point
    while b < c :
        #
        remaining_sub_sum = max_sum_value - c #what we have to work with after c is defined
        if remaining_sub_sum-1 >= c: #first attmpet at b
            b = c-1
        else:
            b = remaining_sub_sum - 1  
        a = remaining_sub_sum - b
        #we reduce any remaining spread between a and b until we violate the constraint 
        while a < b:
            candidate_lists.append((a,b,c))
            b -= 1
            a += 1
        c -= 1

def unique_triplet(x):
    if x[0]**2 + x[1]**2 == x[2]**2:
        return True
    else:
        return False

def solution(max_sum_value = 12):
    """
    In order to try this out, we need to a few things;
    1) generate the set of numbers where a,b,c sum to 1000 and where a < b < c
    2) Test if they are a triplet
    """
    candidate_lists = []
    triplet_candidates(candidate_lists,max_sum_value)
    solution_position = None
    for n, x in enumerate(candidate_lists):
        print(x)
        if unique_triplet(x):
            solution_position = n
            break
    winner = candidate_lists[solution_position]
    print("The winning product is...",winner[0] * winner[1] * winner[2])

if __name__ == '__main__':
    solution() #for a+b+c = 12
    solution(1000) 