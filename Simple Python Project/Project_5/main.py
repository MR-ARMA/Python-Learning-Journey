def print_rangoli(size):
    # your code goes here
    import string
    
    alphabet = string.ascii_lowercase
    list_1 = [alphabet[i] for i in range(size - 1, -1, -1)]
    
    for i in range(len(list_1)):
        line = list_1[: i]
        sol = []
        sol.extend(line)
        sol.append(list_1[i])
        sol.extend(line[::-1])
        print("-".join(sol).center(4 * size - 3, "-"))
    


    for i in range(len(list_1) - 2, -1, -1):
        line = list_1[: i]
        sol = []
        sol.extend(line)
        sol.append(list_1[i])
        sol.extend(line[:: -1])
        print("-".join(sol).center(4 * size - 3, "-"))
        
        
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)