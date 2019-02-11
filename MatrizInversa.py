# Algoritimo 10 - Inverter Matriz

def showMatrix(M): # Imprime matriz
    for i in M:
        print(i, sep=' ')
    print()
    
def idn(n): # Cria matriz identidade de tamanho n
    m = [[0 for l in range(n)] for c in range(n)]
    for i in range(n):
        m[i][i] = 1
    return m

def inv(M):                     # Inverter matriz
    n = len(M)                  # Tamanho da matriz
    inv = idn(n)                # Cria identidade do tamanho da matriz recebida
    start = list(range(n))      # Cria lista com tamanho da matriz
    
    for dg in range(n):         # dg simula a diagonal principal
        dg_sc = 1.0 / M[dg][dg] 

        for col in range(n):      # col simula as colunas
            M[dg][col] *= dg_sc     
            inv[dg][col] *= dg_sc 

        for i in (start[0:dg] + start[dg+1:]):      # Ignora a diagonal principal
            esc = M[i][dg]                          
            for j in range(n):                      
                M[i][j] = M[i][j] - esc * M[dg][j]  
                inv[i][j] = inv[i][j] - esc * inv[dg][j]

    return inv

A = [[2,2,3],
     [4,5,6],
     [7,8,9]]

print("# Matriz Inicial: ")
showMatrix(A)

a = inv(A)

print("# Matriz Invertida: ")
showMatrix(a)
