class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Inserciones:

    def __init__(self):
        self.raiz = None

    def lista_inicial(self, nodo1, nodo2, nodo3, nodo4):
        self.raiz = Nodo(nodo1)
        n1 = self.raiz

        n2 = Nodo(nodo2)
        n1.siguiente = n2
        n1 = n2

        n3 = Nodo(nodo3)
        n2.siguiente = n3
        n2 = n3

        n4 = Nodo(nodo4)
        n3.siguiente = n4
        n3 = n4

    def insertar_final(self, nodo_final):
        nuevo = Nodo(nodo_final)
        
        actual = self.raiz
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def mostrar(self):
        actual = self.raiz

        while actual:
            print(actual.dato, end = " -> ")
            actual = actual.siguiente

        print()
    
if __name__ == "__main__":
    lita = Inserciones()

    lita.lista_inicial(1, 2, 3, 4)

    lita.mostrar()

    lita.insertar_final(5)

    lita.mostrar()
