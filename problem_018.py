
"""
problem 18
Same solution as problem 18

Note, for this problem I originally attmpted a more convoluted solution involved a convoluted ranking appraoch,
which I abandoned when it was apparent it was unworkable. 

"""

def read_triangle_simple(sample = None):
    holding_array = []
    if sample is None:
        with open("./files/problem18.txt",'r') as prime_identifier:
            for i, line in enumerate(prime_identifier.readlines()):
                row =  [int(x.replace('\n',""))for x in line.split(" ")]
                holding_array.append(row)
    return holding_array


def return_row(triangle_row):
    return " ".join([str(item).rjust(2,"0") for item in triangle_row])

def roll_up(triangle_set):
    # we need to fix the maximum sum from top to bottom for this to work.
    sum_set = triangle_set[:]
    sum_set.reverse() 
    
    for i, row in enumerate(sum_set[1:],1):
        for j, element in enumerate(row):
            sum_set[i][j] += max(sum_set[i-1][j],sum_set[i-1][j+1]) 

    sum_set.reverse()

    return sum_set 
        
def process():
    values = read_triangle_simple()
    summed_up_values = roll_up(values)
    for x in summed_up_values:
        print(return_row(x))
    
if __name__ == '__main__':
    process()
    