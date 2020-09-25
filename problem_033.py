"""Digit cancelling fractions
   Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def solution():
    solution_numerator_prod = 1 
    solution_denom_prod = 1
    for numerator_a in range(1,10):
        for numerator_b in range(1,10):
            #print("Numerator",str(numerator_a) + str(numerator_b))
            full_numerator = int(str(numerator_a) + str(numerator_b))
            reduced_numerator = int(numerator_a)
            for denominator_b in range(1,10):
                full_denominator = int(str(numerator_b)+str(denominator_b))
                reduced_denominator = int(str(denominator_b))
                possible_answer = full_numerator/full_denominator == reduced_numerator/reduced_denominator
                if possible_answer and full_numerator/full_denominator != 1:
                    print("Solution found")
                    print(str(full_numerator) + "/" + str(full_denominator) + " == " + str(reduced_numerator)+"/"+str(reduced_denominator))
                    solution_numerator_prod *= reduced_numerator
                    solution_denom_prod *= reduced_denominator
                #print("Denominator",str(numerator_b)+str(denominator_b))
        
    print(solution_numerator_prod,solution_denom_prod)    
if __name__ == '__main__':
    solution() #easy breezey 100