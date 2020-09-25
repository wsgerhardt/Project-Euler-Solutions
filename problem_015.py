from functools import lru_cache

@lru_cache()
def reciprocate_grid(a,b):
    # I use a right-biased incrementation approach.
    x,y = a,b
    running_node_total = 0
    if x==1 and y==1:
        return 2
    else:
        if x > 0 and y > 0:
            if x == y: #taking advantage of symmetrical properties
                running_node_total += 2 * reciprocate_grid(x-1,y)
            else:
                running_node_total += reciprocate_grid(x,y-1)
                running_node_total += reciprocate_grid(x-1,y)
        else:
            return 1

    print((x,y),running_node_total)
    return running_node_total

if __name__ == '__main__':
    print(reciprocate_grid(1,1))
    print(reciprocate_grid(2,2))
    print(reciprocate_grid(3,3))
    print(reciprocate_grid(20,20)) #that was surprisingly fast and easy... so long as you use caching. :o)