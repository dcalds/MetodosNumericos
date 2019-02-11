# Algoritimo 07 - Fatoração LU

A = [[1,1,1],[2,1,-1],[3,2,0]]

def showMatrix(M): # Mostra a matriz
    for i in M:
        print(i,sep=' ')
    print()

def id(n): # Cria Identidade de tamanho n
    
    m = [[0 for i in range(n)]for j in range(n)]
    for i in range(0,n):
        m[i][i]=1
        
    return m

def fatlu(U): # Fatoração LU
    
    n = len(U)
    temp = []
    L = id(n)

    for k in range(n):
        if U[k][k] == 0:
            print('Elemento nulo na posição pivotal.')
            break
        else:
            for i in range(k+1,n):
                m = -U[i][k]/U[k][k]
                temp.append(m)
                L[i][k] = m
                for j in range(k-1,n):
                    U[i][j] = U[i][j] + m * U[k][j]
                    
    return L, U

L,U = fatlu(A) # A = LU

print("# Matriz inicial:")
showMatrix(A)

print("# Matriz L: ")
showMatrix(L)

print("# Matriz U: ")
showMatrix(U)
