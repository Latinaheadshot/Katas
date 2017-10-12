class Lista():

    def __init__(self):
        self.lista = []

    def capturaLista():
       # Captura la lista hasta recibir un elemento vacío mediante la tecla [Enter]
       elemento = "vacio"
       lista = []
       while elemento != "": # mientras que elemento sea distinto de vacío continua capturando elementos para la lista
           elemento = input("Ingresa el elemento a agregar a la lista, para terminar presiona [Enter]: ")
           if elemento != "": # si el elemento es vacío termina bucle y regresa la lista
                lista.append(elemento)
                print(elemento)
           else:
                print(elemento)
                return lista
       else:
           # no capturar mas elementos
           return lista
lista = Lista
#lista.capturaLista()

print ("La longitud de la lista es: ", len(lista.capturaLista()))