# Algoritimo 3 - Ponto Fixo

def pon_fix(g,dg,x,e,n):
    if abs(dg(x))>1:
        print("Convergente! Não vai funcionar.")
    else:
        for i in range(1,n):
            xnovo = g(x)
            if abs(xnovo-x)<=e:
                break
            x=xnovo
        print(f"Após {i} iterações, a raiz é {x}.")
        
f = lambda x: x**4 - 2*x**3 + 4*x**2 - 6*x + 3
g = lambda x: (x**4 - 2*x**3 + 4*x**2 + 3)/6
dg = lambda x: (4*x**3 - 6*x**2 + 8*x)/6

pon_fix(g,dg,0,0.001,100)
