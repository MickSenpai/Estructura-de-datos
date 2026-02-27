import random

class Buscar:
    def __init__(self, numero):
        self.lista = [10, 9, 11, 24, 43, 5, 1, 6]
        self.numero = numero

        for x in self.lista:
            if x == self.numero:
                print(f"El numero {x} si esta")
                break
    
class Mayor_menor:
    def __init__(self):
        self.lista = [10, 9, 11, 24, 43, 5, 6]
        self.numMenor = -1
        self.numMWardado = -1
        self.mayor = 0

        for x in self.lista:           
            self.numMWardado = x

            if  x < self.numMWardado:
                self.mayor = self.numMWardado

            elif x > self.numMenor: 
                self.numMenor = self.numMWardado


        print(f"El numero {self.numMWardado} es menor")
        print(f"El numero {self.numMenor} es mayor")

class Inversion:
    def __init__(self):
        self.lista = [10, 9, 11, 24, 43, 5, 6]
        
        for x in range(len(self.lista) -1, -1, -1):
            print(self.lista[x])

class Randoms:
    def __init__(self):
        self.lista = [random.randint(1, 10) for _ in range(20)]
        self.listaNueva = []

        for x in self.lista:
            if x not in self.listaNueva:
                self.listaNueva.append(x)
        
        print("Lista Vieja")
        print(self.lista)

        print("Lista Nueva")
        print(self.listaNueva)


class Posicion:
    def __init__(self):
        self.lista = [5, 8, 2, 10, 3, 9, 7]

        self.mayor = float('-inf')
        self.segundo_mayor = float('-inf')

        for num in self.lista:
            if num > self.mayor:
                self.segundo_mayor = self.mayor
                self.mayor = num
            elif num > self.segundo_mayor and num != self.mayor:
                self.segundo_mayor= num

        print("El segundo número self.mayor es:", self.segundo_mayor)

class main:
    def __init__(self):
        #numero = int(input("Ingrese un numero: "))

        #Buscar(numero)

        #Mayor_menor()

        #Inversion()
        
        Randoms()

        # Posicion()



if __name__ == "__main__":
    main()