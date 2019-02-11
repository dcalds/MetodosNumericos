# Algoritimo 12 - Lagrange

def lag(x, y, x0=0):

    tam,res = len(x),0
    L = [0]*tam

    for i in range(tam):
        L[i] = 1
        for j in range(tam):
            if j != i:
                L[i] = L[i] * (x0 - x[j])/(x[i] - x[j])

    for k in range (tam):
        res = res + y[k]*L[k]

    print(res)

x = [1,2,3,4] 
y = [1,4,9,16]
x0 = 2.5

lag(x, y, x0)
