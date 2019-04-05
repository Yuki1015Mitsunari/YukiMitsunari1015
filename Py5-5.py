import random
def saikoro(a,b):
    if a==b:
        x = "Lucky"
        return x
    else:
        x1 = "Unlucky"
        return x1

a = random.randint(1,6)
b = random.randint(1,6)
y=saikoro(a,b)
print(y)
print("a:",a,"b:",b)