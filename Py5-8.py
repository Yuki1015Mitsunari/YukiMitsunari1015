import tables
import random
def random(a):
    x = a
    return x
def average(a,b,c):
    x = (a+b+c)/3
    return x
def grade(a):
    if a>=90:
        x="A"
        return x
    elif a>=80:
        x="B"
        return x
    elif a>=70:
        x="C"
        return x
    elif a>=60:
        x="D"
        return x
    else:
        x="F"
        return x

a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)
d = average(a,b,c)
x=tables()
x.field_names=[SutudentID,Subject1,Subject2,Subject3,Average,Grades]
x.add_row(["A001",random(a),random(b),random(c),average(a,b,c),grade(d)])