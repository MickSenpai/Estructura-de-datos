class Nodo:
    def __init__(self, dato):
        self.dato = dato #guarda el valor del nodo
        self.siguiente = None #Enlace   

if __name__ == "__main__":
    raiz = Nodo(1) #Creamos nuetra raiz, tendra valor 1
    maria = raiz #Maria esta en la raiz

    juan = Nodo(2) #Nuevo modo despues de Juan
    maria.siguiente = juan #Maria hace ref a juan
    maria = juan

    juan2punto0 = Nodo(2.3)
    juan.siguiente = juan2punto0
    juan = juan2punto0
    
    jose = Nodo(3)
    juan2punto0.siguiente = jose
    juan2punto0 = jose

    joseN = Nodo(3.4)
    jose.siguiente = joseN
    jose = joseN
    
    miguel = Nodo(4)
    joseN.siguiente = miguel
    joseN = miguel

    daniel = Nodo(5)
    miguel.siguiente = daniel
    miguel = daniel

    paco = Nodo(6)
    daniel.siguiente = paco
    daniel = paco
    
    jose = raiz #Inicio de la lista
    while maria:
        print(maria.dato)
        maria = maria.siguiente