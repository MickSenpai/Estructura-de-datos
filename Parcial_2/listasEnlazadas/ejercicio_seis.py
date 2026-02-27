class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Insercion:
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

                return True

            anterior = actual
            actual = actual.siguiente
        
        return False

    def mostrar_lista(self):
        actual = self.raiz
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

        print()

if __name__ == "__main__":
    
    litas = Insercion()

    litas.insertar(300)
    litas.insertar(200)
    litas.insertar(100)

    litas.mostrar_lista()

    litas.eliminar(100)

    litas.mostrar_lista()