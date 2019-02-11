# Algoritimo 11 - Neville (Fórmula de Lagrange)

def nev(x, y, x0):

    tam = len(x)
    Q = [0]*tam

    for k in range(tam):
        for j in range(tam-k):
            if k == 0:
                Q[j] = y[j]
            else:
                Q[j] = ((x0 - x[j+k] ) * Q[j]+ \
                        (x[j] - x0) * Q[j+1]) / \
                        (x[j] - x[j+k])


    print(Q[0])

x = [1,2,3,4]
fx = [1,4,9,16]
x0 = 2.5

nev(x, fx, x0)
