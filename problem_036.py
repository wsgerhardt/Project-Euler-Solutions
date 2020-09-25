"""
Double-base palindromes
   
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_binary_palindrome(number):
    bin_rep = format(number, 'b')
    reverse_bin_rep = "".join([bin_rep[-i] for i in range(1,len(bin_rep)+1)])
    if bin_rep == reverse_bin_rep:
        #print(number,"is palindrome base 2")
        return True
    else:
        return False

def is_base_10_palindrome(number):
    string_rep = str(number)
    reverse_string_rep = "".join([string_rep[-i] for i in range(1,len(string_rep)+1)])
    if string_rep == reverse_string_rep:
        #print(number,"is palindrome base 10")
        return True
    else:
        return False

def solution():
    all_double_base_palindromes = []
    for x in range(1,1_000_000):
        if is_base_10_palindrome(x) and is_binary_palindrome(x):
            all_double_base_palindromes.append(x)
    
    print("The solution is",sum(all_double_base_palindromes))
    
if __name__ == '__main__':
    #print(format(585, 'b'))
    is_binary_palindrome(585)
    solution() #872187 easy