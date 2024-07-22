import math

x = float(input("Digite um valor para x:"))

ln = math.log1p(x)

log10 = math.log10(x)

raiz = math.sqrt(x)

c = x** (x/2)

c2 = x**2

e = math.exp(x)

log2 = math.log2(x)

if x <= 1:
    print(ln)

if 1 < x <= 2:
    print(log10 + raiz)

if 2 < x <= 5:
    print(c2 + e )

if x > 5:
    print(c + log2)