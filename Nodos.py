class Nodo():
    def __init__(self,dato,siguiente = None):
        self.dato = dato
        self.siguiente = siguiente
    def isEmpty(self):
        return self.dato == None

def recorrer(nodo):
    cont = 0
    while nodo != None:
        print(nodo.dato)
        cont = cont + 1
        nodo = nodo.siguiente
    print ("Tamaño de la lista: ",cont)


nodo4 = Nodo(12)
nodo3 = Nodo(45,nodo4)
nodo2 = Nodo(67,nodo3)
nodo1 = Nodo(89,nodo2)

recorrer(nodo1)
print("¿Esta vacio? ",nodo1.isEmpty())
