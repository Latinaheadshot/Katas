import sys


class Histograma():
    def __init__(self):
        pass

    def histograma_elemento(self, elemento):
        for x in range (1,elemento):
            sys.stdout.write('*')
        print('')


lista = [4, 9, 7]
histo = Histograma()
for x in range (0,len(lista)):
    histo.histograma_elemento(lista[x])

