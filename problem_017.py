"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
"""

num_dict = { 0:"", 
            1:"one",
            2:"two",
            3:"three",
            4:"four",
            5:"five",
            6:"six",
            7:"seven",
            8:"eight",
            9:"nine",
            10:"ten",
            11:"eleven",
            12:"twelve",
            13:"thirteen",
            14:"fourteen",
            15:"fifteen",
            16:"sixteen",
            17:"seventeen",
            18:"eighteen",
            19:"nineteen",
            20:"twenty",
            30:"thirty",
            40:"forty",
            50:"fifty",
            60:"sixty",
            70:"seventy",
            80:"eighty",
            90:"ninety",
            100:"hundred",
            1000:"thousand"
}


def count_me_down(number):
    #counts the characters of long-form spelling of numbers between 1 and max
    running_total = 0
    formed_word = ""
    
    i = number
    if i > 1000:
            raise ValueError("Sorry, number must be less than 1000.")
    
    while i >= 1:
        #fills the forme word...
        s = str(i).rjust(4,"0")
        formed_word = "" #reset
        #thousand check
        if int(s[0]) >= 1: #find the thousand's spot
            formed_word += num_dict[1] + " "
            formed_word += num_dict[1000] + " "
        if int(s[1]) >= 1: #fill the hundreds spot
            #hundred value is...
            formed_word += num_dict[int(s[1])] + " " 
            formed_word += num_dict[100] + " "
            if int(s[2:]) > 0: #and conditional
                formed_word += "and "
        if int(s[2:]) >= 20: #fill the remaining spot
            formed_word += num_dict[int(s[2])*10] + " "
            formed_word += num_dict[int(s[3])]
        if int(s[2:]) < 20: #fill the remaining spot
            formed_word += num_dict[int(s[2:])]
            
        print(i,formed_word)
        running_total += len(formed_word.strip().replace(" ","")) #strip and replace all whitespace
        i -= 1
    
    print("The total word count is",running_total)
        
if __name__ == '__main__':
    count_me_down(1000)