def solution():
    with open('.//files/problem13.txt') as prime_identifier:
        summation = sum([int(x) for x in prime_identifier.readlines()])
        print("The solution is",str(summation)[:10])

if __name__ == '__main__':
    solution() #easy breezey