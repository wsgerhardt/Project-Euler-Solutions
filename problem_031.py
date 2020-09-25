"""Coin sums
   
Problem 31

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

coin_decode = {0:1,
            1:2,
            2:5,
            3:10,
            4:20,
            5:50,
            6:100,
            7:200}

def coin_divider(amount,coin_key):
    #coin key is the largest denomination to be divided by
    coin_denom = coin_decode[coin_key]
    max_div = amount // coin_denom 
    #print("max div for coin",coin_decode[coin_key],"on amount",amount,"is",max_div)
    variations_on_a_coin = []
    if coin_key > 0:
        i = 0
        while i <= max_div:
            number_of_coin = max_div-i
            remaining = amount - coin_denom*(number_of_coin)
            #print(number_of_coin,remaining)
            #create a list of sub-possibilities on the remainder
            for possibility in coin_divider(remaining,coin_key-1):
                current_sub_set = [(coin_denom,number_of_coin)] + [x for x in possibility]
                variations_on_a_coin.append(current_sub_set)
            i += 1
    else:
        variations_on_a_coin.append([(coin_denom,max_div)])
    
    variations_on_a_coin.sort(key = lambda x: x[0][1],reverse=True)
        
    return variations_on_a_coin
    
def solution():
    variation_list = coin_divider(amount=200,coin_key=7)
    print("The Solution is ",len(variation_list))
        
if __name__ == '__main__':
    a = coin_divider(amount=10,coin_key=2)
    for row in a:
        print(row) 

    solution()    