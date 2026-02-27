class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Inserciones:
    def __init__(self):
        self.raiz = None

    def lista_inicial(self, nodo1, nodo2, nodo3, nodo4, nodo5):
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

    def insertar_en_medio(self, posicion, nuevo_nodo):
        nuevo = Nodo(nuevo_nodo)
        actual = self.raiz

        while actual and actual.dato != posicion:
            actual = actual.siguiente

        if actual:
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.raiz

        while actual:
            print(actual.dato, end= " -> ")
            actual = actual.siguiente

        print("")

if __name__ == "__main__":
    lita = Inserciones()


    lita.lista_inicial(2, 4, 6, 8, 10)

    lita.mostrar()

    lita.insertar_en_medio(4, 5)

    lita.mostrar()