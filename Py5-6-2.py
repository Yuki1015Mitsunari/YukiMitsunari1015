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
def money(a,b,c,d):
    x=a*800
    y=b*950
    z=c*1000
    f=d*650
    m=x+(2*y)+z+f
    return m
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
goukei = money(float(me),float(s),float(kuti),float(kao))
print("金額：￥",goukei)