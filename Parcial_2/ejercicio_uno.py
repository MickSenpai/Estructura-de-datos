class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Inserciones:
    def __init__(self):
        self.raiz = None

    def lista_inicial(self, nodo, nodo_2, nodo_3):
        self.raiz = Nodo(nodo)
        valor1 = self.raiz

        valor2 = Nodo(nodo_2)
        valor1.siguiente = valor2
        valor1 = valor2

        valor3 = Nodo(nodo_3)
        valor2.siguiente = valor3
        valor2 = valor3

    def insertar_en_inicio(self, numero):
        nuevo = Nodo(numero)
        nuevo.siguiente = self.raiz
        self.raiz = nuevo

    def mostrar_lista(self):
        actual = self.raiz
        while actual:
            print(actual.dato, end= " -> ")
            actual = actual.siguiente

        print()

if __name__ == "__main__":
    
    litas = Inserciones()

    litas.lista_inicial(10, 20, 30)

    litas.mostrar_lista()

    litas.insertar_en_inicio(5)

    litas.mostrar_lista()