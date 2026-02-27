class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Busqueda:
    def __init__(self):
        self.raiz = None

    def agregar(self, numero):
        nuevo = Nodo(numero)
        nuevo.siguiente = self.raiz
        self.raiz = nuevo

    def buscar(self):
        actual = self.raiz

        while actual != None:
            if actual.dato % 2 == 0:
                print(actual.dato, end= " -> ")

            actual = actual.siguiente

        print() 
        return False

    def mostrar(self):
        actual = self.raiz

        while actual:
            print(actual.dato, end= "-> ")
            actual = actual.siguiente

        print()
    
if __name__ == "__main__":
    litas = Busqueda()

    litas.agregar(10)
    litas.agregar(9)
    litas.agregar(8)
    litas.agregar(7)
    litas.agregar(6)
    litas.agregar(5)
    litas.agregar(4)
    litas.agregar(3)
    litas.agregar(2)
    litas.agregar(1)

    litas.mostrar()
    litas.buscar()