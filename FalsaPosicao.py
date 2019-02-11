# Algorítimo 2 - Falsa Posição

def bis(f,a,b,e,n):
    
    A=f(a)
    B=f(b)
    i=1
    
    while i<=n:
        x=(a*B-b*A)/(B-A)
        X=f(x)
        if A*B>=0:
            print("Intervalo pode conter 0 ou um número par de raízes.")
            break
        if X==0 or (b-a)<e or abs(X)<e:
            print(f"Após {i} iterações, a raiz é {x}.")
            break
        i+=1
        if A*X<0:
            b=x    
        else:
            a=x
        if i>n:
            print("Rodou, rodou, e não chegou em lugar nenhum. :(")

f = lambda x: (x-2)*(x-3)
bis(f,1,2.5,0.001,500)
