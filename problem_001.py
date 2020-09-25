"""
Problem 1: (Difficulty 5%)

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def sum_of_all_multiples_below(max=10):
    #sums all values for the given number that are multiples of either 3 or 5. 
    int_list = []
    natural_number_list = list(range(max))
    
    for x in natural_number_list:
        if not x%3 or not x%5:
            int_list.append(x)

    return sum(int_list)

if __name__ == '__main__':
    #initial test
    first_result = sum_of_all_multiples_below()  
    if first_result == 23:
        print("Hey, it works. You got 23!")
    else:
        print("Better luck next run.")
    
    
    solution = sum_of_all_multiples_below(1000)
    print("The sum of all multiples of 3 or 5 below 1000 is:\n",solution)