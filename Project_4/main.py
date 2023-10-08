def printMove(one, two):
    print('move from ' + str(one) + ' to ' + str(two))


def Towers(n, one, two, three):
    if n == 1:
        printMove(one, two)
    else:
        Towers(n-1, one, three, two)
        Towers(1, one, two, three)
        Towers(n-1, three, two, one)

n = int(input("enter number of disk: "))
x = Towers(n, '1', '2', '3')
print(x)
