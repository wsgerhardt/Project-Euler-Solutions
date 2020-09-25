from pathlib import Path

def populate_matrix(matrix_list):
    with open('.//files//problem11.txt') as prime_identifier:
        output = prime_identifier.read()
        rows = output.split('\n')
        for x in rows:
            matrix_list.append(x.split(' '))
 
def string_product(a_list):
    x = 1
    for element in a_list:
        x *= int(element)
   
    return x
 
def scrape_lines_from_2020_matrix(n):
    #pulls all sequences of lenght n from a 20 x 20 matrix
    matrix_list = []
    populate_matrix(matrix_list)
    
    max_product = 0
        
    print("#vertical sweep")
    #boring case
    for row in matrix_list:
        print(row)
        for p, num in enumerate(range(0,len(row)+1-n)):
            candidate_numbers = [int(a) for a in row[p:p+n]]
            print(candidate_numbers)
            new_string_product = string_product(candidate_numbers)
            max_product = max(max_product,new_string_product) 
   
    print("#horizonal sweep")
    x = matrix_list
    for p in range(0,21-n):
        for q in range(0,20):
            candidate_numbers = [int(x[p+n][q]) for n in range(0,4)]
            print(candidate_numbers)
            new_string_product = string_product(candidate_numbers)
            max_product = max(max_product,new_string_product)
    
    print("#right diagonal sweep")
    x = matrix_list
    for p in range(0,21-n):
        for q in range(0,21-n):
            candidate_numbers = [int(x[p+n][q+n]) for n in range(0,4)]
            print(candidate_numbers)
            new_string_product = string_product(candidate_numbers)
            max_product = max(max_product,new_string_product)

    print("#left diagonal sweep")
    x = matrix_list
    for p in range(0,21-n):
        for q in range(3,20):
            candidate_numbers = [int(x[p+n][q-n]) for n in range(0,4)]
            print(candidate_numbers)
            new_string_product = string_product(candidate_numbers)
            max_product = max(max_product,new_string_product)


    print("The maximum product amount is",max_product)

if __name__ == '__main__':
    scrape_lines_from_2020_matrix(4)