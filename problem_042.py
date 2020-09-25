"""
Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""


from string import ascii_uppercase as sup
from functools import lru_cache

def word_to_sum(word):
    total = 0
    for character in word:
        total += sup.index(character) + 1
    return total
    
def file_pull():
    word_list = []
    with open("./files/problem42.txt",'r') as f:
        for word in f.read().split(","):
            word = word.replace('"','')  
            word_list.append((word_to_sum(word), word))
    print("generated lst of length",len(word_list))
    return word_list

@lru_cache()
def triangle_number_generator(n):
    return int(n*(n+1)/2)

def is_triangle_number(candidate_number):
    current_triangle_number = 1
    i=1
    while current_triangle_number < candidate_number:
        i += 1
        current_triangle_number = triangle_number_generator(i)
        #print(current_triangle_number)
    if current_triangle_number == candidate_number:
        return True
    else:
        return False

def solution():
    word_numbers = file_pull()
    counter = 0
    for k in word_numbers:
        #print(k)
        if is_triangle_number(k[0]):
            print(k[1],"appears to be a triangle word of length",k[0])
            counter += 1
    print("The solution appears to be",counter)

if __name__ == '__main__':
    word_dict = file_pull()
    max_word = max(file_pull())
    print("SKY is",word_to_sum("SKY"))
    print(is_triangle_number(55))
    solution() #162 Stupid note to self: Don't use dictionary using a non-unique decode value as the key. XP
    