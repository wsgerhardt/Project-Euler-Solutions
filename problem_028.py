"""
Number spiral diagonals
   
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

def early_draft_planning():
    """# note corners will always be the list/array values (n)(x-1) 
    #for x = being the width, from n = 0 to 3   
    
    # the array length will be (x-1)(x-1)
    
    #the number will jump to the most_clockwise position after the first cycle 
    # will always be equal to position... n + 1
    # so the values of the array to be populated will always go from position n+1 to position n
    
    """
    pass

def gen_spirals(max_dimension=3):
    levels = {1:[1]}
    level_number = 3
    starting_number = 2
    while level_number <= max_dimension:
        #print("On level",level_number)
        treshold_number = starting_number + (level_number-1)*4 #will be the max-1 for the spin

        #print("thesthold number is",treshold_number)
        level_number_list = []
        #add level numbers
        for x in range(starting_number,treshold_number):
            level_number_list.append(x)
            
        levels[level_number] = level_number_list 
        #print("level",level_number,"numbers are",levels[level_number])
        level_number += 2
        starting_number = treshold_number
        
        #print("next starting number is",starting_number)

        
    return levels

def sum_of_diagnals(max_dimension=3):
    level_dictionary = gen_spirals(max_dimension)
    growing_total = 0 
    for level in level_dictionary:
        if level==1:
            growing_total += 1
        else:
            """
            bottom_right = (level-1)*1-1
            bottom_left = (level-1)*2-1
            top_left = (level-1)*3-1
            top_right = (level-1)*4-1
            """
            for x in range(1,5):
                corner_location = (level-1)*x-1
                growing_total += level_dictionary[level][corner_location]
            

    print("The solution for a num spiral of max dim",max_dimension,"is",growing_total)
    return growing_total

if __name__ == '__main__':
    gen_spirals(5)
    sum_of_diagnals(3)
    sum_of_diagnals(5)
    sum_of_diagnals(1001)