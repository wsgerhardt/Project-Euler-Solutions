"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2    =     0.5
    1/3    =     0.(3)
    1/4    =     0.25
    1/5    =     0.2
    1/6    =     0.1(6)
    1/7    =     0.(142857)
    1/8    =     0.125
    1/9    =     0.(1)
    1/10    =     0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def generate_fractional_pattern(d, max_digits):
    i = 0
    trailing_digits = ""
    pattern_not_found = True
    test_pattern = ""

    #kick-off sequence
    value,remainder = divmod(10,d)
    
    while pattern_not_found and i < max_digits:
        if value > 0: 
            trailing_digits += str(value)
            value,remainder = divmod(remainder*10,d)
            i += 1
        elif remainder > 0:
            trailing_digits += str(value)
            value,remainder = divmod(remainder*10,d)
            i += 1
        else:
            break
    #proposed checks
    #1. Repeating number check, from midpoint with first occurence identification
    #2. Repeating sequence check, which is unlikely to have trailing 1's past 
    ##  NOTE: understanding basic leading 0 logic at 1/10 and 1/100 and hard-code that into the algorith   
    return(d, trailing_digits)

def rep_check(pattern,string_to_check):
    string_bump_length = len(pattern) 
    if string_bump_length <= 3:
        rep_count = 10
    else:
        rep_count = 3
        
    continuous_pattern = True
    i = 0
    while continuous_pattern and i < rep_count:
        a = string_to_check[string_bump_length*i:string_bump_length*(i+1)]
        #print("i, a = " + str(i)+", " +str(a))
        if pattern == a:
            i += 1
        else:
            return False #can consider adding point-of-failure value, if it improved algorithmic efficiency.
    return True

def speculative_pattern_test(test_pattern,string_to_check):
    #checks to see if a pattern can be easily found from the current location
        
    
    return 


def find_repeating_pattern(denominator,string_digits,max_digit_value):

    if len(string_digits) < max_digit_value:
        #print("No pattern in terminal 0.",string_digits)
        return ("1/"+str(denominator),"0." + string_digits, None)
    else:
        pattern_not_found = True

    a,b = 0,1 #the search position    
    while pattern_not_found:
        test_pattern = string_digits[a:b]
        #print("testing pattern for 1/" + str(denominator) + ": " + test_pattern)
        
        static_component = string_digits[:a] 
        substring = string_digits[a:] #used to check for repititions
        finder = substring[a+len(test_pattern):].find(test_pattern) #tests to see if the pattern occurs after first occurence
        if finder != -1:
            #checks if see repeating single-digit pattern 
            pattern_not_found =  not rep_check(test_pattern,substring)
            
            #expanded pattern check, for non "a-repeating" patterns
            if pattern_not_found: 
                #print("For 1/" +str(denominator))
                #print("finder",finder)
                expanded_test_pattern = substring[:a+finder+1] #expanded test_pattern
                #print("a,b = " + str(a) +", " +str(b))
                #print("substring",substring)
                #print("expanded_test_pattern",expanded_test_pattern)
                
                if rep_check(expanded_test_pattern,substring):
                    test_pattern = expanded_test_pattern
                    pattern_not_found = False
                else:
                    #check to see what the next_occurance of the string is...
                    speculative_finder = substring[a+finder+1:].find(expanded_test_pattern)
                    #rint("speculative_finder",speculative_finder)
                    if speculative_finder > 0:
                        speculative_pattern = substring[:a+finder+speculative_finder+1]
                        #print("speculative_pattern",speculative_pattern)
                        if rep_check(speculative_pattern,substring):
                            test_pattern = speculative_pattern
                            pattern_not_found = False
                        else: #we know this substring exists! Get it!
                            while pattern_not_found and speculative_finder >= 0 :
                                speculative_finder = substring[a+finder+1:].find(speculative_pattern)
                                speculative_pattern = substring[:a+finder+speculative_finder+1]
                                if rep_check(speculative_pattern,substring):
                                    test_pattern = speculative_pattern
                                    pattern_not_found = False
                                else: #find the next candidate in the string
                                    speculative_finder = substring[a+finder+1:].find(speculative_pattern)
    
                            if speculative_finder <0:
                                a += 1
                                b += 1
    
                            #print("new expanded_test_pattern",expanded_test_pattern)
                    
                    else: #nothing to see here; keep on looking
                        a += 1
                        b += 1

        #for single digit solutions; could be more effective incorporated into the the above if needed
        if finder == -1 or (pattern_not_found and finder > 0):
            a += 1
            b += 1
    
    if pattern_not_found:
        return "ERROR: Pattern not found. :("
    else:
        return ("1/"+str(denominator),"0." + static_component + "(" +test_pattern +")",test_pattern)

if __name__ == '__main__':
    max_length = 0
    max_associated_denominator = 0
    for d in range(2,1000):
        generated_digits = 10000
        a,b = generate_fractional_pattern(d,generated_digits)
        result = find_repeating_pattern(a,b,generated_digits)
        if result[2] is not None and len(result[2]) > max_length:
            max_associated_denominator = d
            max_length = len(result[2]) 
            
        print(result[0],result[1])
        #print("0."+b)
    
    #note the algorithm is slightly broken, but still finds the largest pattern 
    print("THE ANSWER IS",max_associated_denominator,"With a max rep pattern of",max_length)
    #THE ANSWER IS 983 With a max rep pattern of 982
