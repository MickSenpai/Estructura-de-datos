class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Eliminacion:
    def __init__(self):
        self.raiz = None

    def insertar(self, numero):
        nuevo = Nodo(numero)
        nuevo.siguiente = self.raiz
        self.raiz = nuevo

    def eliminar(self, numero):
        actual = self.raiz
        anterior = None

        while actual != None:
            if actual.dato == numero:
                if anterior == None:
                    self.raiz = actual.siguiente
                else: 
                    anterior.siguiente = actual.siguiente

                return

            anterior = actual
            actual = actual.siguiente

        return False

    def mostrar(self):
        actual = self.raiz

        while actual:
            print(actual.dato, end= " -> ")
            actual = actual.siguiente

        print()

if __name__ == "__main__":
    litas = Eliminacion()

    litas.insertar(32)
    litas.insertar(24)
    litas.insertar(16)
    litas.insertar(8)

    litas.mostrar()

    litas.eliminar(32)

    litas.mostrar()