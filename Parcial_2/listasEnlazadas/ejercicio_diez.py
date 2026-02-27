class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Names:
    def __init__(self):
        self.raiz = None

    def agregar(self, nombre):
        nuevo = Nodo(nombre)
        nuevo.siguiente = self.raiz
        self.raiz = nuevo

    def mostrar(self):
        actual = self.raiz
        
        while actual:
            print(actual.dato, end= "-> ")
            actual = actual.siguiente

        print()

if __name__ == "__main__":
    litas = Names()


    litas.agregar("Jesus")
    litas.agregar("Imelda")
    litas.agregar("Santiago")
    litas.agregar("Cheli")
    litas.agregar("Mick")

    litas.mostrar()