class Colasimple:
    def __init__(self, max_size):
        self.max = max_size
        self.cola = [None] * (self.max + 1)
        self.front = 0
        self.back = 0

    def es_vacia(self):
        return self.front == 0 and self.back == 0

    def es_llena(self):
        return self.back == self.max

    def size(self):
        return self.back - self.front
    
    def enqueue(self, elemento):
        if not self.es_llena():
            self.back = self.back + 1
            self.cola[self.back] = elemento
        else:
            print("La cola está llena")
            
    def mostrar(self):
        if self.es_vacia():
            print("Cola vacía")
        else:
            print(self.cola[self.front + 1 : self.back + 1])
    
    def obtener_pares(self):
        if self.es_vacia():
            print("Cola vacía, no hay elementos para obtener")
            return []

        pares = []
        for i in range(self.front + 1, self.back + 1):
            if self.cola[i] % 2 == 0:
                pares.append(self.cola[i])
        
        return pares


max_size = int(input("Introduce el tamaño máximo de la cola: "))
cola1 = Colasimple(max_size)

for m in range(max_size):
    if cola1.es_llena():
        print("La cola está llena")
        break
    elemento = int(input("Agrega el elemento: "))
    cola1.enqueue(elemento)

print("Contenido de la cola:")
cola1.mostrar()

pares = cola1.obtener_pares()

if pares:
    print(f"Números pares en la cola: {pares}")
else:
    print("No se encontraron números pares.")

