def makeChange(setOfChange,value):
    print setOfChange
    D = range(value)
    D[0] = 1
    for i in range(value)[1:]:
        D[i] = 0

    print D

    for v in range(value)[1:]:
        print v, D
        for x in setOfChange:
            if x <= v:
                D[v] = D[v] + D[v-x]
            else:
                D[v] = 0
    return D[value-1], D



print makeChange([3,7],18)


