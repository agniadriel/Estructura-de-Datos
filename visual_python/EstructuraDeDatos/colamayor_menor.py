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
            print ("cola vacia")
        else:
            print (self.cola[self.front + 1: self.back + 1])
    
    def obtener_elemento_mayor(self):
        if self.es_vacia():
            print("Cola vacía, no hay elementos para obtener")
            return elemento
        
        max_elemento = self.cola[self.front + 1]
        for i in range(self.front + 2, self.back + 1):
            if self.cola[i] > max_elemento:
                max_elemento = self.cola[i]
        
        return max_elemento
                
max_size = int(input("Introduce el tamaño maximo de la cola: "))
cola1 = Colasimple(max_size)

for m in range(max_size):
    if cola1.es_llena():
        print("la cola esta llena")
        break
    elemento = int(input("agregue el elemento: " ))
    cola1.enqueue(elemento)
    
print("Contenido de la cola")

cola1.mostrar()

elemento_mayor = cola1.obtener_elemento_mayor()

if elemento_mayor:
    print(f"Elemento mayor en la cola: {elemento_mayor}")
