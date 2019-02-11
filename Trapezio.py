# Algoritimo 13 - Trapézio (Integração Numérica)

import math

def a(x):
    return math.exp(x)

def trap(n,x0,xn,f):
    if n<0:
        print("Divisão por zero")
    else:
        if n<0:
            print("Intervalo Inválido")
        else:
            h = (xn-x0)/n
            x = x0+h
            soma = 0
            for i in range(n-1):
                soma = soma + f(x)
                x = x + h
            R = h*((f(x0) + f(xn))/2 + soma)
            print("O Resultado da integral da função é", R)

trap(4,1,2,a)
