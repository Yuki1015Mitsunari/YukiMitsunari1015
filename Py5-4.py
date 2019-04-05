import random
def Rectangle(a,b):
    x1 = a*b
    return x1
def sur(a,b):
    x2 = 2*(a+b)
    return x2

a = input("長辺：")
a = float(a)
b = input("短辺：")
b = float(b)
y=Rectangle(a,b)
z=sur(a,b)
print("面積：",y)
print("周囲：",z)