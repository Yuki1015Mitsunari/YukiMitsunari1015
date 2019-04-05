import math
def cicle(a):
    x1=a*a*math.pi
    x2=2*a*math.pi
    return x1,x2

a = input("半径：")
a = float(a)
y=cicle(a)
print("(面積,周囲)：",y)