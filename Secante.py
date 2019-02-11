# Algoritimo 05 - Secante

def secante(f,x0,x1,e,n):
    i=1
    while i<=n:
        xnovo = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        if abs(f(xnovo))<e or abs(xnovo - x1)<e:
            print(f"Após {i} iterações, a raiz é {x2}.")
            break
        x0 = x1
        x1 = xnovo
        i+=1
    if i>n:
        print("Rodou, rodou, e não chegou em lugar nenhum. :(")

f = lambda x: (x-2)*(x-3)
secante(f,-1000,1000,0.001,5000)

