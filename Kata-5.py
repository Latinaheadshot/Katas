class Operaciones():
    def __init__(self):
        pass
    def suma(self,lista):
        suma = 0
        for x in range(0,len(lista)):
            suma = suma + lista[x]
        return suma

    def multiplicacion(self,lista):
        multiplicacion = 1
        for x in range(0,len(lista)):
            multiplicacion = int(multiplicacion) * int(lista[x])
        return multiplicacion

lista = [1,2,3,4]
resultados = Operaciones()
suma = resultados.suma(lista)
multi = resultados.multiplicacion(lista)

print(suma)
print(multi)

