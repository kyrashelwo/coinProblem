def makeChange(setOfChange,value):
# D[i] states if we found a way to reach i.
    D = [0] * (value + 1)
# 0 is trivial to reach.
    D[0] = 1

# coins[i] states which and how much coins we used to reach i.
    coins = [[0 for x in range(len(setOfChange))] for x in range(value + 1)]

# check if we can reach value v
    for v in range(value + 1)[1:]:
        #print v, D
        #print coins
        for x in setOfChange:
            if x <= v:
                if D[v] == 0:
                    if D[v-x] != 0:
                        D[v] = 1
                        for i in range(len(setOfChange)):
                            coins[v][i] = coins[v-x][i]
                        coins[v][setOfChange.index(x)] += 1
                        break
    return D[value], coins[value]

print makeChange([6,9,20],44)


