class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Busquedas:
    def __init__(self):
        self.raiz = None

    def agregar(self, numero):
        nuevo = Nodo(numero)
        nuevo.siguiente = self.raiz
        self.raiz = nuevo

    def buscar(self, valor):    
        actual = self.raiz

        while actual != None:
            if actual.dato == valor:
                print(f"Se encontro el dato {actual.dato}")

                return 
            actual = actual.siguiente

        print("No existe tal vaina")
        return False

    def mostrar(self):
        actual = self.raiz

        while actual:
            print(actual.dato, end= " -> ")
            actual = actual.siguiente

        print()

if __name__ == "__main__":
    litas = Busquedas()

    litas.agregar(1)
    litas.agregar(2)
    litas.agregar(3)
    litas.agregar(4)
    litas.agregar(5)
    litas.agregar(6)

    litas.mostrar()

    litas.buscar(7)