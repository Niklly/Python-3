x =  float(input())
y = float(input())

if (x > 0  and y > 0 ):
    print("I")

if (x > 0 and y < 0):
    print("IV")

if (x < 0 and y > 0):
    print("II")

if (x < 0 and y < 0):
    print("III")

if (x == 0  or y == 0):
    print("EIXOS")
