class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Inserciones:
    def __init__(self):
        self.raiz = None

    def lista_inicial(self, nodo1, nodo2, nodo3, nodo4, nodo5, nodo6, nodo7):
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

        n5 = Nodo(nodo5)
        n4.siguiente = n5
        n4 = n5

        n6 = Nodo(nodo6)
        n5.siguiente = n6
        n5 = n6

        n7 = Nodo(nodo7)
        n6.siguiente = n7
        n6 = n7

    def insertar_en_medio(self, nodo, nodo_nuevo):
        nuevo = Nodo(nodo_nuevo)
        actual = self.raiz

        while actual and actual.dato != nodo:
            actual = actual.siguiente

        if actual:
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.raiz

        while actual:
            print(actual.dato, end= " -> ")
            actual = actual.siguiente
        
        print()

if __name__ == "__main__":
    lita = Inserciones()

    lita.lista_inicial(1, 2, 3, 4, 5, 6, 7)

    lita.mostrar()

    lita.insertar_en_medio(4, 300)

    lita.insertar_en_medio(6, 500)

    lita.mostrar()