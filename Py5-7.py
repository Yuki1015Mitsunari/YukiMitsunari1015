import requests
def discomfort(x,Td,Tw):
    DI=0.72*x*(Td+Tw)+40.6
    return DI
