# Algoritimo 4 - Newton-Raphson

def new_rap(f,df,x,e,n):
    if df(x)==0:
        print("Tu quer mesmo dividir por zero?")
    else:
        for i in range(1,n):
            xnovo = x - (f(x)/df(x))
            if abs(xnovo-x)<=e:
                break
            x=xnovo
        print(f"Após {i} iterações, a raiz é {x}.")

f = lambda x: x**4 - 2*x**3 + 4*x**2 - 6*x + 3
df = lambda x: 4*x**3-6*x**2 + 8*x-6*x + 3
new_rap(f,df,0,0.001,5000)
    
