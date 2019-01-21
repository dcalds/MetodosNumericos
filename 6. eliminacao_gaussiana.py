# Algoritimo 06 - Eliminação de Gauss (Retrosubstituição)

M = [[1,2,3,1],
     [-1,2,1,2],
     [1,-2,1,3]]


def showMatrix(M): # Mostra a matriz
    for i in M:
        print(i,sep=' ')
    print()

def showVector(V): # Mostra vetor
    n=0
    for i in V:
        n+=1
        print(f" x{n}:", i, end=' ')
        print()

def elmGau(M): # Eliminação Gaussiana (Encontra Matriz Triangular Superior)

    n = len(M)
    xn = []

    for k in range(n):
        if M[k][k]==0:
            print('Elemento nulo na posição pivotal.')
            break
        else:
            for i in range(k+1,n):
                m = -M[i][k]/M[k][k]
                xn.append(m)
                for j in range(k,n+1):
                    M[i][j] = M[i][j] + m * M[k][j]
    return M

def retSub(M): # Retrosubstituição (Encontra Coeficientes xi's)

    n = len(M)
    xn = n*[0]

    for i in range (n-1,-1,-1):
        s = sum([M[i][j] * xn[j] for j in range(i+1,n)])
        xn[i] = (M[i][n]-s)/M[i][i]

    return xn

print('# Matriz Inicial:')
showMatrix(M)

print('# Matriz Triangular:')
M_triangular = elmGau(M)
showMatrix(M_triangular)

print('# Vetor de Coeficientes:')
M_coeficientes = retSub(M)
showVector(M_coeficientes)
