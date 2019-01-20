# Algorítimo 1 - Bisseção

def bis(f,a,b):
    e=0.001
    n=500
    A=f(a)
    B=f(b)
    i=0
    
    while i<=n:
        x=(a+b)/2
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


bis(lambda x: (x-2)*(x-3),1,2.5)
