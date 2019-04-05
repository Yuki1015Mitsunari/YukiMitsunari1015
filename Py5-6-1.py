import math
def cicle(a):
    x=a*a*math.pi
    return x

def Rectangle(a,b):
    x = a*b
    return x

def s_(a,b,c,d):
    x = a-(b+c+d)
    return x

a = 11 #顔
b = 2.2 #目
c = 3.5 #口
d = 5.25 #鼻（長さ）
e = 2.1 #鼻（幅）

kao = cicle(a)
me = cicle(b)
kuti = cicle(c)
hana = Rectangle(d,e)
s = s_(kao,me,kuti,hana)
print("白い部分の面積は：",s)