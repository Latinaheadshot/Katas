# coding = utf-8

def max(a,b):

    if a > b:
        mayor = a
    elif b > a:
        mayor = b
    elif int(a) == int (b):
        return ("son iguales")
    return mayor

valor = max(5,5)

print (valor)