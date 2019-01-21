# Algoritimo 08 - Gauss Jacobi

def showMatrix(M):
    for i in M:
        print(i, sep=' ')
    print()

def gaussJ(A, b):

    xo = [0,0,0] # Chutes
    N = 500 # Limitador de Iterações
    e = 0.001 # Erro
    n = len(A)
    k = 1
    x = [0 for i in range(n)]
    
    
    while k <= N:
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += A[i][j] * xo[j]
            x[i] = (b[i] - soma) / A[i][i]

            X = []

            for a in range(n):
                X.append(abs(x[a]-xo[a]))
            if max(X) < e:
                return x
        k+=1
        for i in range(n):
            xo[i] = x[i]
    return ("Rodou, rodou e não chegou em lugar nenhum.")

A = [[10,2,1],[1,5,1],[2,3,10]]
b = [7,-8,6]

print("# Matriz A: ")
showMatrix(A)

print("# Vetor b: ")
print(b)
print()

print("# Matriz de Coeficientes xi's: ")
print(gaussJ(A,b))
